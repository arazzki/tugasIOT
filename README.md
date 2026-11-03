# 🌐 Repositori Tugas Kelompok - Internet of Things (ITH3V3)

Repositori ini merupakan repositori bersama (*group repository*) untuk pengerjaan tugas mata kuliah **Internet of Things (ITH3V3)**. Repositori ini mencakup seluruh implementasi firmware mikrokontroler (ESP32 / ESP8266), skema simulasi sirkuit virtual Wokwi, integrasi multi-platform cloud IoT, serta pengembangan arsitektur **Model Context Protocol (MCP) Server** untuk integrasi Artificial Intelligence (AI).

---

## 👥 Informasi Akademik & Anggota Kelompok

- **Mata Kuliah:** Internet of Things (ITH3V3)
- **Dosen Pengampu:** UIW & PHV

### Pembagian Tugas Kelompok:
| No | Nama Mahasiswa | NIM | Bagian Tugas / Tanggung Jawab |
| :---: | :--- | :---: | :--- |
| 1 | **Ariq Azzki** | **103032400138** | **Tugas 4:** Review 4 Platform IoT, Simulasi Wokwi & MCP Server |
| 2 | [Nama Anggota Kelompok] | [NIM] | **Tugas 2:** Communication Protocol (Serial & Wireless) |
| 3 | [Nama Anggota Kelompok] | [NIM] | **Tugas 3:** IP Based Communication Protocol (MQTT & CoAP) |

---

## 📚 Ruang Lingkup & Cakupan Tugas

### 🔹 [Tugas 2 - Communication Protocol](file:///e:/Project/tugasIOT/tugas-2/tugas2_radix_converter/tugas2_radix_converter.ino)
Fokus pada pemahaman protokol komunikasi serial kabel (*wired*) dan nirkabel (*wireless*) pada mikrokontroler:
1. **Universal Asynchronous Receiver Transmitter (UART):** Komunikasi asinkron titik-ke-titik, baud rate, framing data (TX/RX).
2. **Serial Peripheral Interface (SPI):** Komunikasi sinkron berkecepatan tinggi berbasis Master-Slave (MOSI, MISO, SCK, CS).
3. **Inter-Integrated Circuit (I2C / IIC):** Komunikasi berbasis bus dua kawat (SDA & SCL) dengan pengalamatan 7-bit/10-bit.
4. **Bluetooth & Zigbee:** Karakteristik perbandingan WPAN (Personal Area Network), konsumsi daya BLE vs topologi mesh Zigbee.
5. **Implementasi Program (ESP32):** Program konversi radiks bilangan (Desimal $\rightarrow$ Biner, Heksadesimal, Oktal) via Serial Monitor dengan pengukuran waktu komputasi mikrosekon.

---

### 🔹 [Tugas 3 - IP Based Communication Protocol](file:///e:/Project/tugasIOT/tugas-3/tugas3_wifi_dhcp/tugas3_wifi_dhcp.ino)
Fokus pada protokol lapisan aplikasi berbasis Internet Protocol (IP) untuk ekosistem IoT:
1. **Message Queuing Telemetry Transport (MQTT):** Arsitektur Publish-Subscribe melalui perantara MQTT Broker, efisiensi header 2 byte, dan level Quality of Service (QoS 0, 1, 2).
2. **Constrained Application Protocol (CoAP):** Protokol web berbasis RESTful untuk perangkat terbatas, berjalan di atas UDP port 5683.
3. **Komparasi Mendalam CoAP vs HTTP:** Perbandingan overhead header, latensi UDP vs TCP 3-way handshake, dan transmisi multicast.
4. **Implementasi Program (ESP32):** Menghubungkan perangkat ke Access Point Wi-Fi (mendukung router fisik atau `Wokwi-GUEST`), negosiasi DHCP DORA, serta pembacaan IP dan subnet ke Serial Monitor.

---

