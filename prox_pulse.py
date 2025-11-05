import time

from .pulse import pulse
from .abstract import LEDController, ProximitySensor

THRESHOLD: int = 75

RED: tuple[int, int, int] = (150, 10, 10)
GREEN: tuple[int, int, int] = (30, 100, 10)


def prox_pulse(px: LEDController, color: tuple[int, int, int], prox: int) -> None:
    """
    Maps proximity value to pulse duration and calls pulse.

    Args:
        px: LED controller object.
        color (tuple): color to pulse.
        prox (int): proximity value.
    """
    ...


def run_prox_pulse(apds: ProximitySensor, pixels: LEDController) -> None:
    """
    Runs proximity-based pulsing demo.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
    """
    # Main loop

    while True:
        print(apds.proximity)
        if apds.proximity >= THRESHOLD:
            pulse(pixels, RED, 1)
