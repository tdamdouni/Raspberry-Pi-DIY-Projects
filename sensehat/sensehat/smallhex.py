# 'smallhex.py' : Defines small (3x5) character-definitions for hexadecimal numbers.
# Allows two-digit numbers to be displayed on the Raspberry Pi 'SenseHat' LED display. (8x8 pixels)
# The file 'smallhex.txt' holds the definition of each character in a format like this:
"""
#0
ooo
o-o
o-o
o-o
ooo
"""
# Where 'o' represents pixel-on, and '-' pixel-off.
# Each 5 line character definition needs to be preceded by a line starting with the hash (#) character , followed by the character lookup (eg '#A')
# Use the method 'to_hex_chars(int)' to generate a 64 element list of pixels , which can then be displayed with the 'sensehat' 'set_pixels' method.
# Only numbers from 0-255 (ie, '00' to 'FF')  can be displayed of course.
# [There is a 'to_dec_char(int)' also for convenience]
#
# To manually combine two arbitary characters use the 'two_char(string)' method.
# Change the global 'pixel_on/off' values to change the colour of the returned pixels. (TBD; this should really be a param to the 'hex_chars(int)' method.
#
# See: 'counter_test.py' for example use

import re
from collections import defaultdict

on_char='o'
off_char='-'
pixel_on=(255,255,0)
pixel_off=(0,0,0)

max_width=8
max_height=8
char_defs=defaultdict(list) # Character Defintions held as a list of strings; comprised of 'on/off-chars'

def pad(line):
	global pixel_off, max_width
	return line +  off_char*(max_width-len(line)) 

def char_to_pixel( char ):
	global on_char, pixel_on, pixel_off
	if char==on_char:
		return pixel_on
	else:
		return pixel_off

def combine_chars(char1, char2):
	global char_defs
	combined_char_def=[]
	for c1,c2 in zip(char_defs[char1], char_defs[char2]):
		combined_char_def.append( "%s%s%s"%(c1, off_char , c2) )
	return combined_char_def

def two_chars( characters ):
	combined=combine_chars(characters[0], characters[1])
	return fit_char_to_display( combined )

def to_hex_chars(i):
	assert(i>=0)
	assert(i<=255)
	return two_chars( hex(i)[2:].zfill(2).upper() )

def to_dec_chars(i): # sounds a bit like a posh person saying 'two deck chairs' :-)
	assert(i>=0)
	assert(i<=99)
	return two_chars("%02d"%i)

def fit_char_to_display( char_def ):
	global max_width, max_height
	padded_char_def=[]
	for line in char_def:				# For each in the char_def, pad it out to max width of display
		padded_char_def.append( pad( line ) )
	char_height=len( char_def )
	for linenum in range(max_height-char_height):	# pad empty lines to max height
		padded_char_def.append( pad("") )
	
	pix_list=[]
	for line in padded_char_def:
		for pix in [ char_to_pixel(c) for c in line ]:	# convert on_chars/off_chars to pixel values ; append to one big list of pixels
			pix_list.append( pix )
	return pix_list

def read_character_file(charfile='smallhex.txt'):
	print "Reading Character File '%s'"%charfile
	file_err="Error reading definition file %s, Line %d. No Character defined. (use '#<charname>' on line above)"	
	global char_defs,on_char, off_char, pixel_on, pixel_off
	char_code=None
	for linenum, line in enumerate( open(charfile, "rb"), start=1 ):
		if re.match("^#", line):
			char_code=line.strip()[1:]
			next
		else:
			if char_code==None or len(char_code)==0:
				raise ValueError( file_err%(charfile, linenum) )
			char_defs[char_code].append( line.strip() )
	print "Read %d Character Definitions"%(len(char_defs))

read_character_file()
