#!/usr/bin/env python

from time import sleep, gmtime, strftime
import sys
import colorsys

import unicornhat as unicorn

TEXT_COLOUR = None # Rainbow
#TEXT_COLOUR = (255,0,0) # RGB - Red
SCROLL_SPEED = 0.2 

CHARS = {" ": ["  ", "  ", "  ", "  "],
         "A": [ "XXX", 
                "X X", 
                "XXX", 
                "X X" ],

         "B": [ "X  ", 
                "XXX", 
                "X X", 
                "XXX" ],

         "C": [ "XXX", 
                "X  ", 
                "X  ", 
                "XXX" ],

         "D": [ "XX ", 
                "X X", 
                "X X", 
                "XX " ],
    
         "E": [ "XXX", 
                "XX ", 
                "X  ", 
                "XXX" ],

         "F": [ "XXX", 
                "X  ", 
                "XX ", 
                "X  " ],

         "G": [ "XXX", 
                "X  ", 
                "X X", 
                "XXX" ],

         "H": [ "X X", 
                "X X", 
                "XXX", 
                "X X" ],

         "I": [ "XXX", 
                " X ", 
                " X ", 
                "XXX" ],

         "J": [ " XX", 
                "  X", 
                "X X", 
                " X " ],

         "K": [ "X X", 
                "XX ", 
                "XX ", 
                "X X" ],

         "L": [ "X  ",
                "X  ",
                "X  ", 
                "XXX" ],

         "M": [ "XX XX", 
                "X X X", 
                "X   X",   
                "X   X" ],

         "N": [ "X  X", 
                "XX X", 
                "X XX", 
                "X  X" ],

         "O": [ " X ", 
                "X X", 
                "X X", 
                " X " ],

         "P": [ "XXX", 
                "X X", 
                "XXX", 
                "X  " ],

         "Q": [ " X  ", 
                "X X ", 
                "X X ", 
                " XXX" ],

         "R": [ "XXX", 
                "X X", 
                "XX ", 
                "X X" ],

         "S": [ "XXX", 
                "XX ", 
                "  X", 
                "XXX" ],

         "T": [ "XXX", 
                " X ", 
                " X ", 
                " X " ],

         "U": [ "X X", 
                "X X", 
                "X X", 
                "XXX" ],

         "V": [ "X X", 
                "X X", 
                "X X", 
                " X " ],

         "W": [ "X   X", 
                "X   X", 
                "X X X", 
                " X X " ],

         "X": [ "X X", 
                " X ", 
                " X ", 
                "X X" ],

         "Y": [ "X X", 
                "X X", 
                " X ", 
                " X " ],

         "Z": [ "XXX", 
                " XX", 
                "XX ", 
                "XXX" ],

         ".": [ "  ", 
                "  ", 
                "  ", 
                "X " ],

         ",": [ "  ", 
                "  ", 
                "X ", 
                "X " ],

         "!": [ "X ", 
                "X ", 
                "  ", 
                "X " ],

         "?": [ "XXX", 
                " XX", 
                "   ", 
                " X " ],

         "'": [ "X", 
                "X", 
                " ", 
                " " ],

         ":": [ "X",
                " ",
                " ",
                "X" ],

         "1": [ "X", 
                "X", 
                "X", 
                "X" ],

         "2": [ "XXX", 
                " XX", 
                "X  ", 
                "XXX" ],

         "3": [ "XXX", 
                " XX", 
                "  X", 
                "XXX" ],

         "4": [ "X  ", 
                "X X", 
                "XXX", 
                "  X" ],

         "5": [ "XXX", 
                "XX ", 
                "  X", 
                "XXX" ],

         "6": [ "XXX", 
                "X  ", 
                "XXX", 
                "XXX" ],

         "7": [ "XXX", 
                "  X", 
                "  X", 
                "  X" ],

         "8": [ "XXX", 
                "X X", 
                "XXX", 
                "XXX" ],

         "9": [ "XXX", 
                "X X", 
                "XXX", 
                "  X" ],

         "0": [ "XXX", 
                "X X", 
                "X X", 
                "XXX" ]}

def init_unicorn():
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(180)
    unicorn.brightness(0.4)


class ScrollingText:

    def __init__(self, text="", speed=SCROLL_SPEED, colour=TEXT_COLOUR):
        self.speed=speed
        init_unicorn() 
        self.max_width, self.max_height = unicorn.get_shape()
        self.reset_pixels()
        self.set_text(text)
        self.reset_position()
        self.init_colour(colour)

    def reset_pixels(self):
        self.pixels = []
        for i in range(self.max_height):
            self.pixels.append([])

    def add_column(self, col):
        for i in range(4):
            self.pixels[i].append(col[i])

    def add_letter(self, letter):
        letter = letter.upper()
        if not letter in CHARS:
           letter = '?'
        map = CHARS[letter]
        for i in range(len(map[0])):
            col = []
            for j in range(len(map)):
                col.append(map[j][i])
            self.add_column(col)
        self.add_blank_column()

    def add_blank_column(self):
        col = []
        for i in range(self.max_height):
            col.append(' ')
        self.add_column(col)

    def set_text(self, text):
        self.reset_pixels()
        for letter in text:
            self.add_letter(letter)                
    
    def pixels_width(self):
        return len(self.pixels[0])

    def reset_position(self):
        self.position = -self.max_width

    def init_colour(self, colour):
        self.default_colour=colour
        self.colour = 0.0
        self.colour_incr = 0.01

    def peek_next_colour(self, offset=1.0):
        colour = self.colour + (offset * self.colour_incr) 
        if colour > 1:
            colour = colour - 1.0
        return colour

    def set_next_colour(self):
        self.colour = self.peek_next_colour()

    def get_colour_rgb(self, offset=0):
        if self.default_colour:
            rgb = self.default_colour
        else:
            colour = self.peek_next_colour(offset)
            rgb = colorsys.hsv_to_rgb(colour,1.0,1.0)    
            rgb = [int(x*255) for x in rgb]
        return rgb

    def scroll(self, loop_count=0, text=None):
        if text:
            self.set_text(text)
        count=loop_count
        while loop_count == 0 or count > 0:
            self.scroll_once()
            count -= 1

    def scroll_once(self):
        self.reset_position()
        while self.position <= self.pixels_width():
            self.display()
            sleep(self.speed)
            self.position += 1  
            self.set_next_colour()

    def display(self):
        for x in range(self.max_width):
            (r,g,b) = self.get_colour_rgb(x)
            for y in range(self.max_height):
                if (self.position + x < self.pixels_width()
                and self.position + x >= 0
                and self.pixels[y][self.position+x] == 'X'):
                   unicorn.set_pixel(x, y, r, g, b)
                else:
                   unicorn.set_pixel(x, y, 0, 0, 0)                
        unicorn.show()

def demo(text):
    scrolling = ScrollingText(text)
    scrolling.scroll()

def disp_time():
    scrolling = ScrollingText(colour=(127,0,0))
    while True:
        now = strftime("%a %-d %b %H:%M", gmtime())        
        scrolling.scroll(1, now)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = "Unicorn pHAT scrolling rainbow text."
    if text.upper() == "CLOCK":
        disp_time()
    else:
        demo(text)
