import time


def create_telemetry() -> dict:
    return {
        "device_id": "UAV-001",
        "timestamp": time.time(),
        "latitude": 49.82,
        "longitude": 19.04,
        "altitude": 125.4,
        "battery": 87,
        "status": "OK",
    }