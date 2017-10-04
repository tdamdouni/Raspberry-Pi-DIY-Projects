import threading

import RPi.GPIO as GPIO


LED_PIN     = 23
SWITCH_PIN  = 24


class PiThing(object):
    """Internet 'thing' that can control GPIO on a Raspberry Pi."""

    def __init__(self):
        """Initialize the 'thing'."""
        # Setup GPIO library.
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        # Setup LED as an output and switch as an input.
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.setup(SWITCH_PIN, GPIO.IN)
        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()

    def read_switch(self):
        """Read the switch state and return its current value.
        """
        with self._lock:
            return GPIO.input(SWITCH_PIN)

    def set_led(self, value):
        """Set the LED to the provided value (True = on, False = off).
        """
        with self._lock:
            GPIO.output(LED_PIN, value)
