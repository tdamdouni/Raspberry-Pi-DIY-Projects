#! /usr/bin/env python

# http://forums.pimoroni.com/t/hilbert-curve-on-the-unicorn-hat/4427

##  Hilbert_Chase.py

##  Author  :  Craig Thomas (Honorable mention to John Burkardt for the complex maths)
##  Created :  2017.03.27

##  Inspired by the Raspberry Pi, Unicorn HAT and the Hilbert Curve
#   https://en.wikipedia.org/wiki/Hilbert_curve

##  John Burkardt's code
#   https://people.sc.fsu.edu/~jburkardt/py_src/hilbert_curve/hilbert_curve.html

##  Other Useful links:
#   https://shop.pimoroni.com/products/unicorn-hat
#   https://github.com/pimoroni/unicorn-hat
#   https://learn.pimoroni.com/tutorial/unicorn-hat/making-rainbows-with-unicorn-hat




# Import statements

import unicornhat as uh
import colorsys as col
import time



def d2xy ( m, d ):

#*****************************************************************************80
#
## D2XY converts a 1D Hilbert coordinate to a 2D Cartesian coordinate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Parameters:
#
#    Input, integer M, the index of the Hilbert curve.
#    The number of cells is N=2^M.
#    0 < M.
#
#    Input, integer D, the Hilbert coordinate of the cell.
#    0 <= D < N * N.
#
#    Output, integer X, Y, the Cartesian coordinates of the cell.
#    0 <= X, Y < N.
#
  n = 2 ** m

  x = 0
  y = 0
  t = d
  s = 1

  while ( s < n ):

	rx = ( ( t // 2 ) % 2 )
	if ( rx == 0 ):
	  ry = ( t % 2 )
	else:
	  ry = ( ( t ^ rx ) % 2 )
	x, y = rot ( s, x, y, rx, ry )
	x = x + s * rx
	y = y + s * ry
	t = ( t // 4 )

	s = s * 2

  return x, y


  
  
def rot ( n, x, y, rx, ry ):

#*****************************************************************************80
#
## ROT rotates and flips a quadrant appropriately.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Parameters:
#
#    Input, integer N, the length of a side of the square.  
#    N must be a power of 2.
#
#    Input/output, integer X, Y, the coordinates of a point.
#
#    Input, integer RX, RY, ???
#
  if ( ry == 0 ):
#
#  Reflect.
#
	if ( rx == 1 ):
	  x = n - 1 - x
	  y = n - 1 - y
#
#  Flip.
#
	t = x
	x = y
	y = t

  return x, y

  
 
  
  
def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

  


def draw ( x, y, r=255, g=0, b=0 ):
	# Function to draw a pixel a particular colour on the unicorn HAT and pause
	
	uh.set_pixel(x,y,r,g,b)
	uh.show()				# Show the new pixel
	time.sleep( 1.0 / 10 )	# Pause for 1/10th of a second
	
	return		# End def draw
	
	
def d2xy_walk ( ):

#*****************************************************************************80
#
## D2XY_WALK runs D2XY.
#
	# Partly my function
	
	# import platform
	#import unicornhat as uh
	#from time import sleep
	#import colorsys

	m = 3
	n = 2 ** m

	print ( '' )
	print ( '    D    X    Y    R    G    B' )
	print ( '' )
	
	huemax = 10		# Number of steps in hue to take to cover the entire range
	for hue in range ( 0 , huemax ):
		# For each hue step
		
		for d in range ( 0, n * n ):
			# For each pixel
			
			x, y = d2xy ( m, d )	# Get location on grid
			rgb = col.hsv_to_rgb( (1.0 * hue) / huemax, 1.0, 1.0 )		# Convert HSV stepped colour to RGB
			r = int( round (255 * rgb[0] ) )		# Set R, G and B values
			g = int( round (255 * rgb[1] ) )
			b = int( round (255 * rgb[2] ) )
			draw ( x, y, r, g, b )		# Draw the coloured pixel
			print ( '  %3d  %3d  %3d  %3d  %3d  %3d' % ( d, x, y, r, g, b ) )	# Text Output (debugging)
			
		# End for d
		
	# End for hue
	
	print ( '' )

	return		# End def d2xy_walk
  
  


#*****************************************************************************80
#
## The MAIN program starts HERE
  

# If being run as the primary program (not a module)  
if ( __name__ == '__main__' ):

	# Set up Unicorn HAT
	
	uh.set_layout(uh.HAT)				# Set layout to 8x8 Unicorn HAT - Default anyway?
	u_width,u_height=uh.get_shape()		# Get the shape

	uh.rotation(0)						# Set rotation
	uh.brightness(0.5)					# Set the brightness
	uh.off								# Clear the board
	
	timestamp ( )		# Timestamp the start

	# Run the Walk?
	d2xy_walk ()
	
	timestamp ( )		# Timestamp the end
  

## End of the File