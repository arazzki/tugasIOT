/*
 * Tugas 4 - IoT Platform Review: Antares IoT (Telkom Indonesia)
 * Mata Kuliah: Internet of Things (ITH3V3)
 * Deskripsi: Mengirimkan data telemetri sensor ke Antares oneM2M Platform via HTTPS (Port 8443).
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include <WiFiClientSecure.h>
#include "DHT.h"

// Konfigurasi Wi-Fi (Gunakan Wokwi-GUEST jika di simulator Wokwi)
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// Konfigurasi Antares oneM2M (HTTPS Port 8443)
const char* antaresServer = "https://platform.antares.id:8443/~/antares-cse/antares-id";

#if __has_include("config.secrets.h")
  #include "config.secrets.h"
  const char* accessKey       = ANTARES_ACCESS_KEY;
  const char* applicationName = ANTARES_APP_NAME;
  const char* deviceName      = ANTARES_DEV_NAME;
#else
  const char* accessKey       = "YOUR_ANTARES_ACCESS_KEY";
  const char* applicationName = "tugasIOT4";
  const char* deviceName      = "ESP32Node";
#endif

// Pinout Sensor & Aktuator
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
    WiFiClientSecure secureClient;
    secureClient.setInsecure(); // Mengizinkan self-signed / public CA tanpa sertifikat manual

    HTTPClient http;
    String endpoint = String(antaresServer) + "/" + applicationName + "/" + deviceName;

    http.begin(secureClient, endpoint);
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
