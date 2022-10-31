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
INFO: Found 9 device(s)
INFO: Found 1 Aranet4 device(s)
[
    {
        "address": "390F544C-F0FF-F8BE-3A3A-BB1219AA2145",
        "name": "Aranet4 1D6BA",
        "rssi": -71
    }
]
% claranet4 read 390F544C-F0FF-F8BE-3A3A-BB1219AA2145
INFO: Selected Aranet4 1D6BA (-74dBm)
{
    "name": "Aranet4 1D6BA",
    "address": "390F544C-F0FF-F8BE-3A3A-BB1219AA2145",
    "rssi": -74,
    "co2": 946,
    "temperature": 17.6,
    "pressure": 1002.1,
    "humidity": 73.4
}
% claranet4 read
INFO: Found 9 device(s)
INFO: Found 1 Aranet4 device(s)
INFO: Selected Aranet4 1D6BA (-74dBm)
{
    "name": "Aranet4 1D6BA",
    "address": "390F544C-F0FF-F8BE-3A3A-BB1219AA2145",
    "rssi": -74,
    "co2": 946,
    "temperature": 17.6,
    "pressure": 1002.1,
    "humidity": 73.4
}
```
