import asyncio
from dataclasses import dataclass
import logging
import sys
from bleak import BleakScanner, BleakClient


class DeviceError(RuntimeError):
    pass


logging.basicConfig(
    level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stderr
)


@dataclass
class Device:
    address: str
    name: str
    rssi: int


class Reading:
    def __init__(self, device: Device, response: bytearray):
        self.name: str = device.name
        self.address: str = device.address
        self.rssi: int = device.rssi
        self.co2: int = le16(response)
        self.temperature: float = round(le16(response, 2) / 20, 1)
        self.pressure: float = round(le16(response, 4) / 10, 1)
        self.humidity: float = round(le16(response, 5) / 255, 1)


def le16(data: bytearray, start: int = 0) -> int:
    """Read long integer from specified offset of bytearray"""
    raw = bytearray(data)
    return raw[start] + (raw[start + 1] << 8)


async def discover() -> list[Device]:
    """Return list of Devices sorted by descending RSSI dBm"""
    devices = [
        Device(address=d.address, name=str(d.name), rssi=d.rssi)
        for d in await BleakScanner.discover()
    ]
    logging.info(f"Found {len(devices)} device(s)")
    return sorted(devices, key=lambda d: d.rssi, reverse=True)


async def request_measurements(address: str) -> bytearray:
    """Request measurements bytearray for target address"""
    UUID_CURRENT_MEASUREMENTS_SIMPLE = "f0cd1503-95da-4f4b-9ac8-aa55d312af0c"
    async with BleakClient(address) as client:
        return await client.read_gatt_char(UUID_CURRENT_MEASUREMENTS_SIMPLE)


def scan() -> list[Device]:
    """Show Bluetooth devices in the vicinity"""
    return asyncio.run(discover())


def discover_ara4s(substring: str = "Aranet4") -> list[Device]:
    """Find Aranet4s in the vicinity"""
    devices = scan()
    ara4_devices = [d for d in devices if substring in d.name]
    logging.info(f"Found {len(ara4_devices)} Aranet4 device(s)")
    return ara4_devices


def find_device(address) -> Device:
    """Find Device by address"""
    r = asyncio.run(BleakScanner.find_device_by_address(address))
    if r:
        return Device(address=r.address, name=str(r.name), rssi=r.rssi)
    else:
        raise DeviceError("Error finding device")


def read(address: str = "") -> Reading:
    if address:
        device = find_device(address)
    else:
        ara4_devices = discover_ara4s()
        device = ara4_devices[0]
    logging.info(f"Selected {device.name} ({device.rssi}dBm)")
    measurements = asyncio.run(request_measurements(device.address))
    return Reading(device, measurements)
