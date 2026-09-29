import json
import socket


HOST = "127.0.0.1"
PORT = 5005


def receive_telemetry(
    host: str = HOST,
    port: int = PORT,
    timeout: float = 2.0,
) -> dict:

    with socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM,
    ) as udp_socket:

        udp_socket.bind(
            (host, port)
        )

        udp_socket.settimeout(timeout)

        data, address = udp_socket.recvfrom(4096)

        json_data = data.decode("utf-8")

        telemetry = json.loads(json_data)

        return telemetry


if __name__ == "__main__":
    print(
        f"Listening for UDP telemetry "
        f"on {HOST}:{PORT}"
    )

    telemetry = receive_telemetry()

    print(
        f"Received telemetry: {telemetry}"
    )