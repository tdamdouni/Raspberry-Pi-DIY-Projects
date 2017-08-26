#===============================================================================
# rpi_weather.py
#
# Class for interfacing to Raspberry Pi with four Adafruit 8x8 LEDs attached.
#
# 2015-04-15
# Carter Nelson
#===============================================================================
from time import sleep

from Adafruit_LED_Backpack import Matrix8x8
from led8x8icons import LED8x8ICONS

class RpiWeather():
    """Class for interfacing to Raspberry Pi with four Adafruit 8x8 LEDs attached."""
    
    def __init__(self, ):
        self.matrix = []
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x70, busnum=1))
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x71, busnum=1))
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x72, busnum=1))
        self.matrix.append(Matrix8x8.Matrix8x8(address=0x73, busnum=1))
        for m in self.matrix:
            m.begin()
          
    def is_valid_matrix(self, matrix):
        """Returns True if matrix number is valid, otherwise False."""
        return matrix in xrange(len(self.matrix))     
          
    def clear_disp(self, matrix=None):
        """Clear specified matrix. If none specified, clear all."""
        if matrix == None:
            for m in self.matrix:
                m.clear()
                m.write_display()
        else:
            if not self.is_valid_matrix(matrix):
                return
            self.matrix[matrix].clear()
            self.matrix[matrix].write_display()
            
    def set_pixel(self, x, y, matrix=0, value=1):
        """Set pixel at position x, y for specified matrix to the given value."""
        if not self.is_valid_matrix(matrix):
            return
        self.matrix[matrix].set_pixel(x, y, value)
        self.matrix[matrix].write_display()
          
    def set_bitmap(self, bitmap, matrix=0):
        """Set specified matrix to provided bitmap."""
        if not self.is_valid_matrix(matrix):
            return
        for x in xrange(8):
            for y in xrange(8):
                self.matrix[matrix].set_pixel(x, y, bitmap[y][x])
        self.matrix[matrix].write_display()
        
    def set_raw64(self, value, matrix=0):
        """Set specified matrix to bitmap defined by 64 bit value."""
        if not self.is_valid_matrix(matrix):
            return        
        self.matrix[matrix].clear()
        for y in xrange(8):
            row_byte = value >> (8*y)
            for x in xrange(8):
                pixel_bit = row_byte >> x & 0x01 
                self.matrix[matrix].set_pixel(x, y, pixel_bit) 
        self.matrix[matrix].write_display()
        
    def scroll_raw64(self, value, matrix=0, delay=0.15):
        """Scroll out the current bitmap with the supplied bitmap. Can also
        specify a matrix (0-3) and a delay to set scroll rate.
        """
        for step in xrange(7,-1,-1):
            for old_row in xrange(7,0,-1):
                self.matrix[matrix].buffer[old_row*2] = self.matrix[matrix].buffer[(old_row-1)*2]
            new_row = (value >> (8*step)) & 0xff
            new_row = (new_row << 7 | new_row >> 1) & 0xff  #fix for memory buffer error
            self.matrix[matrix].buffer[0] = new_row
            self.matrix[matrix].write_display()
            sleep(delay)   
        
    def disp_number(self, number):
        """Display number as integer. Valid range is 0 to 9999."""
        num = int(number)
        if num > 9999 or num < 0:
            return
        self.clear_disp()
        matrix = 3
        while num:
            digit = num % 10
            self.set_raw64(LED8x8ICONS['{0}'.format(digit)], matrix)
            num /= 10
            matrix -= 1