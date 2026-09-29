from framework.udp_receiver import receive_telemetry


def test_telemetry_is_received_over_udp(
    simulator_process,
):
    telemetry = receive_telemetry(
        timeout=3.0
    )

    assert telemetry["device_id"] == "UAV-001"

    assert telemetry["status"] == "OK"

    assert 0 <= telemetry["battery"] <= 100

    assert -90 <= telemetry["latitude"] <= 90

    assert -180 <= telemetry["longitude"] <= 180