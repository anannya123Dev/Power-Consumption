import random, time

def get_api_data():
    return [
        {"device": "Fan",    "voltage": 220 + random.uniform(-5, 5), "current": 0.5 + random.uniform(-0.05, 0.05), "api_power": 110.0},
        {"device": "AC",     "voltage": 220 + random.uniform(-5, 5), "current": 5.2 + random.uniform(-0.1, 0.1),  "api_power": 1144.0},
        {"device": "TV",     "voltage": 220 + random.uniform(-5, 5), "current": 1.0 + random.uniform(-0.05, 0.05),"api_power": 220.0},
        {"device": "Fridge", "voltage": 220 + random.uniform(-5, 5), "current": 1.5 + random.uniform(-0.05, 0.05),"api_power": 330.0},
    ]