import asyncio
import logging
import sys
from bleak import BleakScanner, BleakClient


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stderr)


def le16(data, start=0):
    """
    Read value from byte array as a long integer

    :param bytearray data:  Array of bytes to read from
    :param int start:  Offset to start response at
    :return int:  An integer, read from the first two bytes at the offset.
    """
    raw = bytearray(data)
    return raw[start] + (raw[start + 1] << 8)


class Reading:
    """Test"""
    def __init__(self, response):
        self.co2 = le16(response)
        self.temperature = round(le16(response, 2)/20, 1)
        self.pressure = round(le16(response, 4) / 10, 1)
        self.humidity = round(le16(response, 5) / 255, 1)


async def discover():
    devices = [d.__dict__ for d in await BleakScanner.discover()]
    logging.info(f"Found {len(devices)} device(s)")
    return devices


async def discover_a4s(sort_by_rssi=True):
    A4_STRING = "Aranet4"
    a4_devices = [d for d in await discover() if d["name"] and A4_STRING in d["name"]]
    logging.info(f"Found {len(a4_devices)} Aranet4 device(s)")
    if sort_by_rssi:
        a4_devices = sorted(a4_devices, key=lambda d: d['rssi'], reverse=True)
    return a4_devices


async def get_response(address):
    UUID_CURRENT_MEASUREMENTS_SIMPLE = "f0cd1503-95da-4f4b-9ac8-aa55d312af0c"
    async with BleakClient(address) as client:
        return await client.read_gatt_char(UUID_CURRENT_MEASUREMENTS_SIMPLE)


async def get_reading(address):
    return Reading(await get_response(address))


def get_nearest_reading():
    a4_devices = asyncio.run(discover_a4s())
    this_device = a4_devices[0]
    logging.info(f"Selected {this_device['name']} ({this_device['rssi']}dBm)")
    reading = asyncio.run(get_reading(this_device["address"]))
    return reading


def main():
    get_nearest_reading()
