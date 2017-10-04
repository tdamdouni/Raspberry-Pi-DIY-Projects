import threading
import time

import Adafruit_DHT
import RPi.GPIO as GPIO


DHT_TYPE    = Adafruit_DHT.AM2302
DHT_PIN     = 18
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
        # Setup a thread to read the DHT sensor every 2 seconds and store
        # its last known value.
        self._humidity = None
        self._temperature = None
        self._dht_thread = threading.Thread(target=self._update_dht)
        self._dht_thread.daemon = True  # Don't let this thread block exiting.
        self._dht_thread.start()

    def _update_dht(self):
        """Main function for DHT update thread, will grab new temp & humidity
        values every two seconds.
        """
        while True:
            with self._lock:
                # Read the humidity and temperature from the DHT sensor.
                self._humidity, self._temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
            # Wait 2 seconds then repeat.
            time.sleep(2.0)

    def get_humidity(self):
        """Get the most recent humidity value (%)."""
        with self._lock:
            return self._humidity

    def get_temperature(self):
        """Get the most recent temperature value (in degrees Celsius)."""
        with self._lock:
            return self._temperature

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
