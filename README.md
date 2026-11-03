# 🌐 Tugas 4 - Review IoT Platform & MCP Server (ITH3V3)

Repositori ini berisi implementasi kode, simulasi Wokwi, konfigurasi platform IoT, serta pengembangan **Model Context Protocol (MCP) Server** untuk **Tugas 4 (Review & Implementasi IoT Platform)** pada mata kuliah **Internet of Things (ITH3V3)**.

> 👥 **Catatan Kelompok:** Proyek ini merupakan bagian dari tugas kelompok, di mana repositori ini berfokus khusus pada penyelesaian **Tugas 4 (Review 4 IoT Platform + Inovasi MCP Server)**.

---

## 📋 Informasi Akademik

- **Mata Kuliah:** Internet of Things (ITH3V3)
- **Dosen Pengampu:** UIW & PHV
- **Mahasiswa (Bagian Tugas 4):** Ariq Azzki
- **NIM:** 103032400138

---

## 📚 Ruang Lingkup Tugas 4

Fokus pada analisis komparatif, review fitur, serta tutorial dan pengujian implementasi platform IoT berbasis cloud:

1. **Platform yang Di-review & Diuji Secara Live:**
   - [**ThingSpeak**](https://thingspeak.com/) – Channel ID `3564706` (Telemetri data sensor).
   - [**Adafruit IO**](https://io.adafruit.com/AriqAzzki/feeds) – Feeds `suhu`, `kelembaban`, dan kendali `saklar-relay` dua arah.
   - [**Antares IoT (Telkom)**](https://antares.id/) – Aplikasi `tugasIOT4` / Device `ESP32Node` (oneM2M HTTPS Port 8443).
   - [**Arduino Cloud / IoT**](https://create.arduino.cc/iot/) – Ekosistem cloud terpadu dengan sinkronisasi variabel.

2. **Eksplorasi & Tutorial Praktis:**
   - Integrasi firmware ESP32 dengan sensor suhu/kelembaban (DHT22) dan aktuator (Relay).
   - Skema simulasi virtual interaktif menggunakan [**Wokwi Simulator**](https://wokwi.com/) (menggunakan Wi-Fi `Wokwi-GUEST`).
   - Pengiriman telemetri sensor (*uplink*) dan kontrol aktuator (*downlink*).

3. **Inovasi Model Context Protocol (MCP) Server:**
   - Server perantara berbasis Python (`mcp` SDK) yang memungkinkan Artificial Intelligence (seperti Antigravity, Claude, atau Cursor) untuk berinteraksi langsung dengan platform IoT (membaca feed data sensor dan mengendalikan aktuator secara otonom).

---

## 🛠️ Kebutuhan Hardware & Software

### Perangkat & Lingkungan Simulasi
- **Mikrokontroler:** ESP32 Dev Module (Fisik atau Virtual via [Wokwi](https://wokwi.com/))
- **Sensor & Aktuator:** Sensor Suhu/Kelembaban (DHT22), Modul Relay 5V, Indikator LED
- **Konektivitas:** Wi-Fi (SSID `Wokwi-GUEST` untuk simulasi atau Wi-Fi Access Point fisik)

### Perangkat Lunak & Pustaka
- **IDE:** Arduino IDE / VS Code
- **Runtime MCP Server:** Python 3.10+ (`mcp`, `httpx`, `python-dotenv`)
- **Libraries Arduino/Wokwi:**
  - `WiFi.h` & `WiFiClientSecure.h`
  - `PubSubClient` (untuk MQTT Adafruit IO)
  - `DHT sensor library`

---

## 📂 Struktur Direktori

```text
tugasIOT/
├── tugas-4/              # Kode sketch Arduino & skema Tugas 4
│   ├── thingspeak/       # Firmware ESP32 ThingSpeak
│   ├── adafruit_io/      # Firmware ESP32 MQTT Adafruit IO
│   ├── antares/          # Firmware ESP32 oneM2M HTTPS Antares
│   ├── arduino_cloud/    # Firmware ESP32 Arduino IoT Cloud
│   └── wokwi/            # Konfigurasi simulasi Wokwi (diagram.json)
│
├── mcp-server/           # MCP (Model Context Protocol) Server IoT
│   ├── server.py         # Script utama server FastMCP / MCPServer
│   ├── requirements.txt  # Dependensi Python
│   ├── .env.example      # Template konfigurasi API Key
│   └── README.md         # Panduan penggunaan MCP Server
│
├── .gitignore            # Filter file build, .docx, dan kredensial sensitif
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
