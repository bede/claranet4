import asyncio
import json
import defopt

from claranet4.lib import get_nearest_reading, discover_a4s


def discover():
    a4_devices = asyncio.run(discover_a4s())
    a4_devices_subset = [
        {k: v for k, v in d.items() if k in {"address", "name", "rssi"}}
        for d in a4_devices
    ]
    print(json.dumps(a4_devices_subset, indent=4))


def nearest():
    print(json.dumps(get_nearest_reading().__dict__, indent=4))


def main():
    defopt.run(
        {
            "discover": discover,
            "nearest": nearest,
        },
        no_negated_flags=True,
        strict_kwonly=False,
        short={},
    )


if __name__ == "__main__":
    main()
