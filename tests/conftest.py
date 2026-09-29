import subprocess
import sys
import time

import pytest


@pytest.fixture(scope="session")
def simulator_process():

    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "device.simulator",
        ]
    )

    time.sleep(0.5)

    yield process

    process.terminate()

    try:
        process.wait(timeout=3)

    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=3)