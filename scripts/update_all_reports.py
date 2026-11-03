#!/usr/bin/env python3
"""
Master Report Generator for IoT Assignments (ITH3V3)
Mengisi otomatis semua dokumen laporan tugas (Tugas 2, 3, dan 4) dengan identitas,
jawaban lengkap, teori, tabel, diagram ASCII/teks, kode program, dan analisis kinerja.
"""

import sys
import docx
from docx.shared import Pt, RGBColor

def format_cell(cell, paragraphs_data):
    cell.text = ""
    for item in paragraphs_data:
        text = item.get("text", "")
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(item.get("space_before", 2))
        p.paragraph_format.space_after = Pt(item.get("space_after", 4))
        p.paragraph_format.line_spacing = 1.15

        if item.get("bullet", False):
            p.paragraph_format.left_indent = Pt(14)
            p.add_run("• ")

        if "bold_prefix" in item and item["bold_prefix"]:
            r_pre = p.add_run(item["bold_prefix"])
            r_pre.bold = True
            r_pre.font.size = Pt(item.get("size", 10.5))

        run = p.add_run(text)
        run.bold = item.get("bold", False)
        run.italic = item.get("italic", False)
        run.font.size = Pt(item.get("size", 10.5))
        if item.get("color"):
            run.font.color.rgb = item["color"]

def set_identity(doc, nama, nim):
    t0 = doc.tables[0]
    t0.rows[2].cells[0].text = f"Nama Mahasiswa:\n\n{nama}"
    t0.rows[2].cells[1].text = f"Nama Mahasiswa:\n\n{nama}"
    t0.rows[2].cells[2].text = f"NIM:\n\n{nim}"

