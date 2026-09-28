from device.telemetry import create_telemetry


def test_telemetry_contains_correct_device_id():
    telemetry = create_telemetry()

    assert telemetry["device_id"] == "UAV-001"

def test_battery_level_is_valid():
    telemetry = create_telemetry()

    assert 0 <= telemetry["battery"] <= 100


def test_coordinates_are_valid():
    telemetry = create_telemetry()

    assert -90 <= telemetry["latitude"] <= 90
    assert -180 <= telemetry["longitude"] <= 180