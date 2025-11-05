from .abstract import LEDController, ProximitySensor, TouchSensor
from .pulse import run_simple_pulse  # pyright: ignore
from .prox_pulse import run_prox_pulse  # pyright: ignore
from .morse_engine import run_morse_engine  # pyright: ignore


def run(apds: ProximitySensor, pixels: LEDController, touch: TouchSensor):
    """
    Runs the selected demo on the Trinkey.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
        touch: touch sensor.
    """
    # run_simple_pulse(pixels)
    run_prox_pulse(apds, pixels)
    # run_morse_engine(apds, pixels, touch)
