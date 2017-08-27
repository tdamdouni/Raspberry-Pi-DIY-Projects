import os
import urllib


web_file = urllib.urlopen(" Enter your URL address here ")

out_file = open('trains.csv', 'w')
out_file.write(web_file.read())
out_file.close()
print "files written"
