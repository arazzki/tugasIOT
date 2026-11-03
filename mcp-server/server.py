#!/usr/bin/env python3
"""
IoT Platforms MCP Server (Model Context Protocol)
Mata Kuliah: Internet of Things (ITH3V3) - Tugas 4

Server ini menyediakan antarmuka bagi AI Assistant (seperti Antigravity, Claude, Cursor)
untuk berinteraksi langsung dengan platform IoT:
- ThingSpeak: Membaca & mengirim feed data sensor
- Adafruit IO: Membaca telemetri & mengontrol aktuator/relay
- Antares IoT: Membaca & mengirim data payload oneM2M
"""

import os
import json
import httpx
from dotenv import load_dotenv

# Kompatibilitas SDK MCP v2 (MCPServer) dan v1 (FastMCP)
try:
    from mcp.server.mcpserver import MCPServer
    app = MCPServer(
        name="iot-platform-server",
        instructions="IoT Platform MCP Server for ThingSpeak, Adafruit IO, and Antares"
    )
except ImportError:
    from mcp.server.fastmcp import FastMCP
    app = FastMCP(
        name="iot-platform-server",
        instructions="IoT Platform MCP Server for ThingSpeak, Adafruit IO, and Antares"
    )

# Muat variabel environment dari .env di direktori yang sama atau root
env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    load_dotenv()

# ==============================================================================
# 1. ThingSpeak Tools
# ==============================================================================
@app.tool()
async def get_thingspeak_feeds(
    channel_id: str | None = None,
    read_key: str | None = None,
    results: int = 5
) -> str:
    """Mengambil riwayat data feed telemetri terbaru dari Channel ThingSpeak.
    
    Args:
        channel_id: ID Channel ThingSpeak (opsional jika sudah diatur di .env).
        read_key: Read API Key ThingSpeak (opsional jika channel bersifat publik atau ada di .env).
        results: Jumlah data titik terakhir yang ingin diambil (default: 5).
    """
    cid = channel_id or os.getenv("THINGSPEAK_CHANNEL_ID")
    rkey = read_key or os.getenv("THINGSPEAK_READ_KEY", "")

    if not cid:
        return "Error: Channel ID belum diatur. Masukkan channel_id atau isi di file .env."

    url = f"https://api.thingspeak.com/channels/{cid}/feeds.json?results={results}"
    if rkey:
        url += f"&api_key={rkey}"

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, timeout=10.0)
            resp.raise_for_status()
            data = resp.json()
            channel_info = data.get("channel", {})
            feeds = data.get("feeds", [])
            return json.dumps({
                "status": "success",
                "channel_name": channel_info.get("name"),
                "description": channel_info.get("description"),
                "feeds_count": len(feeds),
                "feeds": feeds
            }, indent=2)
        except Exception as e:
            return f"Error saat mengakses ThingSpeak: {str(e)}"


@app.tool()
async def send_thingspeak_data(
    field1: float | None = None,
    field2: float | None = None,
    field3: float | None = None,
    write_key: str | None = None
) -> str:
    """Mengirim data telemetri (suhu, kelembaban, dll.) ke Channel ThingSpeak via REST API.
    
    Args:
        field1: Nilai untuk Field 1 (misal: Suhu).
        field2: Nilai untuk Field 2 (misal: Kelembaban).
        field3: Nilai untuk Field 3.
        write_key: Write API Key ThingSpeak (opsional jika sudah diatur di .env).
    """
    wkey = write_key or os.getenv("THINGSPEAK_WRITE_KEY")
    if not wkey:
        return "Error: Write API Key belum diatur. Masukkan write_key atau isi di file .env."

    params = {"api_key": wkey}
    if field1 is not None:
        params["field1"] = str(field1)
    if field2 is not None:
        params["field2"] = str(field2)
    if field3 is not None:
        params["field3"] = str(field3)

    url = "https://api.thingspeak.com/update"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, params=params, timeout=10.0)
            resp.raise_for_status()
            entry_id = resp.text.strip()
            if entry_id == "0":
                return "Peringatan: ThingSpeak menolak update (rate limit 15 detik belum tercapai)."
            return f"Sukses mengirim data ke ThingSpeak! Entry ID baru: {entry_id}"
        except Exception as e:
            return f"Error saat mengirim ke ThingSpeak: {str(e)}"


# ==============================================================================
# 2. Adafruit IO Tools
# ==============================================================================
@app.tool()
async def get_adafruit_feed(
    feed_key: str,
    username: str | None = None,
    aio_key: str | None = None
) -> str:
    """Membaca nilai data terakhir dari sebuah Feed di Adafruit IO.
    
    Args:
        feed_key: Key/nama feed (contoh: 'suhu', 'kelembaban', 'saklar-relay').
        username: Username Adafruit IO (opsional jika sudah di .env).
        aio_key: Active AIO Key Adafruit IO (opsional jika sudah di .env).
    """
    user = username or os.getenv("ADAFRUIT_IO_USERNAME")
    key = aio_key or os.getenv("ADAFRUIT_IO_KEY")

    if not user or not key:
        return "Error: Username atau AIO Key Adafruit IO belum diatur."

    url = f"https://io.adafruit.com/api/v2/{user}/feeds/{feed_key}/data/last"
    headers = {"X-AIO-Key": key}

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, headers=headers, timeout=10.0)
            resp.raise_for_status()
            data = resp.json()
            return json.dumps({
                "status": "success",
                "feed_key": feed_key,
                "value": data.get("value"),
                "created_at": data.get("created_at")
            }, indent=2)
        except Exception as e:
            return f"Error saat mengakses Adafruit IO: {str(e)}"


