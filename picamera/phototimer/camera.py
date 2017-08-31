class exposureCalc:
	def __init__(self, sunrise, sunset):
		self.sunrise=sunrise
		self.sunset=sunset
	def get_exposure(self, time):
		if(time >=self.sunrise and time <=self.sunset):
			return 'auto'
		return 'night'
		
	#One hour either side of sunrise/set
	def take_shot(self, time):
		if(time >=self.sunrise and time <=self.sunset):
			return True
		return False
