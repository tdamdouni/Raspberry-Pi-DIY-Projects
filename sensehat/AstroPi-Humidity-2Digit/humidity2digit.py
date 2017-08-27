from astro_pi import AstroPi
import time
import logging
from datetime import datetime


ap = AstroPi()

r = [255, 0, 0]
e = [0, 0, 0]

space = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]
tmstmp = time.strftime("%Y%m%d-%H%M%S")
logging.basicConfig(format='%(asctime)s %(message)s',filename='humidity'+str(tmstmp)
+'.log',level=logging.DEBUG)

def numToMatrix(num):

# define 1x8 columns that make  single digits when combined

	num_1_2 = [e,e,r,e,e,e,r,e]
	num_1_1 = [e,r,r,r,r,r,r,e]
	num_1_0 = [e,e,e,e,e,e,r,e]

	num_2_2 = [e,r,e,e,e,r,r,e]
	num_2_1 = [e,r,e,e,r,e,r,e]
	num_2_0 = [e,r,r,r,e,e,r,e]

	num_3_2 = [e,r,e,e,r,e,r,e]
	num_3_1 = [e,r,e,e,r,e,r,e]
	num_3_0 = [e,r,r,r,r,r,r,e]

	num_4_2 = [e,r,r,r,r,e,e,e]
	num_4_1 = [e,e,e,e,r,e,e,e]
	num_4_0 = [e,r,r,r,r,r,r,e]

	num_5_2 = [e,r,r,r,r,e,r,e]
	num_5_1 = [e,r,e,e,r,e,r,e]
	num_5_0 = [e,r,e,e,r,r,e,e]

	num_6_2 = [e,r,r,r,r,r,r,e]
	num_6_1 = [e,r,e,e,r,e,r,e]
	num_6_0 = [e,r,e,e,r,r,r,e]

	num_7_2 = [e,r,e,e,e,e,e,e]
	num_7_1 = [e,r,e,e,e,e,e,e]
	num_7_0 = [e,r,r,r,r,r,r,e]

	num_8_2 = [e,r,r,r,r,r,r,e]
	num_8_1 = [e,r,e,e,r,e,r,e]
	num_8_0 = [e,r,r,r,r,r,r,e]

	num_9_2 = [e,r,r,r,r,e,r,e]
	num_9_1 = [e,r,e,e,r,e,r,e]
	num_9_0 = [e,r,r,r,r,r,r,e]

	num_0_2 = [e,r,r,r,r,r,r,e]
	num_0_1 = [e,r,e,e,e,e,r,e]
	num_0_0 = [e,r,r,r,r,r,r,e]

# combine columns to make digits

	sing_0 = num_0_0 + num_0_1 + num_0_2
	sing_1 = num_1_0 + num_1_1 + num_1_2
	sing_2 = num_2_0 + num_2_1 + num_2_2
	sing_3 = num_3_0 + num_3_1 + num_3_2
	sing_4 = num_4_0 + num_4_1 + num_4_2
	sing_5 = num_5_0 + num_5_1 + num_5_2
	sing_6 = num_6_0 + num_6_1 + num_6_2
	sing_7 = num_7_0 + num_7_1 + num_7_2
	sing_8 = num_8_0 + num_8_1 + num_8_2
	sing_9 = num_9_0 + num_9_1 + num_9_2

# map digits onto appropriate strings
	if num == '1':
		return sing_1
	if num == '2':
		return sing_2
	if num == '3':
		return sing_3
	if num == '4':
		return sing_4
	if num == '5':
		return sing_5
	if num == '6':
		return sing_6
	if num == '7':
		return sing_7
	if num == '8':
		return sing_8
	if num == '9':
		return sing_9
	if num == '0':
		return sing_0

# set previous humidity value to zero

hum_prev = 0

# Main program loop

while True:

# Get humidity from astro-pi

	hum_f = ap.get_humidity()
	hum_int = int(hum_f)
# test to see if value is higher or lower than previous, and then set led colour appropriately 
	logging.info(hum_f)
	if hum_int > hum_prev:
		r = [0,255,0] # green if higher
	elif hum_int == hum_prev:
		r = [255,127,0] # orange if the same
	else:
		r = [255,0,0] # red if lower
	hum_prev = hum_int
	hum =  str(hum_int) # convert reading to string
	
	# add a leading zero for single digit readings
	if hum_int < 10:
		hum = '0' + hum
	
	image = numToMatrix(hum[1]) + space + numToMatrix(hum[0]) # build image from two digits plus spacer
	ap.set_pixels(image)
	time.sleep(0.5)


