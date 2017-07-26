from weather import *
import unittest

class TestWeather(unittest.TestCase):
    def setUp(self):
        self.location = "3684"  # Get data from here since it's closest to
        self.mock_temp_list = ['6.7', '6.5', '6.2', '5.4', '5.2', '4.7', '4.2', '4.0', '4.2', '4.3', '4.5', '4.1', '4.1', '4.2', '3.9', '4.1', '4.3', '4.7', '5.0', '5.5', '5.7', '5.0', '4.7', '4.1', '3.6']

    def test_extracting_temperature(self):
        self.assertEqual(extract_latest_temperature(self.mock_temp_list), 3.6)

    def test_extract_25hrs_temperatures(self):
        weather_obs = extract_API_temperatures(get_MET_weather_observations(self.location))
        self.assertEqual(25, len(weather_obs))
        print("At the moment it's {0} degrees C at location {1}".format(extract_latest_temperature(weather_obs), self.location))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
