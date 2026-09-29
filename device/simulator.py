import json
import socket
import time

from device.telemetry import create_telemetry


HOST = "127.0.0.1"
PORT = 5005


def run_simulator():
    udp_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    print(
        f"Simulator started. "
        f"Sending telemetry to {HOST}:{PORT}"
    )

    while True:
        telemetry = create_telemetry()

        json_data = json.dumps(telemetry)

        payload = json_data.encode("utf-8")

        udp_socket.sendto(
            payload,
            (HOST, PORT)
        )

        print(f"Sent telemetry: {telemetry}")

        time.sleep(1)


if __name__ == "__main__":
    run_simulator()