/*
 * Tugas 4 - IoT Platform Review: Arduino Cloud / IoT
 * Mata Kuliah: Internet of Things (ITH3V3)
 * Deskripsi: Menghubungkan ESP32 ke Arduino IoT Cloud, sinkronisasi variabel suhu, kelembaban, dan saklar relay.
 */

#include "thingProperties.h"
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

#define RELAY_PIN 5

void setup() {
  Serial.begin(115200);
  delay(1500);

  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
  dht.begin();

  // Inisialisasi properti cloud dari thingProperties.h
  initProperties();

  // Koneksi ke Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();

  static unsigned long lastMillis = 0;
  if (millis() - lastMillis > 5000) {
    lastMillis = millis();

    float t = dht.readTemperature();
    float h = dht.readHumidity();

    if (!isnan(t) && !isnan(h)) {
      temperature = t;  // Variabel Cloud
      humidity = h;     // Variabel Cloud
      Serial.printf("[Arduino Cloud] Update Suhu: %.2f °C, Kelembaban: %.2f %%\n", t, h);
    }
  }
}

// Callback otomatis saat variabel relaySwitch diubah dari Dashboard Cloud
void onRelaySwitchChange() {
  if (relaySwitch) {
    digitalWrite(RELAY_PIN, HIGH);
    Serial.println("[Arduino Cloud] Relay Aktif (HIGH)");
  } else {
    digitalWrite(RELAY_PIN, LOW);
    Serial.println("[Arduino Cloud] Relay Nonaktif (LOW)");
  }
}