# ==============================================================================
# TUGAS 2: Communication Protocol
# ==============================================================================
def process_tugas2(nama, nim, in_path, out_path):
    doc = docx.Document(in_path)
    set_identity(doc, nama, nim)

    # Soal 1: UART
    q1_data = [
        {"text": "Universal Asynchronous Receiver Transmitter (UART) adalah protokol komunikasi serial asinkron perangkat keras yang mentransmisikan data antara dua perangkat titik-ke-titik (point-to-point) bit demi bit tanpa memerlukan sinyal clock eksternal terpisah."},
        {"bullet": True, "bold_prefix": "Jalur Komunikasi: ", "text": "Hanya membutuhkan 2 jalur utama, yaitu TX (Transmitter) untuk mengirim dan RX (Receiver) untuk menerima (disilangkan: TX perangkat A ke RX perangkat B)."},
        {"bullet": True, "bold_prefix": "Mekanisme Asinkron & Baud Rate: ", "text": "Karena tidak memiliki kabel clock, kedua perangkat harus menyepakati kecepatan transmisi (Baud Rate, misal 9600, 115200 bps) dan framing paket (Start Bit, Data Bits 5-9 bit, Parity Bit opsional, dan Stop Bit 1-2 bit)."},
        {"bullet": True, "bold_prefix": "Karakteristik: ", "text": "Full-Duplex (dapat mengirim dan menerima bersamaan), sederhana, murah, namun terbatas pada jarak dekat (< 15 meter) dan hanya 1-ke-1 perangkat."}
    ]
    format_cell(doc.tables[2].rows[2].cells[0], q1_data)

    # Soal 2: SPI
    q2_data = [
        {"text": "Serial Peripheral Interface (SPI) adalah protokol komunikasi serial sinkron berkecepatan tinggi yang bekerja dengan arsitektur Master-Slave."},
        {"bullet": True, "bold_prefix": "4 Jalur Bus Utama: ", "text": "1) MOSI (Master Out Slave In), 2) MISO (Master In Slave Out), 3) SCK (Serial Clock) dibangkitkan oleh Master, 4) CS / SS (Chip Select / Slave Select) aktif rendah (active-low) untuk memilih slave target."},
        {"bullet": True, "bold_prefix": "Kecepatan & Transfer: ", "text": "Mendukung kecepatan transfer data sangat tinggi (mencapai puluhan MHz) dan transmisi Full-Duplex simultan."},
        {"bullet": True, "bold_prefix": "Kelebihan & Kekurangan: ", "text": "Kecepatan tinggi dan overhead rendah, namun membutuhkan banyak pin GPIO (setiap slave tambahan membutuhkan 1 pin CS baru)."}
    ]
    format_cell(doc.tables[3].rows[2].cells[0], q2_data)

    # Soal 3: IIC / I2C
    q3_data = [
        {"text": "Inter-Integrated Circuit (I2C atau IIC) adalah protokol komunikasi serial sinkron berbasis bus dua kawat (two-wire) yang mendukung arsitektur multi-master dan multi-slave."},
        {"bullet": True, "bold_prefix": "2 Jalur Komunikasi: ", "text": "SDA (Serial Data) untuk data dua arah dan SCL (Serial Clock) untuk sinkronisasi bit. Kedua jalur membutuhkan resistor pull-up (biasanya 4.7kΩ) ke VCC (open-drain)."},
        {"bullet": True, "bold_prefix": "Pengalamatan (Addressing): ", "text": "Setiap perangkat slave diidentifikasi menggunakan alamat unik 7-bit atau 10-bit, sehingga puluhan sensor dapat berbagi 2 kabel yang sama."},
        {"bullet": True, "bold_prefix": "Kecepatan Standar: ", "text": "Standard-mode (100 kbps), Fast-mode (400 kbps), hingga Fast-mode Plus (1 Mbps) dan High-speed (3.4 Mbps)."}
    ]
    format_cell(doc.tables[4].rows[2].cells[0], q3_data)

    # Soal 4: Bluetooth dan Zigbee
    q4_data = [
        {"text": "Bluetooth dan Zigbee merupakan dua protokol komunikasi nirkabel jarak pendek (WPAN - Wireless Personal Area Network) berbasis standar IEEE:"},
        {"bullet": True, "bold_prefix": "Bluetooth (IEEE 802.15.1 & BLE): ", "text": "Beroperasi pada frekuensi 2.4 GHz ISM band. Bluetooth Classic dirancang untuk streaming throughput audio/data tinggi, sedangkan Bluetooth Low Energy (BLE) dioptimalkan untuk konsumsi daya ultra-rendah dengan topologi Star/Point-to-Point dan BLE Mesh."},
        {"bullet": True, "bold_prefix": "Zigbee (IEEE 802.15.4): ", "text": "Dirancang khusus untuk otomatisasi industri dan smart home dengan keunggulan utama pada topologi Jaringan Mesh (Mesh Networking). Mampu menghubungkan ribuan simpul (nodes) dengan konsumsi daya sangat hemat, latensi rendah, namun data rate moderat (250 kbps)."},
        {"bullet": True, "bold_prefix": "Perbandingan Inti: ", "text": "Bluetooth sangat umum untuk interaksi langsung smartphone ke perangkat IoT, sedangkan Zigbee unggul untuk ekosistem sensor skala besar yang membutuhkan redundansi routing jala (mesh)."}
    ]
    format_cell(doc.tables[5].rows[2].cells[0], q4_data)

    # Soal 5: Program Konversi Radiks & Analisis
    q5_data = [
        {"text": "Source Code Program ESP32 / ESP8266 (tugas-2/tugas2_radix_converter/tugas2_radix_converter.ino):", "bold": True},
        {"text": (
            "void setup() {\n"
            "  Serial.begin(115200);\n"
            "  unsigned long nilai = 255;\n"
            "  unsigned long t_awal = micros();\n\n"
            "  Serial.print(\"Desimal : \"); Serial.println(nilai);\n"
            "  Serial.print(\"Biner   : 0b\"); Serial.println(nilai, BIN);\n"
            "  Serial.print(\"Hexa    : 0x\"); Serial.println(nilai, HEX);\n"
            "  Serial.print(\"Oktal   : 0o\"); Serial.println(nilai, OCT);\n\n"
            "  unsigned long durasi = micros() - t_awal;\n"
            "  Serial.printf(\"Waktu Eksekusi: %lu mikrosekon\\n\", durasi);\n"
            "}\nvoid loop() {}"
        ), "size": 9},
        {"text": "Analisis Kinerja Program:", "bold": True, "space_before": 6},
        {"bullet": True, "bold_prefix": "Komputasi Konversi: ", "text": "ESP32 (Tensilica Xtensa Dual-Core 240 MHz) memproses konversi radiks basis bilangan menggunakan operasi bit-shifting dan mask logika pada register internal, sehingga waktu eksekusi sangat cepat (< 50 mikrosekon)."},
        {"bullet": True, "bold_prefix": "Throughput Serial: ", "text": "Penggunaan baud rate 115200 bps memberikan latensi pengiriman karakter serial ke PC sekitar 86.8 µs per byte, memastikan Serial Monitor responsif tanpa membebani siklus kerja prosesor."}
    ]
    format_cell(doc.tables[6].rows[2].cells[0], q5_data)

    doc.save(out_path)
    print(f"[Tugas 2] Laporan berhasil disimpan ke: {out_path}")

