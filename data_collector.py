import random
from datetime import datetime

def get_api_data():
    devices = [
        # devices
        {"device": "Fan",             "voltage": 220, "current": 0.50, "api_power": 110.0},
        {"device": "AC",              "voltage": 220, "current": 5.20, "api_power": 1144.0},
        {"device": "TV",              "voltage": 220, "current": 1.00, "api_power": 220.0},
        {"device": "Fridge",          "voltage": 220, "current": 1.50, "api_power": 330.0},
        {"device": "Washing Machine", "voltage": 220, "current": 2.27, "api_power": 500.0},
        {"device": "Microwave",       "voltage": 220, "current": 4.55, "api_power": 1000.0},
        {"device": "Water Heater",    "voltage": 220, "current": 9.09, "api_power": 2000.0},
        # 4 individual LED bulbs — each 10W
        {"device": "LED Bulb 1",      "voltage": 220, "current": 0.045, "api_power": 10.0},
        {"device": "LED Bulb 2",      "voltage": 220, "current": 0.045, "api_power": 10.0},
        {"device": "LED Bulb 3",      "voltage": 220, "current": 0.045, "api_power": 10.0},
        {"device": "LED Bulb 4",      "voltage": 220, "current": 0.045, "api_power": 10.0},
    ]

    for d in devices:
        d["voltage"] += random.uniform(-3, 3)
        d["current"] += random.uniform(-0.002, 0.002)
        d["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return devices
