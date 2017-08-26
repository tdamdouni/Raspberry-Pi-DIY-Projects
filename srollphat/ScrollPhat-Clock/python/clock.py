#!/usr/bin/env python

# Designed by Chris Butcher to overcome Three (3) Digit Limit
# On the ScrollPhat by Pimoroni

import scrollphat
import time, sys, os
from time import sleep, strftime
from datetime import datetime

# Using the 'set_pixel' command to create custom numbers allowing 
# four (4) number to fit ontop the 11x5 LED Matrix.

# This then calls the numbers as required by the 'strftime' module
# to display the clock on the LED Matrix

# The only addition was the centre flashing to simulate the seconds

# please see disclaimer at bottom of file


# Setup ScrollPhat for Brightness and Rotation
scrollphat.set_brightness(1)
scrollphat.rotate = True

# Centre Flashing Colon (ON)
def sec_gap_on():
    scrollphat.set_pixel(5,1,1)
    scrollphat.set_pixel(5,3,1)

# Centre Flashing Colon (OFF)
def sec_gap_off():
    scrollphat.set_pixel(5,1,0)
    scrollphat.set_pixel(5,3,0)

# First Digit
def num_1_matrix(digit):    
    if digit == '1':
        scrollphat.set_pixel(0,0,0)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,1)
        scrollphat.set_pixel(1,1,1)
        scrollphat.set_pixel(0,2,0)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,0)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,0)
        scrollphat.set_pixel(1,4,1)
    
    if digit == '2':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,0)
        scrollphat.set_pixel(1,1,1)
        scrollphat.set_pixel(0,2,1)
        scrollphat.set_pixel(1,2,0)
        scrollphat.set_pixel(0,3,1)
        scrollphat.set_pixel(1,3,0)
        scrollphat.set_pixel(0,4,1)
        scrollphat.set_pixel(1,4,1)
    
    if digit == '3':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,0)
        scrollphat.set_pixel(1,1,1)
        scrollphat.set_pixel(0,2,1)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,0)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,1)
        scrollphat.set_pixel(1,4,1)
    
    if digit == '4':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,0)
        scrollphat.set_pixel(0,1,1)
        scrollphat.set_pixel(1,1,0)
        scrollphat.set_pixel(0,2,1)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,0)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,0)
        scrollphat.set_pixel(1,4,1)

    if digit == '5':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,1)
        scrollphat.set_pixel(1,1,0)
        scrollphat.set_pixel(0,2,1)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,0)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,1)
        scrollphat.set_pixel(1,4,1)
    
    if digit == '6':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,0)
        scrollphat.set_pixel(0,1,1)
        scrollphat.set_pixel(1,1,0)
        scrollphat.set_pixel(0,2,1)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,1)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,1)
        scrollphat.set_pixel(1,4,1)
    
    if digit == '7':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,0)
        scrollphat.set_pixel(1,1,1)
        scrollphat.set_pixel(0,2,0)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,0)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,0)
        scrollphat.set_pixel(1,4,1)
    
    if digit == '8':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,1)
        scrollphat.set_pixel(1,1,1)
        scrollphat.set_pixel(0,2,0)
        scrollphat.set_pixel(1,2,0)
        scrollphat.set_pixel(0,3,1)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,1)
        scrollphat.set_pixel(1,4,1)

    if digit == '9':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,1)
        scrollphat.set_pixel(1,1,1)
        scrollphat.set_pixel(0,2,1)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,0)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,0)
        scrollphat.set_pixel(1,4,1)
    
    if digit == '0':
        scrollphat.set_pixel(0,0,1)
        scrollphat.set_pixel(1,0,1)
        scrollphat.set_pixel(0,1,1)
        scrollphat.set_pixel(1,1,1)
        scrollphat.set_pixel(0,2,1)
        scrollphat.set_pixel(1,2,1)
        scrollphat.set_pixel(0,3,1)
        scrollphat.set_pixel(1,3,1)
        scrollphat.set_pixel(0,4,1)
        scrollphat.set_pixel(1,4,1)
    
