# 🔌 IoT Platforms MCP Server

Model Context Protocol (MCP) Server untuk menghubungkan **Large Language Model (LLM)** seperti Antigravity, Claude Desktop, atau Cursor ke berbagai **Platform IoT** (ThingSpeak, Adafruit IO, dan Antares IoT).

---

## 🚀 Fitur & Tools

| Nama Tool | Platform | Fungsi |
| :--- | :--- | :--- |
| `get_thingspeak_feeds` | ThingSpeak | Membaca riwayat data telemetri sensor dari channel |
| `send_thingspeak_data` | ThingSpeak | Mengirim data suhu/kelembaban ke channel |
| `get_adafruit_feed` | Adafruit IO | Mengambil nilai terakhir dari feed sensor/saklar |
| `set_adafruit_feed` | Adafruit IO | Mengontrol aktuator/relay (ON/OFF) via feed |
| `get_antares_latest_data`| Antares | Mengambil data telemetri oneM2M terakhir |
| `send_antares_data` | Antares | Mengirimkan payload JSON oneM2M ke perangkat Antares |

---

## 🛠️ Instalasi & Konfigurasi

### 1. Pasang Dependensi
Pastikan Python 3.10+ sudah terpasang, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 2. Atur Kredensial Environment
Salin file `.env.example` menjadi `.env`:
```bash
cp .env.example .env
```
Lalu isi kredensial akun IoT Anda di file `.env`.

---

## ⚙️ Integrasi dengan MCP Client

### Konfigurasi Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "iot-platform": {
      "command": "python",
      "args": ["E:\\Project\\tugasIOT\\mcp-server\\server.py"],
      "env": {
        "THINGSPEAK_CHANNEL_ID": "YOUR_CHANNEL_ID",
        "THINGSPEAK_READ_KEY": "YOUR_READ_KEY",
        "THINGSPEAK_WRITE_KEY": "YOUR_WRITE_KEY",
        "ADAFRUIT_IO_USERNAME": "YOUR_USERNAME",
        "ADAFRUIT_IO_KEY": "YOUR_AIO_KEY",
        "ANTARES_ACCESS_KEY": "YOUR_ACCESS_KEY",
        "ANTARES_APPLICATION_NAME": "YOUR_APP_NAME",
        "ANTARES_DEVICE_NAME": "YOUR_DEVICE_NAME"
      }
    }
  }
}
```

---

## 💬 Contoh Prompt Penggunaan dengan AI
- *"Berapa suhu dan kelembaban ruangan saat ini dari ThingSpeak?"*
- *"Tolong nyalakan saklar relay di Adafruit IO."*
- *"Tampilkan data JSON telemetri terakhir yang tersimpan di Antares."*
