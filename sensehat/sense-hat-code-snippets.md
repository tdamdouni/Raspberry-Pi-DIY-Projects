#1
from sense_hat import SenseHat
sense = SenseHat()

temperature = sense.temperature
sense.show_message("Temperature is %d" % temperature)

#2
sense.show_message("Hello my name is Tim Peake")

#3
from sense_hat import SenseHat

sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)

message = "Astro Pi is awesome!!"

speed = 0.05

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

#4
from sense_hat import SenseHat

sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)

message = "Astro Pi is awesome!!"

speed = 0.05

while True:
    sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

#5
from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

sense.show_letter("J", red)

#6
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

sense.show_letter("O", red)
sleep(1)
sense.show_letter("M", blue)
sleep(1)
sense.show_letter("G", green)
sleep(1)
sense.show_letter("!", black, white)
sleep(1)
sense.clear()

#7
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

r = randint(0,255)
sense.show_letter("O", (r, 0, 0))
sleep(1)

r = randint(0,255)
sense.show_letter("M", (0, 0, r))
sleep(1)

r = randint(0,255)
sense.show_letter("G", (0, r, 0))
sleep(1)

sense.show_letter("!", (0, 0, 0), (255, 255, 255))
sleep(1)
sense.clear()

#8
