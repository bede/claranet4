# Claranet4

Ultra-minimal (i.e. incomplete) Python & CLI client for collecting current readings from Aranet4 Bluetooth sensors. There are two relatively mature existing Python client libraries, but I couldn't get either to work (MacOS 12.6). This  client uses Bleak and should work across platforms.

## Install

Python >= 3.10

```
git clone https://github.com/bede/claranet4.git
pip install ./claranet4
```

## Usage
```
% claranet4 discover
INFO: Found 63 device(s)
INFO: Found 1 Aranet4 device(s)
[
    {
        "address": "390F544C-F0FF-F8BE-3A3A-BB1219AA2145",
        "name": "Aranet4 1D6BA",
        "rssi": -64
    }
]
% claranet4 nearest
INFO: Found 67 device(s)
INFO: Found 1 Aranet4 device(s)
INFO: Selected Aranet4 1D6BA (-69dBm)
{
    "co2": 891,
    "temperature": 22.4,
    "pressure": 1005.2,
    "humidity": 63.4
}
```
