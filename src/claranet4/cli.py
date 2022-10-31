import json
import defopt

import claranet4.lib as lib


def dictify(obj):
    return obj.__dict__


def scan():
    """
    Show Bluetooth devices in the vicinity
    """
    devices = lib.scan()
    print(json.dumps(devices, default=dictify, indent=4))


def discover(*, substring: str = "Aranet4"):
    """
    Discover Aranet4 devices in the vicinity

    :arg substring: device name substring used to identify Aranet4s
    """
    ara4_devices = lib.discover_ara4s()
    print(json.dumps(ara4_devices, default=dictify, indent=4))


def read(address: str = ""):
    """
    Read current measurements from Aranet4 devices in the vicinity

    :arg address: target device address
    """
    print(json.dumps(lib.read(address), default=dictify, indent=4))


def main():
    defopt.run(
        {
            "scan": scan,
            "discover": discover,
            "read": read,
        },
        short={},
    )


if __name__ == "__main__":
    main()
