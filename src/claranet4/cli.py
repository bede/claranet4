import json
import defopt
import logging

from typing import Literal

import claranet4.lib as lib


def dictify(obj):
    return obj.__dict__


def scan(*, timeout: int = 5):
    """
    Show nearby Bluetooth devices

    :arg timeout: listening timeout in seconds
    """
    devices = lib.scan(timeout=timeout)
    print(json.dumps(devices, default=dictify, indent=4))


def discover(*, substring: str = "Aranet4", timeout: int = 5):
    """
    Discover nearby Aranet4 devices

    :arg substring: device name substring used to identify Aranet4s
    :arg timeout: listening timeout in seconds
    """
    ara4_devices = lib.discover_ara4s()
    print(json.dumps(ara4_devices, default=dictify, indent=4))


def read(
    address: str = "",
    *,
    field: Literal["co2", "temperature", "pressure", "humidity", ""] = "",
    quiet: bool = False,
    timeout: int = 5,
):
    """
    Request latest measurements from a nearby Aranet4 device

    :arg address: target device address
    :arg field: return a specified field value only
    :arg quiet: suppress notices on stderr
    :arg timeout: listening timeout in seconds
    """
    if quiet:
        logging.getLogger().setLevel("WARNING")
    reading = lib.read(address, timeout=timeout)
    if field:
        print(getattr(reading, field))
    else:
        print(json.dumps(reading, default=dictify, indent=4))


def main():
    defopt.run(
        {
            "scan": scan,
            "discover": discover,
            "read": read,
        },
        short={},
        no_negated_flags=True,
    )


if __name__ == "__main__":
    main()
