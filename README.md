# 🌐 Tugas Kuliah Internet of Things (ITH3V3)

Repositori ini berisi kumpulan tugas, implementasi kode, dan dokumentasi laporan untuk mata kuliah **Internet of Things (ITH3V3)**.

---

## 📋 Informasi Akademik

- **Mata Kuliah:** Internet of Things (ITH3V3)
- **Dosen Pengampu:** UIW & PHV
- **Mahasiswa:** [Nama Lengkap]
- **NIM:** [Nomor Induk Mahasiswa]

---

## 📚 Daftar & Ruang Lingkup Tugas

### 🔹 [Tugas 2 - Communication Protocol](file:///e:/Project/tugasIOT/Tugas%202%20-%20Internet%20of%20Things%20-%20Communication%20Protocol-UIW.docx)
Fokus pada pemahaman protokol komunikasi serial kabel (*wired*) dan nirkabel (*wireless*) pada mikrokontroler:
1. **Universal Asynchronous Receiver Transmitter (UART):** Konsep komunikasi serial asinkron, baud rate, pin TX/RX.
2. **Serial Peripheral Interface (SPI):** Konsep komunikasi sinkron full-duplex berbasis Master-Slave (MOSI, MISO, SCK, CS/SS).
3. **Inter-Integrated Circuit (I2C / IIC):** Komunikasi multi-master multi-slave menggunakan 2 jalur kabel (SDA & SCL) dengan pengalamatan berbasis alamat perangkat (*device address*).
4. **Bluetooth & Zigbee:** Karakteristik, topologi jaringan, efisiensi daya, dan perbandingan jangkauan komunikasi personal area network (PAN/WPAN).
5. **Implementasi Program (ESP32/ESP8266):**
   - Pembuatan program berbasis Arduino IDE untuk menampilkan konversi nilai format desimal ke **Biner**, **Heksadesimal**, dan **Oktal** pada Serial Monitor.
   - Analisis performa dan cara kerja konversi data di mikrokontroler.

---

### 🔹 [Tugas 3 - IP Based Communication Protocol](file:///e:/Project/tugasIOT/Tugas%203%20-%20Internet%20of%20Things%20-%20IP%20Based%20Communication%20Protocol-UIW.docx)
Fokus pada protokol lapisan aplikasi berbasis Internet Protocol (IP) yang umum digunakan pada ekosistem IoT:
1. **Message Queuing Telemetry Transport (MQTT):**
   - Mekanisme arsitektur *Publish-Subscribe* melalui perantara *MQTT Broker*.
   - Efisiensi overhead header paket dan level Quality of Service (QoS 0, 1, 2).
2. **Constrained Application Protocol (CoAP):**
   - Arsitektur berbasis RESTful khusus untuk perangkat dengan sumber daya terbatas (*constrained devices*).
   - Penggunaan protokol transport UDP untuk efisiensi latensi dan konsumsi bandwidth.
3. **Komparasi Protokol: CoAP vs HTTP:**
   - Perbandingan transport layer (UDP vs TCP), ukuran header, model komunikasi (Request/Response & Asynchronous Observe), dan efisiensi energi.
4. **Implementasi Program (ESP32/ESP8266):**
   - Menghubungkan modul ESP8266/ESP32 ke jaringan Wi-Fi lokal (Access Point).
   - Mendapatkan alokasi alamat IP secara dinamis via DHCP dan menampilkannya pada Serial Monitor sebagai verifikasi konektivitas jaringan.
   - Analisis proses *handshake* dan stabilitas koneksi Wi-Fi.

---

