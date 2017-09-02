# http://forums.pimoroni.com/t/display-temperature-in-colours-on-unicorn-phat/4317/2

import os # Importing the module to read the file.
import time # Importing the module to check every hour.

sec = time.time()

def getlast():
templist = open("temp.txt").read().split() #Opening the file in Python
last = templist[-1] # Getting the last value in the list

def hotornot(last): # Making a function to check for the temperature, pretty self explanatory
if last > 5:
print("HOT")
elif last <= 5:
print("COLD")
else:
print("Q! What have you done!?")

continue_ = True # Acts as a stopper gauge

while continue_ == True: # While forever:
sec1 = time.time() - sec # Set sec1 as being the time elapsed since the loop began
sec1 = int(sec1) # And make it an integer so we can easily use it
if sec1 == 3600: # If the seconds elapsed are 1 hour
temp = getlast() # Take a new last value from the temp file
light = hotornot(temp) # Find whether it is hot or not
sec = time.time() # Update the time to a new elapsed time