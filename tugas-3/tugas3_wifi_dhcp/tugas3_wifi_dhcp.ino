/*
 * Tugas 3 - Internet of Things (ITH3V3)
 * Soal No 4: Program Koneksi Wi-Fi & Pembacaan IP DHCP
 * Deskripsi: Menghubungkan ESP32/ESP8266 ke Access Point (bisa menggunakan Wokwi-GUEST untuk simulator Wokwi)
 *            dan menampilkan informasi jaringan DHCP secara mendetail ke Serial Monitor.
 */

#include <WiFi.h>

// Konfigurasi Wi-Fi (Bisa disesuaikan untuk router fisik atau simulator Wokwi)
const char* ssid = "Wokwi-GUEST";     // Gunakan "Wokwi-GUEST" jika di Wokwi, atau SSID Wi-Fi rumah
const char* password = "";            // Kosongkan jika menggunakan Wokwi-GUEST

void setup() {
  Serial.begin(115200);
  while (!Serial) { delay(10); }

  Serial.println("\n=======================================================");
  Serial.println("  TUGAS 3 IOT: KONEKSI WI-FI & DHCP IP DISPLAY (ESP32)");
  Serial.println("=======================================================");

  WiFi.mode(WIFI_STA); // Mode Station (Klien)
  Serial.printf("Menghubungkan ke Access Point: %s ", ssid);

  unsigned long startTime = millis();
  WiFi.begin(ssid, password);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 40) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  unsigned long connectionTime = millis() - startTime;

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\n[STATUS: BERHASIL TERHUBUNG!]");
    Serial.println("-------------------------------------------------------");
    Serial.printf("Waktu Handshake & DHCP  : %lu ms\n", connectionTime);
    Serial.print("Alamat IP DHCP (IPv4)   : ");
    Serial.println(WiFi.localIP());
    Serial.print("Subnet Mask             : ");
    Serial.println(WiFi.subnetMask());
    Serial.print("Gateway IP              : ");
    Serial.println(WiFi.gatewayIP());
    Serial.print("DNS Server IP           : ");
    Serial.println(WiFi.dnsIP());
    Serial.print("MAC Address Perangkat   : ");
    Serial.println(WiFi.macAddress());
    Serial.printf("Kekuatan Sinyal (RSSI)  : %d dBm\n", WiFi.RSSI());
    Serial.println("-------------------------------------------------------\n");
  } else {
    Serial.println("\n[STATUS: GAGAL TERHUBUNG]");
    Serial.println("Periksa kembali SSID dan Password Wi-Fi Anda.");
  }
}

void loop() {
  // Tetap memantau status koneksi setiap 10 detik
  static unsigned long lastCheck = 0;
  if (millis() - lastCheck > 10000) {
    lastCheck = millis();
    if (WiFi.status() == WL_CONNECTED) {
      Serial.printf("[Ping Keep-Alive] IP: %s | RSSI: %d dBm\n", 
                    WiFi.localIP().toString().c_str(), WiFi.RSSI());
    } else {
      Serial.println("[Peringatan] Koneksi Wi-Fi terputus!");
    }
  }
}
