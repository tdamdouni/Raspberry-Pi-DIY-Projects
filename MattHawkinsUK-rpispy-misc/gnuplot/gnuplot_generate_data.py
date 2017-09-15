#!/usr/bin/python
#--------------------------------------
#
#     GNUPlot Data Generator
#
# This script generates some space
# separated data to use with GNUPlot
#
# Author : Matt Hawkins
# Date   : 01/09/2017
#
# https://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
import math

# Open output file
f = open('mydata.dat','w')

# Loop
for degrees in range(720):

  # Generate three data points si,co and sq
  si=math.sin(math.radians(degrees))
  co=0.5 * math.cos(math.radians(degrees))

  if si>0:
    sq=0.6
  else:
    sq=-0.6

  # Write 3 data points to text file
  data="{} {:.02f} {:.02f} {:.02f}\n".format(degrees,si,co,sq)
  f.write(data)

# Close output file
f.close()

print("Created mydata.dat")