# Second Digit
def num_2_matrix(digit):    
    if digit == '1':
        scrollphat.set_pixel(3,0,0)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,1)
        scrollphat.set_pixel(4,1,1)
        scrollphat.set_pixel(3,2,0)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,0)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,0)
        scrollphat.set_pixel(4,4,1)
    
    if digit == '2':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,0)
        scrollphat.set_pixel(4,1,1)
        scrollphat.set_pixel(3,2,1)
        scrollphat.set_pixel(4,2,0)
        scrollphat.set_pixel(3,3,1)
        scrollphat.set_pixel(4,3,0)
        scrollphat.set_pixel(3,4,1)
        scrollphat.set_pixel(4,4,1)
    
    if digit == '3':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,0)
        scrollphat.set_pixel(4,1,1)
        scrollphat.set_pixel(3,2,1)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,0)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,1)
        scrollphat.set_pixel(4,4,1)
    
    if digit == '4':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,0)
        scrollphat.set_pixel(3,1,1)
        scrollphat.set_pixel(4,1,0)
        scrollphat.set_pixel(3,2,1)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,0)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,0)
        scrollphat.set_pixel(4,4,1)

    if digit == '5':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,1)
        scrollphat.set_pixel(4,1,0)
        scrollphat.set_pixel(3,2,1)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,0)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,1)
        scrollphat.set_pixel(4,4,1)
    
    if digit == '6':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,0)
        scrollphat.set_pixel(3,1,1)
        scrollphat.set_pixel(4,1,0)
        scrollphat.set_pixel(3,2,1)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,1)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,1)
        scrollphat.set_pixel(4,4,1)
    
    if digit == '7':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,0)
        scrollphat.set_pixel(4,1,1)
        scrollphat.set_pixel(3,2,0)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,0)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,0)
        scrollphat.set_pixel(4,4,1)
    
    if digit == '8':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,1)
        scrollphat.set_pixel(4,1,1)
        scrollphat.set_pixel(3,2,0)
        scrollphat.set_pixel(4,2,0)
        scrollphat.set_pixel(3,3,1)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,1)
        scrollphat.set_pixel(4,4,1)

    if digit == '9':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,1)
        scrollphat.set_pixel(4,1,1)
        scrollphat.set_pixel(3,2,1)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,0)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,0)
        scrollphat.set_pixel(4,4,1)
    
    if digit == '0':
        scrollphat.set_pixel(3,0,1)
        scrollphat.set_pixel(4,0,1)
        scrollphat.set_pixel(3,1,1)
        scrollphat.set_pixel(4,1,1)
        scrollphat.set_pixel(3,2,1)
        scrollphat.set_pixel(4,2,1)
        scrollphat.set_pixel(3,3,1)
        scrollphat.set_pixel(4,3,1)
        scrollphat.set_pixel(3,4,1)
        scrollphat.set_pixel(4,4,1)
        
# Third Digit
def num_3_matrix(digit):    
    if digit == '1':
        scrollphat.set_pixel(6,0,0)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,1)
        scrollphat.set_pixel(7,1,1)
        scrollphat.set_pixel(6,2,0)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,0)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,0)
        scrollphat.set_pixel(7,4,1)
    
    if digit == '2':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,0)
        scrollphat.set_pixel(7,1,1)
        scrollphat.set_pixel(6,2,1)
        scrollphat.set_pixel(7,2,0)
        scrollphat.set_pixel(6,3,1)
        scrollphat.set_pixel(7,3,0)
        scrollphat.set_pixel(6,4,1)
        scrollphat.set_pixel(7,4,1)
    
    if digit == '3':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,0)
        scrollphat.set_pixel(7,1,1)
        scrollphat.set_pixel(6,2,1)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,0)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,1)
        scrollphat.set_pixel(7,4,1)
    
    if digit == '4':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,0)
        scrollphat.set_pixel(6,1,1)
        scrollphat.set_pixel(7,1,0)
        scrollphat.set_pixel(6,2,1)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,0)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,0)
        scrollphat.set_pixel(7,4,1)

    if digit == '5':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,1)
        scrollphat.set_pixel(7,1,0)
        scrollphat.set_pixel(6,2,1)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,0)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,1)
        scrollphat.set_pixel(7,4,1)
    
    if digit == '6':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,0)
        scrollphat.set_pixel(6,1,1)
        scrollphat.set_pixel(7,1,0)
        scrollphat.set_pixel(6,2,1)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,1)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,1)
        scrollphat.set_pixel(7,4,1)
    
    if digit == '7':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,0)
        scrollphat.set_pixel(7,1,1)
        scrollphat.set_pixel(6,2,0)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,0)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,0)
        scrollphat.set_pixel(7,4,1)
    
    if digit == '8':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,1)
        scrollphat.set_pixel(7,1,1)
        scrollphat.set_pixel(6,2,0)
        scrollphat.set_pixel(7,2,0)
        scrollphat.set_pixel(6,3,1)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,1)
        scrollphat.set_pixel(7,4,1)

    if digit == '9':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,1)
        scrollphat.set_pixel(7,1,1)
        scrollphat.set_pixel(6,2,1)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,0)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,0)
        scrollphat.set_pixel(7,4,1)
    
    if digit == '0':
        scrollphat.set_pixel(6,0,1)
        scrollphat.set_pixel(7,0,1)
        scrollphat.set_pixel(6,1,1)
        scrollphat.set_pixel(7,1,1)
        scrollphat.set_pixel(6,2,1)
        scrollphat.set_pixel(7,2,1)
        scrollphat.set_pixel(6,3,1)
        scrollphat.set_pixel(7,3,1)
        scrollphat.set_pixel(6,4,1)
        scrollphat.set_pixel(7,4,1)

