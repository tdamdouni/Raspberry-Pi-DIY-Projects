from display_colours import *
import unittest

class TestDisplay(unittest.TestCase):
    def setUp(self):
        pass

    def test_display_temperature(self):
        self.assertEqual(temperature_to_hue(-1.5), (255, 255, 255))
        self.assertEqual(temperature_to_hue(35.7), (255, 0, 0))
        self.assertEqual(temperature_to_hue(10.5), (0, 0, 255) )
        # ends of range

    def test_colour_interpolation_works(self):
        blue = Color("blue")
        green = Color("green")
        transition_cols = list(blue.range_to(green, 10))
        print(transition_cols)

        self.assertEqual(len(transition_cols), 10)  # 10 colour values
        # start of range is blue
        self.assertEqual(one_range_to_255_range(transition_cols[0].rgb), (0, 0, 255))
        # end of range is green
        self.assertEqual(one_range_to_255_range(transition_cols[9].rgb), (0, 128, 0))

    def test_hue_translation(self):
        self.assertEqual(hue_to_RGB("Red"), (255, 0, 0))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
