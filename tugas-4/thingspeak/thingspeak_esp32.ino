/*
 * Tugas 4 - IoT Platform Review: ThingSpeak
 * Mata Kuliah: Internet of Things (ITH3V3)
 * Deskripsi: Membaca data sensor DHT22 (Suhu & Kelembaban) dan mengirimkan ke ThingSpeak Channel via HTTP/REST.
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

// Konfigurasi Wi-Fi (Gunakan Wokwi-GUEST jika menjalankan di simulator Wokwi)
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// Konfigurasi ThingSpeak
const char* server = "api.thingspeak.com";
const char* writeAPIKey = "VC8CYXGXO2XKIXVF";

// Konfigurasi Sensor DHT
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// Konfigurasi Indikator LED
#define LED_PIN 2

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  dht.begin();

  Serial.println("\n[ThingSpeak] Menghubungkan ke Wi-Fi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n[ThingSpeak] Wi-Fi Terhubung!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // ThingSpeak rate limit: minimal interval 15 detik untuk akun free
  delay(15000);

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("[ThingSpeak] Gagal membaca sensor DHT!");
    return;
  }

  Serial.printf("[ThingSpeak] Suhu: %.2f °C | Kelembaban: %.2f %%\n", temperature, humidity);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = String("https://") + server + "/update?api_key=" + writeAPIKey +
                 "&field1=" + String(temperature) +
                 "&field2=" + String(humidity);

    http.begin(url);
    int httpCode = http.GET();

    if (httpCode > 0) {
      String payload = http.getString();
      Serial.printf("[ThingSpeak] Data berhasil dikirim! Response Code: %d, Entry ID: %s\n", httpCode, payload.c_str());
      digitalWrite(LED_PIN, HIGH);
      delay(200);
      digitalWrite(LED_PIN, LOW);
    } else {
      Serial.printf("[ThingSpeak] Gagal mengirim data. HTTP Error: %s\n", http.errorToString(httpCode).c_str());
    }
    http.end();
  } else {
    Serial.println("[ThingSpeak] Wi-Fi terputus!");
  }
}
