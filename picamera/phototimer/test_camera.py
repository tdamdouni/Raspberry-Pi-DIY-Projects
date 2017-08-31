import unittest
from camera import exposureCalc

class test_camera(unittest.TestCase):
	def test_exposureCalc_lowerBounds(self):
		exposureCalc1=exposureCalc(700,1700)
		self.assertEqual(exposureCalc1.get_exposure(700), "auto")
	def test_exposureCalc_upperBounds(self):
		exposureCalc1=exposureCalc(700,1700)
		self.assertEqual(exposureCalc1.get_exposure(1700), "auto")
	def test_exposureCalc_middleBounds(self):
		exposureCalc1=exposureCalc(700,1700)
		self.assertEqual(exposureCalc1.get_exposure(1245), "auto")
		
	def test_exposureCalc_outsideUpperBounds(self):
		exposureCalc1=exposureCalc(700,1700)
		self.assertEqual(exposureCalc1.get_exposure(2130), "night")
		
	def test_exposureCalc_outsideLowerBounds(self):
		exposureCalc1=exposureCalc(700,1700)
		self.assertEqual(exposureCalc1.get_exposure(600), "night")
		
	def test_take_shot(self):
		exp=exposureCalc(700,1700)
		self.assertEqual(exp.take_shot(1700), True)
		self.assertEqual(exp.take_shot(1245), True)
		self.assertEqual(exp.take_shot(700), True)
		self.assertEqual(exp.take_shot(699), False)
		
		self.assertEqual(exp.take_shot(0), False)
		self.assertEqual(exp.take_shot(500), False)
		self.assertEqual(exp.take_shot(2100), False)

	def test_take_shot_rangetest(self):
		exp=exposureCalc(700, 1700)
		for x in range(0,2300):
			val = exp.take_shot(x)
			# print(str(x) + " = (x) = " + str(val))
			if(x >= 700 and x <= 1700):
				self.assertTrue(val)
			else:
				self.assertFalse(val)

	def test_exposureCalc_rangetest(self):
		exp=exposureCalc(700, 1700)
		for x in range(0,2300):
			value = exp.get_exposure(x)
			self.assertTrue(value in ('auto','night'), 'value: ' + str(value) + ' not in collection')

if __name__ == '__main__':
    unittest.main()