### 🔹 [Tugas 5 - Review IoT Platform](file:///e:/Project/tugasIOT/Tugas%205%20-%20Internet%20of%20Things%20-%20Review%20IoT%20Platform-UIW.docx)
Fokus pada analisis komparatif, review fitur, serta tutorial implementasi platform IoT berbasis cloud:
1. **Platform yang Di-review:**
   - [ThingSpeak](https://thingspeak.com/) – Platform analisis data dan visualisasi MATLAB untuk IoT.
   - [Adafruit IO](https://io.adafruit.com/) – Platform dashboard IoT interaktif dengan dukungan feed dan trigger MQTT/HTTP.
   - [Arduino Cloud / IoT](https://create.arduino.cc/iot/) – Ekosistem cloud terintegrasi untuk board Arduino dan ESP.
   - [Antares IoT](https://antares.id/id/index.html) – Platform IoT enterprise lokal berbasis standar oneM2M dari Telkom Indonesia.
2. **Eksplorasi & Tutorial Praktis:**
   - Integrasi perangkat ESP8266/ESP32 dengan sensor dan aktuator.
   - Pengiriman data telemetri sensor (*uplink*) dan penerimaan perintah kontrol (*downlink*) pada masing-masing platform.
   - Dokumentasi tutorial langkah demi langkah konfigurasi setiap platform.

---

## 🛠️ Kebutuhan Hardware & Software

### Perangkat Keras (Hardware)
- **Mikrokontroler:** ESP32 Dev Module / ESP8266 NodeMCU
- **Sensor & Aktuator:** Sensor Suhu/Kelembaban (DHT11/DHT22), LDR, LED, Modul Relay 5V
- **Konektivitas:** Wi-Fi Access Point / Hotspot
- **Aksesoris:** Breadboard, Kabel Jumper, Kabel Data Micro-USB/Type-C

### Perangkat Lunak (Software)
- **IDE:** [Arduino IDE](https://www.arduino.cc/) atau VS Code + PlatformIO
- **Core Board:** ESP32 by Espressif / ESP8266 by ESP8266 Community
- **Libraries:**
  - `WiFi.h` / `ESP8266WiFi.h`
  - `PubSubClient` (untuk MQTT)
  - `ThingSpeak` Library
  - `Adafruit IO Arduino`
  - `AntaresESPHTTP` / `AntaresESP32MQTT`

---

## 📂 Struktur Direktori

```text
tugasIOT/
├── Tugas 2 - Internet of Things - Communication Protocol-UIW.docx
├── Tugas 3 - Internet of Things - IP Based Communication Protocol-UIW.docx
├── Tugas 5 - Internet of Things - Review IoT Platform-UIW.docx
│
├── tugas-2/              # Kode sketch & laporan Tugas 2 (Konversi Biner/Hexa/Oktal)
│   └── tugas2_radix_converter/
│       └── tugas2_radix_converter.ino
│
├── tugas-3/              # Kode sketch & laporan Tugas 3 (Koneksi WiFi & DHCP IP)
│   └── tugas3_wifi_dhcp/
│       └── tugas3_wifi_dhcp.ino
│
├── tugas-5/              # Kode sketch & tutorial Tugas 5 (ThingSpeak, Adafruit IO, Arduino Cloud, Antares)
│   ├── thingspeak/
│   ├── adafruit_io/
│   ├── arduino_cloud/
│   └── antares/
│
├── .gitignore            # Filter file build dan kredensial sensitif
└── README.md             # Dokumentasi utama repositori
```

---

## 🚀 Panduan Penggunaan & Upload Kode

1. **Clone Repositori:**
   ```bash
   git clone https://github.com/arazzki/tugasIOT.git
   cd tugasIOT
   ```
2. **Buka Program di Arduino IDE:**
   - Buka file sketch `.ino` sesuai tugas yang ingin dijalankan.
   - Pilih jenis board (`Tools > Board > ESP32 Dev Module` atau `NodeMCU 1.0`).
   - Pilih COM Port yang terhubung.
3. **Konfigurasi Kredensial:**
   - Sesuaikan SSID, Password Wi-Fi, dan API Key platform pada kode.
4. **Upload & Monitor:**
   - Klik tombol **Upload**.
   - Buka **Serial Monitor** pada baud rate `115200` (atau sesuai konfigurasi `Serial.begin()`).

---

## 📄 Lisensi & Hak Cipta
Dokumentasi dan kode dalam repositori ini disusun untuk memenuhi tugas akademik mata kuliah Internet of Things (ITH3V3).
