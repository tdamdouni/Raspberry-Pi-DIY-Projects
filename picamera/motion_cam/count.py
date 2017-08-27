import os

path, dirs, files = os.walk('/home/pi/photo_output').next()
file_count = len(files)
print (file_count)