### 🔹 [Tugas 4 - Review IoT Platform & Inovasi MCP Server](file:///e:/Project/tugasIOT/tugas-4/)
Fokus pada analisis komparatif, pengujian live 4 platform IoT cloud, serta inovasi AI Agentic:
1. **Platform yang Di-review & Diuji Secara Live:**
   - [**ThingSpeak**](https://thingspeak.com/) – Channel ID `3564706` (Telemetri data sensor).
   - [**Adafruit IO**](https://io.adafruit.com/AriqAzzki/feeds) – Feeds `suhu`, `kelembaban`, dan kendali dua arah `saklar-relay`.
   - [**Antares IoT (Telkom)**](https://antares.id/) – Aplikasi `tugasIOT4` / Device `ESP32Node` (oneM2M HTTPS Port 8443).
   - [**Arduino Cloud / IoT**](https://create.arduino.cc/iot/) – Ekosistem cloud terpadu dengan sinkronisasi variabel instan.
2. **Simulasi Wokwi Lengkap:**
   - Skema sirkuit virtual siap pakai di [`tugas-4/wokwi/diagram.json`](file:///e:/Project/tugasIOT/tugas-4/wokwi/diagram.json) (ESP32 + DHT22 + Relay) yang terkoneksi langsung ke internet via `Wokwi-GUEST`.
3. **Pengembangan IoT Model Context Protocol (MCP) Server:**
   - Berada di [`mcp-server/`](file:///e:/Project/tugasIOT/mcp-server/) untuk memungkinkan AI (seperti Antigravity, Claude, atau Cursor) membaca data telemetri dan mengontrol relay platform secara otonom melalui bahasa alami.

---

## 🛠️ Kebutuhan Hardware & Software

### Hardware & Simulator
- **Mikrokontroler:** ESP32 Dev Module (Fisik atau Virtual via [Wokwi](https://wokwi.com/))
- **Sensor:** Sensor Suhu & Kelembaban (DHT11 / DHT22)
- **Aktuator:** Modul Relay 5V, Indikator LED
- **Konektivitas:** Wi-Fi (SSID `Wokwi-GUEST` untuk simulasi atau Wi-Fi Access Point fisik)

### Perangkat Lunak & Environment
- **IDE:** [Arduino IDE](https://www.arduino.cc/) / VS Code + PlatformIO
- **Runtime MCP Server:** Python 3.10+
- **Libraries Arduino/ESP32:**
  - `WiFi.h` & `WiFiClientSecure.h`
  - `PubSubClient` (untuk MQTT Adafruit IO)
  - `DHT sensor library`
  - `ThingSpeak` Library

---

## 📂 Struktur Direktori Repositori

```text
tugasIOT/
├── tugas-2/              # Tugas 2: Communication Protocol
│   └── tugas2_radix_converter/
│       └── tugas2_radix_converter.ino
│
├── tugas-3/              # Tugas 3: IP Based Communication Protocol
│   └── tugas3_wifi_dhcp/
│       └── tugas3_wifi_dhcp.ino
│
├── tugas-4/              # Tugas 4: Review 4 Platform IoT & Simulasi Wokwi
│   ├── thingspeak/       # Firmware ESP32 ThingSpeak (Channel 3564706)
│   ├── adafruit_io/      # Firmware ESP32 MQTT Adafruit IO
│   ├── antares/          # Firmware ESP32 oneM2M HTTPS Antares
│   ├── arduino_cloud/    # Firmware ESP32 Arduino IoT Cloud
│   └── wokwi/            # Konfigurasi simulasi Wokwi (diagram.json & wokwi.toml)
│
├── mcp-server/           # Inovasi AI: Model Context Protocol (MCP) Server
│   ├── server.py         # Script server FastMCP (ThingSpeak, Adafruit, Antares)
│   ├── requirements.txt  # Dependensi Python MCP
│   ├── .env.example      # Template kredensial API Key
│   └── README.md         # Dokumentasi integrasi MCP Client
│
├── .gitignore            # Filter build binary, kredensial sensitif, dan file .docx
└── README.md             # Dokumentasi utama proyek kelompok
```

---

## 🚀 Panduan Menjalankan Program

### 1. Menjalankan Sketch Arduino (ESP32)
1. Buka file `.ino` sesuai tugas yang ingin dijalankan di **Arduino IDE**.
2. Pilih Board: `Tools > Board > ESP32 Arduino > ESP32 Dev Module`.
3. Pilih Port COM yang sesuai.
4. Klik tombol **Upload**, lalu buka **Serial Monitor** pada baud rate `115200`.

### 2. Menjalankan Simulasi di Wokwi
1. Kunjungi **[https://wokwi.com/projects/new/esp32](https://wokwi.com/projects/new/esp32)**.
2. Salin isi file [`tugas-4/wokwi/diagram.json`](file:///e:/Project/tugasIOT/tugas-4/wokwi/diagram.json) ke tab diagram di Wokwi.
3. Tempelkan kode sketch dari folder tugas yang diinginkan.
4. Klik tombol **Play (Simulate)** ▶️ (Wi-Fi otomatis tersambung via `Wokwi-GUEST`).

### 3. Menjalankan MCP Server
1. Masuk ke direktori `mcp-server/`:
   ```bash
   cd mcp-server
   pip install -r requirements.txt
   ```
2. Buat file `.env` dari `.env.example` dan masukkan API Key platform IoT Anda.
3. Jalankan server:
   ```bash
   python server.py
   ```

---

## 📄 Lisensi & Hak Cipta
Repositori ini disusun sebagai pemenuhan tugas akademik kelompok mata kuliah Internet of Things (ITH3V3).
