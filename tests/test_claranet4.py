import asyncio
import pytest
import subprocess

from claranet4.lib import Device, Reading


def run(cmd, cwd="./"):  # Helper for CLI testing
    return subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)


@pytest.fixture
def device():
    return Device(
        address="390F544C-F0FF-F8BE-3A3A-BB1219AA2145", name="Aranet4 1D6BA", rssi=-75
    )


@pytest.fixture
def measurements():
    return b"\xf9\x03_\x01+'I_\x02"


def test_reading(device, measurements):
    assert Reading(device, measurements).__dict__ == {
        "name": "Aranet4 1D6BA",
        "address": "390F544C-F0FF-F8BE-3A3A-BB1219AA2145",
        "rssi": -75,
        "co2": 1017,
        "temperature": 17.6,
        "pressure": 1002.7,
        "humidity": 73.4,
    }


def test_cli_version():
    run("claranet4 --version")
