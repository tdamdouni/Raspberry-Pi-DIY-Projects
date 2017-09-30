import sys, time, bme

print '\nRunning this script takes the current'
print 'temperature, pressure and humidity reading every 5 minutes'
print 'along with an image capture. \n'
print "The data is stored in 'log.txt' and"
print "the images in the 'imgs' folder both found at the root of this script."
print '\n'
print 'NOTE: Press ctrl+c to exit program!'
print '\n'

while True:
    bme.read_temp()
    time.sleep(300)