# Fourth Digit
def num_4_matrix(digit):    
    if digit == '1':
        scrollphat.set_pixel(9,0,0)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,1)
        scrollphat.set_pixel(10,1,1)
        scrollphat.set_pixel(9,2,0)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,0)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,0)
        scrollphat.set_pixel(10,4,1)
    
    if digit == '2':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,0)
        scrollphat.set_pixel(10,1,1)
        scrollphat.set_pixel(9,2,1)
        scrollphat.set_pixel(10,2,0)
        scrollphat.set_pixel(9,3,1)
        scrollphat.set_pixel(10,3,0)
        scrollphat.set_pixel(9,4,1)
        scrollphat.set_pixel(10,4,1)
    
    if digit == '3':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,0)
        scrollphat.set_pixel(10,1,1)
        scrollphat.set_pixel(9,2,1)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,0)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,1)
        scrollphat.set_pixel(10,4,1)
    
    if digit == '4':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,0)
        scrollphat.set_pixel(9,1,1)
        scrollphat.set_pixel(10,1,0)
        scrollphat.set_pixel(9,2,1)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,0)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,0)
        scrollphat.set_pixel(10,4,1)

    if digit == '5':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,1)
        scrollphat.set_pixel(10,1,0)
        scrollphat.set_pixel(9,2,1)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,0)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,1)
        scrollphat.set_pixel(10,4,1)
    
    if digit == '6':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,0)
        scrollphat.set_pixel(9,1,1)
        scrollphat.set_pixel(10,1,0)
        scrollphat.set_pixel(9,2,1)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,1)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,1)
        scrollphat.set_pixel(10,4,1)
    
    if digit == '7':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,0)
        scrollphat.set_pixel(10,1,1)
        scrollphat.set_pixel(9,2,0)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,0)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,0)
        scrollphat.set_pixel(10,4,1)
    
    if digit == '8':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,1)
        scrollphat.set_pixel(10,1,1)
        scrollphat.set_pixel(9,2,0)
        scrollphat.set_pixel(10,2,0)
        scrollphat.set_pixel(9,3,1)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,1)
        scrollphat.set_pixel(10,4,1)

    if digit == '9':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,1)
        scrollphat.set_pixel(10,1,1)
        scrollphat.set_pixel(9,2,1)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,0)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,0)
        scrollphat.set_pixel(10,4,1)
    
    if digit == '0':
        scrollphat.set_pixel(9,0,1)
        scrollphat.set_pixel(10,0,1)
        scrollphat.set_pixel(9,1,1)
        scrollphat.set_pixel(10,1,1)
        scrollphat.set_pixel(9,2,1)
        scrollphat.set_pixel(10,2,1)
        scrollphat.set_pixel(9,3,1)
        scrollphat.set_pixel(10,3,1)
        scrollphat.set_pixel(9,4,1)
        scrollphat.set_pixel(10,4,1)

# Adjusted 1/2 Second Delay       
delay = 0.397  
  
# Pogram to Display the Clock, this will run until QUIT
while True:
    try:
    
        clock = datetime.now().strftime('%H %M')       
        
        # Hours - Digits
        num_1_matrix(clock[0])
        num_2_matrix(clock[1])
        
        # Minutes - Digits
        num_3_matrix(clock[3])
        num_4_matrix(clock[4])
        
        # Flash ON
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        # Flash OFF
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
    except KeyboardInterrupt:
    
        # Clears ScrollPhat and Screen on QUIT
        scrollphat.clear()
        os.system("clear")
        sys.exit(-1)


# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