@app.tool()
async def set_adafruit_feed(
    feed_key: str,
    value: str,
    username: str | None = None,
    aio_key: str | None = None
) -> str:
    """Mengirim nilai baru ke feed Adafruit IO (misalnya untuk mengontrol saklar/relay: 'ON' / 'OFF' atau angka).
    
    Args:
        feed_key: Key/nama feed tujuan (misal: 'saklar-relay').
        value: Nilai yang ingin dikirimkan (misal: 'ON', 'OFF', '1', '0', atau angka desimal).
        username: Username Adafruit IO.
        aio_key: AIO Key Adafruit IO.
    """
    user = username or os.getenv("ADAFRUIT_IO_USERNAME")
    key = aio_key or os.getenv("ADAFRUIT_IO_KEY")

    if not user or not key:
        return "Error: Username atau AIO Key Adafruit IO belum diatur."

    url = f"https://io.adafruit.com/api/v2/{user}/feeds/{feed_key}/data"
    headers = {
        "X-AIO-Key": key,
        "Content-Type": "application/json"
    }
    payload = {"value": value}

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, headers=headers, json=payload, timeout=10.0)
            resp.raise_for_status()
            data = resp.json()
            return f"Sukses memperbarui Feed '{feed_key}' dengan nilai '{value}'. Data ID: {data.get('id')}"
        except Exception as e:
            return f"Error saat mengirim ke Adafruit IO: {str(e)}"


# ==============================================================================
# 3. Antares IoT Tools
# ==============================================================================
@app.tool()
async def get_antares_latest_data(
    application_name: str | None = None,
    device_name: str | None = None,
    access_key: str | None = None
) -> str:
    """Mengambil data Content Instance (cin) terbaru dari platform Antares oneM2M.
    
    Args:
        application_name: Nama aplikasi di Antares (opsional jika sudah di .env).
        device_name: Nama perangkat di Antares (opsional jika sudah di .env).
        access_key: Access Key akun Antares (opsional jika sudah di .env).
    """
    app_name = application_name or os.getenv("ANTARES_APPLICATION_NAME")
    dev_name = device_name or os.getenv("ANTARES_DEVICE_NAME")
    key = access_key or os.getenv("ANTARES_ACCESS_KEY")

    if not app_name or not dev_name or not key:
        return "Error: Application Name, Device Name, atau Access Key Antares belum lengkap."

    url = f"http://platform.antares.id:8080/~/antares-cse/antares-id/{app_name}/{dev_name}/la"
    headers = {
        "X-M2M-Origin": key,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, headers=headers, timeout=10.0)
            resp.raise_for_status()
            data = resp.json()
            cin = data.get("m2m:cin", {})
            content_str = cin.get("con", "")
            try:
                parsed_con = json.loads(content_str)
            except Exception:
                parsed_con = content_str

            return json.dumps({
                "status": "success",
                "creation_time": cin.get("ct"),
                "resource_name": cin.get("rn"),
                "content": parsed_con
            }, indent=2)
        except Exception as e:
            return f"Error saat mengambil data dari Antares: {str(e)}"


@app.tool()
async def send_antares_data(
    data: dict | str,
    application_name: str | None = None,
    device_name: str | None = None,
    access_key: str | None = None
) -> str:
    """Mengirimkan data payload Content Instance ke Antares oneM2M.
    
    Args:
        data: Data yang ingin dikirim (dictionary JSON atau string).
        application_name: Nama aplikasi di Antares.
        device_name: Nama perangkat di Antares.
        access_key: Access Key Antares.
    """
    app_name = application_name or os.getenv("ANTARES_APPLICATION_NAME")
    dev_name = device_name or os.getenv("ANTARES_DEVICE_NAME")
    key = access_key or os.getenv("ANTARES_ACCESS_KEY")

    if not app_name or not dev_name or not key:
        return "Error: Application Name, Device Name, atau Access Key Antares belum lengkap."

    url = f"http://platform.antares.id:8080/~/antares-cse/antares-id/{app_name}/{dev_name}"
    headers = {
        "X-M2M-Origin": key,
        "Content-Type": "application/json;ty=4",
        "Accept": "application/json"
    }

    con_str = json.dumps(data) if isinstance(data, dict) else str(data)
    payload = {"m2m:cin": {"con": con_str}}

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, headers=headers, json=payload, timeout=10.0)
            resp.raise_for_status()
            res_data = resp.json()
            cin = res_data.get("m2m:cin", {})
            return f"Sukses mengirim data ke Antares! Resource Name (rn): {cin.get('rn')}"
        except Exception as e:
            return f"Error saat mengirim data ke Antares: {str(e)}"


if __name__ == "__main__":
    # Jalankan MCP Server melalui stdio transport
    app.run(transport="stdio")
