/*
 * Tugas 4 - IoT Platform Review: Adafruit IO
 * Mata Kuliah: Internet of Things (ITH3V3)
 * Deskripsi: Publish data sensor ke feed Adafruit IO dan subscribe ke feed kontrol saklar/relay secara real-time via MQTT.
 */

#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// Konfigurasi Wi-Fi
const char* ssid = "NAMA_WIFI";
const char* password = "PASSWORD_WIFI";

// Konfigurasi Adafruit IO
#define IO_SERVER "io.adafruit.com"
#define IO_SERVERPORT 1883
#define IO_USERNAME "YOUR_AIO_USERNAME"
#define IO_KEY "YOUR_AIO_KEY"

// Topik MQTT Adafruit IO
const char* TOPIC_TEMP   = IO_USERNAME "/feeds/suhu";
const char* TOPIC_HUMID  = IO_USERNAME "/feeds/kelembaban";
const char* TOPIC_RELAY  = IO_USERNAME "/feeds/saklar-relay";

// Pinout
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

#define RELAY_PIN 5

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;

void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.printf("[Adafruit IO] Pesan masuk pada topik [%s]: %s\n", topic, message.c_str());

  if (String(topic) == TOPIC_RELAY) {
    if (message == "ON" || message == "1") {
      digitalWrite(RELAY_PIN, HIGH);
      Serial.println("[Adafruit IO] Relay / Aktuator: AKTIF (ON)");
    } else {
      digitalWrite(RELAY_PIN, LOW);
      Serial.println("[Adafruit IO] Relay / Aktuator: NONAKTIF (OFF)");
    }
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("[Adafruit IO] Mencoba koneksi MQTT...");
    String clientId = "ESP32Client-" + String(random(0xffff), HEX);
    if (client.connect(clientId.c_str(), IO_USERNAME, IO_KEY)) {
      Serial.println(" Terhubung!");
      client.subscribe(TOPIC_RELAY);
      Serial.printf("[Adafruit IO] Subscribed ke: %s\n", TOPIC_RELAY);
    } else {
      Serial.printf(" Gagal, rc=%d. Coba lagi dalam 5 detik...\n", client.state());
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.print("\n[Adafruit IO] Menghubungkan ke Wi-Fi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n[Adafruit IO] Wi-Fi Terhubung!");

  client.setServer(IO_SERVER, IO_SERVERPORT);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  // Kirim data setiap 10 detik
  if (now - lastMsg > 10000) {
    lastMsg = now;

    float h = dht.readHumidity();
    float t = dht.readTemperature();

    if (!isnan(t) && !isnan(h)) {
      client.publish(TOPIC_TEMP, String(t).c_str());
      client.publish(TOPIC_HUMID, String(h).c_str());
      Serial.printf("[Adafruit IO] Publish Suhu: %.2f °C | Kelembaban: %.2f %%\n", t, h);
    }
  }
}
