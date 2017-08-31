import unittest
from camera import exposureCalc

class test_exposureCalc(unittest.TestCase):
    def test_exposureCalc_lowerBounds_noshot(self):
        am = 500
        pm = 2000
        exposureCalc1= exposureCalc(am, pm)

        hoursMinutes = 400
        take_shot = exposureCalc1.take_shot(hoursMinutes)
        self.assertEquals(False, take_shot)

    def test_exposureCalc_upperBounds_noshot(self):
        am = 500
        pm = 2000
        exposureCalc1= exposureCalc(am, pm)

        hoursMinutes = 2001
        take_shot = exposureCalc1.take_shot(hoursMinutes)
        self.assertEquals(False, take_shot)

if __name__ == '__main__':
    unittest.main()
