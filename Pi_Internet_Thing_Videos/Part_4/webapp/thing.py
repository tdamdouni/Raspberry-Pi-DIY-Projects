import atexit
import threading
import time

import Adafruit_DHT
import RPi.GPIO as GPIO


DHT_TYPE    = Adafruit_DHT.AM2302
DHT_PIN     = 18
LED_PIN     = 23
SWITCH_PIN  = 24


# Make sure RPI.GPIO resources are cleaned up at the end of the program.
atexit.register(GPIO.cleanup)


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
        # Setup user-defined callbacks for switch and temp/hum
        self._switch_callback = None
        self._dht_callback = None
        # Register a callback to be called when the switch changes from high to
        # low or vice/versa.
        GPIO.add_event_detect(SWITCH_PIN, GPIO.BOTH, callback=self._switch_change,
                              bouncetime=20) # 20ms debounce time
        # Setup a thread to read the DHT sensor and update the temp & humidity.
        self._dht_thread = threading.Thread(target=self._update_dht)
        self._dht_thread.daemon = True  # Don't let this thread block exiting.
        self._dht_thread.start()

    def _switch_change(self, pin):
        """Called by the RPI.GPIO library when the switch pin changes state."""
        # Check if someone has registered a thing switch callback and call it
        # with the current thing switch state.
        if self._switch_callback is not None:
            self._switch_callback(GPIO.input(SWITCH_PIN))

    def _update_dht(self):
        """Main function for DHT update thread, will grab new temp & humidity
        values every two seconds.
        """
        while True:
            with self._lock:
                # Read the humidity and temperature from the DHT sensor.
                humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
                # Fire any callback to receive the latest values.
                if self._dht_callback is not None:
                    self._dht_callback(temperature, humidity)
            # Wait 2 seconds then repeat.
            time.sleep(2.0)

    def on_switch_change(self, callback):
        """Register a function to be called when the switch changes state.
        Callback should be a function that takes one argument, the current switch
        state as a boolean.
        """
        self._switch_callback = callback

    def on_temp_humidity_change(self, callback):
        """Register a function to be called when the temperature & humidity state
        changes.  Callback should be a function that takes two arguments, the
        current temperature (in degrees Celsius) and the current humidity (in %).
        """
        self._dht_callback = callback

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
