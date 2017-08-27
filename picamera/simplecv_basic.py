'''THIS IS A MOTION DETECTING PROGRAM FOR THE RASPBERRY PI
It is part of a tutorial series that you can find here:
https://www.youtube.com/playlist?list=PLlg8lN4r9qWiDzF13lJY-lGtiTFHHGcpx
Running this program requires installing SimpleCV as well as
a few other prerequisits on your pi. You can find detailed
instructions for how to do that here:
http://tinkernut.com/YtQH9
'''

#!/usr/bin/python

# https://gist.github.com/gigafide/c8a8a058334410986a3b#file-simplecv_basic-py

# http://www.tinkernut.com/portfolio/make-raspberry-pi-security-camera-finale/

#import the SimpleCV and py_gmailer  libraries
from SimpleCV import *
import py_gmailer

#initialize the camer
cam = Camera()
#set the max display size
display = Display((800,600))

#create a threshold variable to change  motion sensitivity
threshold = 5.0

#set timer variables for email loop
start_time = time.time()
wait_time = 60 #in seconds

#set a streaming variable to stream webcam online
streaming = JpegStreamer("0.0.0.0:1212")

#create a loop that constantly grabs new images from the webcam
while True:
	#set a time variable that updates with the loop
	current_time = time.time()
	#grab an image still from the camera and convert it to grayscale
	img01 = cam.getImage().toGray()
	#wait half a second
	time.sleep(0.5)
	#grab another image still from the camera and conver it to grayscale
	img02 = cam.getImage().toGray()
	#subract the images from each other, binarize and inver the colors
	diff = (img01 - img02).binarize(50).invert()
	#show the results to the screen
	diff.show()

	#dump all the values into a Numpy matrix and extract the mean avg
	matrix = diff.getNumpy()
	mean = matrix.mean()

	#if the mean is greater than our threshold variable, then save the img
	if mean >= threshold:
		#initialize the counter variable
		i = 0
		#check to see if the filename  already exists
		while os.path.exists('image%s.png' % i):
			#if it does, add one to the filename  and try again
			i += 1
		#once a unique filename has been found, save the image
		img02.save('image%s.png' % i)
		#print results to terminal
		print('Image Saved')
		#check to see if the wait time has been passed
		if current_time >= (start_time + wait_time):
			#if it has, reset the start time
			start_time = time.time()
			#grab the name of the current image	
			current_image = ("image%s.png" %i)
			#send that image to the email program
			py_gmailer.gmail(current_image)
	
	#send the current image to the webcam stream
	img02.save(streaming)