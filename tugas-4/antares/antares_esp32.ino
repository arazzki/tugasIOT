/*
 * Tugas 4 - IoT Platform Review: Antares IoT (Telkom Indonesia)
 * Mata Kuliah: Internet of Things (ITH3V3)
 * Deskripsi: Mengirimkan data sensor suhu dan kelembaban ke Antares oneM2M Platform via HTTP POST (Content Instance).
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

// Konfigurasi Wi-Fi
const char* ssid = "NAMA_WIFI";
const char* password = "PASSWORD_WIFI";

// Konfigurasi Antares oneM2M
const char* antaresServer = "http://platform.antares.id:8080/~/antares-cse/antares-id";
const char* accessKey = "YOUR_ANTARES_ACCESS_KEY";
const char* applicationName = "YOUR_APP_NAME";
const char* deviceName = "YOUR_DEVICE_NAME";

// Pinout
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

#define RELAY_PIN 5

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  dht.begin();

  Serial.println("\n[Antares] Menghubungkan ke Wi-Fi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n[Antares] Wi-Fi Terhubung!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  delay(10000); // Kirim data setiap 10 detik

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  if (isnan(temp) || isnan(hum)) {
    Serial.println("[Antares] Gagal membaca sensor DHT!");
    return;
  }

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String endpoint = String(antaresServer) + "/" + applicationName + "/" + deviceName;

    http.begin(endpoint);
    http.addHeader("X-M2M-Origin", accessKey);
    http.addHeader("Content-Type", "application/json;ty=4");
    http.addHeader("Accept", "application/json");

    // Format payload JSON oneM2M (cin / Content Instance)
    String dataJson = "{\"temp\":" + String(temp, 2) + ",\"hum\":" + String(hum, 2) + "}";
    String payload = "{\"m2m:cin\":{\"con\":\"" + dataJson + "\"}}";

    Serial.printf("[Antares] Mengirim data: %s\n", dataJson.c_str());
    int httpResponseCode = http.POST(payload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.printf("[Antares] Sukses! Response Code: %d\n", httpResponseCode);
    } else {
      Serial.printf("[Antares] Gagal kirim. HTTP Error code: %d\n", httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("[Antares] Wi-Fi terputus!");
  }
}
