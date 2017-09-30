# Just blinks morse code on the SenseHat.
# For a small novelty you can blink the actual letters on the sense hat ('flash_letter'=True on the constructor).
# Additionally: it is the only program I have written where I have had to pleasure of being able to name a method 'do_dah' and for that name to be meaningful ! :-)
#
# I don't speak Morse, so I can't say whether the output it is actually discernable to anybody - although "SOS" looked about right !
# Gets the definitions from a text file (default 'morse.txt')

from sense_hat import SenseHat
import re
import time
import sys

class Morse(object):
	# Read character-to-morse-character definitions from a text file.
	def __init__(self, infile='morse.txt', rotation=180, wpm=50, flash_letter=True):
		# Morse Encoding stuff
		self.dit="."
		self.dah="-"
		re_morse=re.compile( "^(\\"+self.dit+"|\\"+self.dah+")+$" )
		self.spacer=re.compile( "\s+" )
		self.pause=re.compile( "\.|,|\?|!"  )
		self.single_space=" "
		self.characters={}
		print "Reading morse definition file %s:"%(infile)
		for linecount, line in enumerate(open(infile), start=1):
			if not(re.match("^#", line) ):
				fields=line.split()
				if not(len(fields)==2):
					print "Error at line %d, does not contain two space-separated values"%(linecount, line)
					raise
				character, morse_character=fields[0], fields[1]
				if not(re.match(re_morse, morse_character) ):
					print "Error at line %d, I don't understand the morse character :%s"%(linecount, morse_character)
					raise
				self.characters[ character ]= morse_character 
		print "Read %d characters definitions."%len(self.characters)
		allowable_chars="".join( sorted( self.characters.keys() ) ).upper()
		print "Allowable Characters:%s"%(allowable_chars)
		self.allowable_chars=re.compile("[^%s%s]"%(self.single_space, allowable_chars ) )
		self.current_character="" # sort of cheating, using this to communicate to other methods in the same class....

		# Morse Timing stuff
		self.dit_ms=		1200/wpm
		self.dah_ms=		3 * self.dit_ms
		self.inter_element_ms=	self.dit_ms
		self.inter_letter_ms=	3 * self.dit_ms
		self.inter_word_ms=	7 * self.dit_ms

		# SenseHat stuff
		self.blank_pattern=[ [0,0,0] ] *64
		self.flash_pattern=[ [255,255,255] ] *64
		self.flash_letter=flash_letter		# Changes behaviour to flash the actual letter rather than a full-screen flash.
		
		self.sense=SenseHat()
		self.sense.rotation=rotation
		self.sense.clear()
		print "Created Morse Object, wpm=%d, rotation=%d, flash_letter=%s"%( wpm, rotation, self.flash_letter )


	def blank(self, millis):
		self.sense.set_pixels( self.blank_pattern )
		time.sleep( millis/1000.0 )

	def flash(self, on_millis, off_millis):
		self.sense.set_pixels( self.flash_pattern )
		time.sleep( on_millis/1000.0 )
		self.blank( off_millis )

	def flash_char(self, on_millis, off_millis ):
		self.sense.show_letter( self.current_character )
		time.sleep( on_millis/1000.0 )
		self.blank( off_millis )

	def do_flash(self, on_millis, off_millis ):
		if self.flash_letter:
			self.flash_char(on_millis, off_millis)
		else:
			self.flash(on_millis, off_millis)

	def do_dit(self):
		self.do_flash( self.dit_ms, self.inter_element_ms )

	# The Camptown ladies sing this song... 
	def do_dah(self):
		self.do_flash( self.dah_ms, self.inter_element_ms )

	def do_pause(self):
		self.blank( self.inter_word_ms )

	def blink_char(self, character):
		dits_and_dahs=self.characters[character]
		for dit_dah in dits_and_dahs:
			if dit_dah==self.dit:
				self.do_dit()
			elif dit_dah==self.dah:
				self.do_dah()
		self.blank(self.inter_letter_ms)

	def blink_message(self, message, repeat=1):
		normalized_message=re.sub(self.spacer, self.single_space, re.sub(self.pause, self.single_space, message) ) 
		cleaned_message=re.sub(self.allowable_chars, '', normalized_message.upper() ).strip()
		for i in range(1,repeat+1):
			print "Sending Message: %s. (%d of %d)"%(cleaned_message, i, repeat)
			for self.current_character in cleaned_message:
				sys.stdout.write( self.current_character )
				sys.stdout.flush()
				if self.current_character==self.single_space:
					self.do_pause()
				else:
					self.blink_char(self.current_character)
			print "\ndone."
			self.do_pause()


if __name__=='__main__':
	morse=Morse(wpm=10, flash_letter=False)
	morse.blink_message("Hello World")
	morse.blink_message("sos", repeat=3)

	morse=Morse(wpm=15, flash_letter=True)
	morse.blink_message("This is sort of cheating - or possibly educational" )

	

