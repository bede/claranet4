# Claranet4

Barebones (i.e. incomplete) Python & CLI client for collecting current readings from Aranet4 Bluetooth sensors.

## Install

Python >= 3.10

```
pip install ./
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