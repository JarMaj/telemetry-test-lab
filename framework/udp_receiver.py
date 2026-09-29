import json
import socket


HOST = "127.0.0.1"
PORT = 5005


def receive_telemetry():
    udp_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    udp_socket.bind(
        (HOST, PORT)
    )

    print(
        f"Listening for UDP telemetry "
        f"on {HOST}:{PORT}"
    )

    data, address = udp_socket.recvfrom(4096)

    print(f"Received packet from: {address}")
    print(f"Raw data: {data}")

    json_data = data.decode("utf-8")

    telemetry = json.loads(json_data)

    udp_socket.close()

    print(f"Telemetry: {telemetry}")

    return telemetry


if __name__ == "__main__":
    receive_telemetry()