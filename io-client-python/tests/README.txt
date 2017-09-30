Adafruit IO Python Client Test README

To run the tests you can use python's built in unittest module's auto discovery.
Do this by running inside this tests directory:
  python -m unittest discover

Some tests require a valid Adafruit IO account to run, and they key for this
account is provided in the ADAFRUIT_IO_KEY environment variable.  Make sure to
set this envirionment variable before running the tests, for example to run all
the tests with a key execute in this directory:
  ADAFRUIT_IO_KEY=my_io_key_value python -m unittest discover

In addition for the MQTT tests you must set the following environment variable
to the username for your AIO account (found on https://accounts.adafruit.com):
  ADAFRUIT_IO_USERNAME=your_username

To add your own tests you are strongly encouraged to build off the test base 
class provided in base.py.  This class provides a place for common functions
that don't need to be duplicated across all the tests.  See the existing test
code for an example of how tests are written and use the base test case.