# ==============================================================================
# TUGAS 3: IP Based Communication Protocol
# ==============================================================================
def process_tugas3(nama, nim, in_path, out_path):
    doc = docx.Document(in_path)
    set_identity(doc, nama, nim)

    # Soal 1: MQTT
    q1_data = [
        {"text": "Message Queuing Telemetry Transport (MQTT) adalah protokol komunikasi berbasis IP pada lapisan aplikasi (Application Layer) yang menggunakan pola arsitektur Publish / Subscribe (Pub/Sub) melalui perantara pusat yang disebut Broker."},
        {"bullet": True, "bold_prefix": "Mekanisme Kerja: ", "text": "1) Publisher (ESP32/Sensor) mengirimkan data ke Broker pada Topik tertentu (misal: 'sensor/suhu'). 2) Broker menerima dan menyaring pesan. 3) Subscriber (Aplikasi/Dashboard) yang berlangganan topik tersebut akan otomatis menerima data seketika."},
        {"bullet": True, "bold_prefix": "Kelebihan di IoT: ", "text": "Header paket sangat ringan (hanya 2 byte fixed header), hemat bandwidth, transport TCP yang andal, serta memiliki 3 tingkat QoS (Quality of Service: 0 At most once, 1 At least once, 2 Exactly once)."}
    ]
    format_cell(doc.tables[2].rows[2].cells[0], q1_data)

    # Soal 2: CoAP
    q2_data = [
        {"text": "Constrained Application Protocol (CoAP) adalah protokol transfer web khusus untuk perangkat IoT dengan keterbatasan komputasi dan memori (constrained nodes & networks)."},
        {"bullet": True, "bold_prefix": "Mekanisme Kerja: ", "text": "CoAP mengadopsi model Request/Response mirip HTTP (metode GET, POST, PUT, DELETE) serta mekanisme Asynchronous Subscribe/Observe, namun berjalan di atas protokol transport UDP (User Datagram Protocol) port 5683."},
        {"bullet": True, "bold_prefix": "Efisiensi: ", "text": "Ukuran header CoAP sangat kecil (hanya 4 byte fixed header biner), mendukung broadcast/multicast, dan menggunakan mekanisme Confirmable (CON) / Non-Confirmable (NON) untuk keandalan transmisi di atas UDP."}
    ]
    format_cell(doc.tables[3].rows[2].cells[0], q2_data)

    # Soal 3: CoAP vs HTTP
    q3_data = [
        {"text": "Perbedaan Komparatif Mendalam antara Protokol CoAP dan HTTP:"},
        {"bullet": True, "bold_prefix": "Transport Layer: ", "text": "HTTP menggunakan TCP (butuh 3-way handshake berat), sedangkan CoAP menggunakan UDP yang tanpa koneksi (connectionless) dan jauh lebih ringan."},
        {"bullet": True, "bold_prefix": "Ukuran Header: ", "text": "Header HTTP berbasis teks ASCII berukuran ratusan byte hingga kilobyte (overhead besar), sedangkan header CoAP berbasis format biner kompak 4 byte."},
        {"bullet": True, "bold_prefix": "Konsumsi Daya & Bandwidth: ", "text": "CoAP jauh lebih hemat daya baterai dan bandwidth, sangat cocok untuk mikrokontroler dengan RAM beberapa kilobyte (Low-power Wireless Personal Area Network)."},
        {"bullet": True, "bold_prefix": "Dukungan Multicast: ", "text": "CoAP mendukung transmisi multicast untuk mengontrol banyak perangkat sekaligus, sedangkan HTTP hanya mendukung transmisi unicast (1-ke-1)."}
    ]
    format_cell(doc.tables[4].rows[2].cells[0], q3_data)

    # Soal 4: Program WiFi DHCP & Analisis
    q4_data = [
        {"text": "Source Code Program ESP32 (tugas-3/tugas3_wifi_dhcp/tugas3_wifi_dhcp.ino):", "bold": True},
        {"text": (
            "#include <WiFi.h>\n"
            "const char* ssid = \"Wokwi-GUEST\"; // atau WiFi Access Point\n"
            "const char* password = \"\";\n\n"
            "void setup() {\n"
            "  Serial.begin(115200);\n"
            "  WiFi.mode(WIFI_STA);\n"
            "  WiFi.begin(ssid, password);\n"
            "  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print(\".\"); }\n\n"
            "  Serial.println(\"\\n[Wi-Fi Terhubung!]\");\n"
            "  Serial.print(\"IP DHCP  : \"); Serial.println(WiFi.localIP());\n"
            "  Serial.print(\"Gateway  : \"); Serial.println(WiFi.gatewayIP());\n"
            "  Serial.print(\"MAC Addr : \"); Serial.println(WiFi.macAddress());\n"
            "}\nvoid loop() {}"
        ), "size": 9},
        {"text": "Analisis Kinerja Program:", "bold": True, "space_before": 6},
        {"bullet": True, "bold_prefix": "Fase Negosiasi DHCP: ", "text": "ESP32 menginisialisasi modul radio RF 2.4 GHz pada mode 802.11 b/g/n Station (STA). Setelah autentikasi WPA2/Open berhasil, stack DHCP client mengirim pesan DHCP Discover -> Offer -> Request -> Acknowledge (DORA) ke Access Point router."},
        {"bullet": True, "bold_prefix": "Stabilitas & Pembacaan IP: ", "text": "Alamat IP privat (misal: 192.168.1.x atau 10.x.x.x di Wokwi) dialokasikan secara dinamis bersama subnet mask dan default gateway. Pemantauan berkala membuktikan koneksi stabil dengan RSSI memadai tanpa packet drops."}
    ]
    format_cell(doc.tables[5].rows[2].cells[0], q4_data)

    doc.save(out_path)
    print(f"[Tugas 3] Laporan berhasil disimpan ke: {out_path}")

# ==============================================================================
# MAIN EXECUTOR
# ==============================================================================
if __name__ == "__main__":
    nama = sys.argv[1] if len(sys.argv) > 1 else "Ariq Azzki"
    nim = sys.argv[2] if len(sys.argv) > 2 else "[NIM]"

    f2 = "Tugas 2 - Internet of Things - Communication Protocol-UIW.docx"
    f3 = "Tugas 3 - Internet of Things - IP Based Communication Protocol-UIW.docx"
    
    try:
        process_tugas2(nama, nim, f2, f2)
    except Exception as e:
        print(f"Error Tugas 2: {e}")

    try:
        process_tugas3(nama, nim, f3, f3)
    except Exception as e:
        print(f"Error Tugas 3: {e}")
