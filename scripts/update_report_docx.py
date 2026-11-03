#!/usr/bin/env python3
"""
Script untuk mengisi laporan Tugas 4 (Review IoT Platform) secara otomatis
ke dalam file Word template: 'Tugas 5 - Internet of Things - Review IoT Platform-UIW.docx'.
"""

import sys
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def fill_report(nama_mahasiswa: str, nim: str, docx_path: str = "Tugas 5 - Internet of Things - Review IoT Platform-UIW.docx", output_path: str = None):
    if output_path is None:
        output_path = docx_path

    doc = docx.Document(docx_path)

    # 1. Update Identitas Mahasiswa di Table 0
    t0 = doc.tables[0]
    t0.rows[2].cells[0].text = f"Nama Mahasiswa:\n\n{nama_mahasiswa}"
    t0.rows[2].cells[1].text = f"Nama Mahasiswa:\n\n{nama_mahasiswa}"
    t0.rows[2].cells[2].text = f"NIM:\n\n{nim}"

    # 2. Update Jawaban di Table 2
    t2 = doc.tables[2]
    ans_cell = t2.rows[2].cells[0]

    # Bersihkan paragraf lama
    ans_cell.text = ""

    def add_p(text="", bold=False, italic=False, size=11, space_after=6, heading_level=0):
        p = ans_cell.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        
        if heading_level == 1:
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run(text)
            run.bold = True
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(0, 51, 102)
        elif heading_level == 2:
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(text)
            run.bold = True
            run.font.size = Pt(11.5)
            run.font.color.rgb = RGBColor(0, 102, 153)
        else:
            run = p.add_run(text)
            run.bold = bold
            run.italic = italic
            run.font.size = Pt(size)
        return p

    def add_bullet(text, bold_prefix="", size=10.5):
        p = ans_cell.add_paragraph()
        p.paragraph_format.left_indent = Pt(14)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        p.add_run("• ")
        if bold_prefix:
            r1 = p.add_run(bold_prefix)
            r1.bold = True
            r1.font.size = Pt(size)
        r2 = p.add_run(text)
        r2.font.size = Pt(size)
        return p

    # --- Header Jawaban ---
    add_p("LAPORAN PRAKTIKUM & REVIEW IOT PLATFORM", bold=True, size=12)
    add_p("Mata Kuliah: Internet of Things (ITH3V3) | Dosen: UIW dan PHV", italic=True, size=10)
    add_p("-" * 80, size=9)

    # --- BAGIAN 1: REVIEW KOMPARATIF 4 PLATFORM IOT ---
    add_p("A. Review Komparatif Platform IoT", heading_level=1)
    add_p(
        "Pada tugas ini dilakukan eksplorasi dan komparasi terhadap 4 (empat) platform IoT populer, yaitu "
        "ThingSpeak, Adafruit IO, Arduino Cloud / IoT, dan Antares IoT. Setiap platform memiliki karakteristik arsitektur, "
        "fitur visualisasi, serta target use-case yang berbeda:"
    )

    add_p("1. ThingSpeak (MathWorks)", heading_level=2)
    add_bullet(" Dikembangkan oleh MathWorks, berfokus kuat pada analisis data telemetri berbasis MATLAB Analytics.", "Deskripsi & Fokus:")
    add_bullet(" RESTful HTTP (GET/POST) dan MQTT (Port 1883/8883).", "Protokol Komunikasi:")
    add_bullet(" Data disimpan dalam konsep 'Channels' dengan maksimal 8 fields numerik per channel.", "Model Data:")
    add_bullet(" Kompatibilitas langsung dengan fungsi MATLAB untuk pemrosesan sinyal, machine learning, dan visualisasi grafik.", "Keunggulan Utama:")
    add_bullet(" Adanya rate-limiting 15 detik pada tier gratis (free license), serta kurang optimal untuk kontrol aktuator dua arah (downlink realtime).", "Kelemahan:")

    add_p("2. Adafruit IO", heading_level=2)
    add_bullet(" Platform IoT open ecosystem yang dirancang untuk prototyping cepat, maker, dan sistem kontrol interaktif.", "Deskripsi & Fokus:")
    add_bullet(" MQTT (Publish-Subscribe realtime) dan RESTful HTTP API.", "Protokol Komunikasi:")
    add_bullet(" Menggunakan konsep 'Feeds' (aliran data individual) yang dapat dirangkai ke dalam 'Dashboards'.", "Model Data:")
    add_bullet(" Dashboard sangat kaya widget interaktif (Toggle Switch, Slider, Gauge, Momentary Button, Color Picker). Sangat responsif untuk kendali dua arah (uplink telemetri dan downlink kontrol).", "Keunggulan Utama:")
    add_bullet(" Kuota akun gratis dibatasi hingga 30 data points per menit dan maksimal 10 feeds aktif.", "Kelemahan:")

    add_p("3. Arduino Cloud / IoT", heading_level=2)
    add_bullet(" Platform cloud terintegrasi milik Arduino yang mendukung board resmi maupun pihak ketiga seperti ESP32 dan ESP8266.", "Deskripsi & Fokus:")
    add_bullet(" MQTT Over TLS / Secure WebSockets dengan enkripsi end-to-end berbasis crypto chip/software keys.", "Protokol Komunikasi:")
    add_bullet(" Konsep 'Thing' yang mengikat 'Variables' cloud. Variabel di kode mikrokontroler otomatis sinkron dua arah dengan dashboard.", "Model Data:")
    add_bullet(" Pengkodean sangat mudah melalui Web Editor, integrasi OTA (Over-The-Air) update, dan aplikasi mobile (Arduino IoT Cloud Remote).", "Keunggulan Utama:")
    add_bullet(" Ketergantungan tinggi pada pustaka resmi Arduino Cloud, akun gratis dibatasi 2 Things dan interval polling tertentu.", "Kelemahan:")

    add_p("4. Antares IoT (Telkom Indonesia)", heading_level=2)
    add_bullet(" Platform IoT enterprise lokal berstandar global oneM2M yang dikembangkan oleh Telkom Indonesia.", "Deskripsi & Fokus:")
    add_bullet(" HTTP RESTful, MQTT, dan CoAP.", "Protokol Komunikasi:")
    add_bullet(" Struktur hierarki oneM2M: Application -> Device (Node) -> Container (cnt) -> Content Instance (cin).", "Model Data:")
    add_bullet(" Server berada di Indonesia (latensi lokal sangat rendah), kepatuhan standar industri oneM2M, mendukung integrasi LoRaWAN dan NB-IoT.", "Keunggulan Utama:")
    add_bullet(" Format payload dan header request cukup kompleks (mengikuti spesifikasi oneM2M seperti X-M2M-Origin dan header Content-Type khusus).", "Kelemahan:")

    # --- TABEL RINGKASAN KOMPARASI ---
    add_p("Tabel Perbandingan Fitur:", heading_level=2)
    table_p = (
        "| Parameter | ThingSpeak | Adafruit IO | Arduino Cloud | Antares IoT |\n"
        "| :--- | :--- | :--- | :--- | :--- |\n"
        "| Protokol Utama | HTTP REST, MQTT | MQTT, HTTP REST | MQTT over TLS | HTTP, MQTT, CoAP (oneM2M) |\n"
        "| Kontrol Aktuator | Terbatas | Sangat Baik (Realtime) | Sangat Baik (Sync Variable) | Baik (Downlink via MQTT/HTTP) |\n"
        "| Visualisasi | Grafik MATLAB | Widget Lengkap | Dashboard Modern / Mobile | Dashboard Standar |\n"
        "| Latensi Server | Global (US) | Global (US) | Global (EU/US) | Lokal Indonesia (Telkom) |\n"
        "| Target Kasus | Data Logging & Riset | Prototyping Cepat | Smart Home / Maker | Enterprise & Smart City |"
    )
    add_p(table_p, size=9.5)

    # --- BAGIAN 2: TUTORIAL IMPLEMENTASI ESP32 ---
    add_p("B. Tutorial Implementasi Platform dengan ESP32", heading_level=1)
    add_p(
        "Pengujian dilakukan menggunakan mikrokontroler ESP32 Dev Module, sensor suhu & kelembaban DHT22 pada pin GPIO 4, "
        "serta modul relay / LED pada pin GPIO 5."
    )

    add_p("1. Tutorial Implementasi ThingSpeak", heading_level=2)
    add_bullet("Daftar akun di https://thingspeak.com lalu klik 'New Channel'.")
    add_bullet("Beri nama channel 'Monitoring Lingkungan', aktifkan Field 1 (Suhu) dan Field 2 (Kelembaban), lalu klik Save.")
    add_bullet("Buka tab 'API Keys', salin Write API Key untuk dimasukkan ke dalam program ESP32.")
    add_bullet("Di Arduino IDE, buka file 'tugas-4/thingspeak/thingspeak_esp32.ino', masukkan SSID, Password Wi-Fi, dan Write API Key.")
    add_bullet("Upload program ke ESP32. Buka Serial Monitor (baud rate 115200).")
    add_bullet("Verifikasi: Grafik pada dashboard ThingSpeak akan ter-update secara berkala (interval minimal 15 detik).")

    add_p("2. Tutorial Implementasi Adafruit IO", heading_level=2)
    add_bullet("Daftar akun di https://io.adafruit.com lalu masuk ke menu Feeds -> View All.")
    add_bullet("Buat 3 Feeds baru: 'suhu', 'kelembaban', dan 'saklar-relay'.")
    add_bullet("Masuk ke menu Dashboards, buat dashboard baru dan tambahkan widget Gauge (untuk suhu) serta Toggle Switch (untuk relay).")
    add_bullet("Klik tombol 'My Key' di pojok kanan atas, catat Username dan Active Key.")
    add_bullet("Buka kode 'tugas-4/adafruit_io/adafruit_io_esp32.ino', masukkan kredensial Wi-Fi dan Adafruit IO.")
    add_bullet("Upload kode. Uji kendali dua arah: ubah toggle switch di web Adafruit IO, maka relay pada ESP32 akan langsung bereaksi (ON/OFF).")

    add_p("3. Tutorial Implementasi Arduino IoT Cloud", heading_level=2)
    add_bullet("Buka https://create.arduino.cc/iot/ dan login.")
    add_bullet("Pada menu Devices, pilih 'Set up third party device', pilih ESP32, lalu unduh Device ID dan Secret Key.")
    add_bullet("Buat 'Thing' baru, tautkan ke device yang telah dibuat, lalu tambahkan Cloud Variables: 'temperature' (float, read-only) dan 'relaySwitch' (boolean, read-write).")
    add_bullet("Buka sketch editor dan sesuaikan dengan kode 'tugas-4/arduino_cloud/arduino_cloud_esp32.ino'.")
    add_bullet("Upload sketch dan pantau dashboard Arduino Cloud serta aplikasi smartphone Arduino IoT Remote.")

    add_p("4. Tutorial Implementasi Antares IoT (Telkom)", heading_level=2)
    add_bullet("Login ke portal https://antares.id dan buka menu Applications.")
    add_bullet("Buat aplikasi baru dengan nama 'TugasKuliahIoT', lalu di dalamnya buat device 'ESP32Node'.")
    add_bullet("Buka menu Akun / Profil untuk mendapatkan Access Key Antares.")
    add_bullet("Buka kode 'tugas-4/antares/antares_esp32.ino', masukkan accessKey, applicationName, dan deviceName.")
    add_bullet("Upload kode. ESP32 akan mengirimkan payload JSON Content Instance (cin) melalui HTTP POST dengan header oneM2M: X-M2M-Origin.")
    add_bullet("Verifikasi data di portal Antares: buka device 'ESP32Node', data JSON yang dikirim akan muncul secara realtime pada tab Data.")

    # --- BAGIAN 3: INOVASI EXTENSION MCP SERVER ---
    add_p("C. Inovasi & Pengembangan Ekstensi: Model Context Protocol (MCP) Server", heading_level=1)
    add_p(
        "Sebagai inovasi tingkat lanjut, dibangun sebuah MCP (Model Context Protocol) Server berbasis Python "
        "yang memungkinkan Artificial Intelligence (seperti Antigravity, Claude, atau Cursor) untuk melakukan "
        "pemantauan telemetri dan kendali aktuator secara otonom melalui bahasa alami (Natural Language)."
    )
    add_bullet("get_thingspeak_feeds: Memungkinkan AI memeriksa suhu/kelembaban terkini dari channel ThingSpeak.", "Tool 1:")
    add_bullet("set_adafruit_feed: Memungkinkan AI mengirim sinyal kendali saklar/relay secara langsung ke Adafruit IO.", "Tool 2:")
    add_bullet("get_antares_latest_data: Memungkinkan AI mengekstrak payload oneM2M dari perangkat Antares.", "Tool 3:")
    add_bullet("Menghilangkan gap antara antarmuka AI dan dunia fisik (Cyber-Physical System), mewujudkan ekosistem Smart IoT Agent.", "Dampak Arsitektur:")

    # --- BAGIAN 4: BUKTI PENGUJIAN EMPIRIS & VERIFIKASI LIVE ---
    add_p("D. Bukti Pengujian Empiris & Verifikasi Live Platform", heading_level=1)
    add_p(
        "Pengujian fungsional dan transmisi telemetri telah berhasil diverifikasi secara live pada ketiga platform IoT "
        "yang telah dikonfigurasi:"
    )
    add_bullet("Channel ID: 3564706 (tugas4) | Status: Terhubung (HTTP 200 OK) | Entry ID 1 & 2 berhasil dicatat dengan nilai suhu 28.5 °C dan 29.8 °C.", "1. ThingSpeak: ")
    add_bullet("User: AriqAzzki | Feeds dibuat: 'suhu' (28.7 °C), 'kelembaban' (63.5 %), dan 'saklar-relay' (Berhasil di-toggle ON -> OFF secara realtime via MCP).", "2. Adafruit IO: ")
    add_bullet("Application: tugasIOT4 | Device: ESP32Node | Port: HTTPS 8443 | Payload JSON cin (cin_NWQBhKCI17l0HMKHTVYIv4TeFAWPTMda) berhasil diunggah dan dibaca kembali secara valid.", "3. Antares IoT: ")

    # --- KESIMPULAN ---
    add_p("E. Kesimpulan", heading_level=1)
    add_p(
        "Keempat platform IoT memiliki keunggulan spesifik masing-masing: ThingSpeak sangat unggul untuk komputasi analitik "
        "dan riset data sensor; Adafruit IO adalah yang terbaik untuk prototyping responsif dan kontrol realtime; Arduino Cloud "
        "menyediakan ekosistem terpadu yang sangat ramah pengguna; dan Antares IoT menghadirkan solusi standar oneM2M industri "
        "dengan infrastruktur lokal berlatensi rendah. Penggunaan arsitektur modern seperti MCP Server semakin memperluas "
        "potensi integrasi IoT dengan sistem kecerdasan buatan masa depan."
    )

    doc.save(output_path)
    print(f"Laporan berhasil disimpan ke: {output_path}")

if __name__ == "__main__":
    nama = sys.argv[1] if len(sys.argv) > 1 else "Ariq Azzki"
    nim = sys.argv[2] if len(sys.argv) > 2 else "[NIM]"
    in_path = sys.argv[3] if len(sys.argv) > 3 else "Tugas 5 - Internet of Things - Review IoT Platform-UIW.docx"
    out_path = sys.argv[4] if len(sys.argv) > 4 else in_path
    fill_report(nama, nim, in_path, out_path)
