#include <WiFi.h>


const char* ssid = "iPhone";
const char* password = "123456789";

void setup() {
  Serial.begin(115200);
  delay(10);

  Serial.println("\nMenghubungkan ke jaringan...");

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi berhasil terhubung!");
  Serial.print("Alamat IP DHCP: ");
  Serial.println(WiFi.localIP()); // Memunculkan IP Address ke Serial Monitor sebagai bukti
}

void loop() {
}
