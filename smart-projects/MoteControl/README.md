# MoteControl

### Python Flask web app for controlling [Pimoroni] (https://shop.pimoroni.com/products/mote) Mote


![alt tag](https://raw.githubusercontent.com/topshed/MoteControl/master/mote.png)

###Instructions

1) Make sure you have the Mote, colorsys and Flask Python3 libraries installed.

2) For best results also install Firefox/Iceweasel:

sudo apt-get install iceweasel

You can use the app with Epiphany although the Colour Picker function will not work and some of the styling is lost.

3) Clone this repo

4) run:

python3 motecontrol.py

5) Open your browser and go to 127.0.0.1:5000

6) Select the desired lighting for your Mote (this code assumes you have the full Mote kit with 4 mote strips):

##### Rainbow 
 Peaceful fluctuating rainbow colours

#####White 
(ish) - all on white

#####Sunny 
A jolly yellow colour (you may need to optimise for your wall colour - mine are green so I reduced the amount of green in the mix).

#####Disco 
Random flashing colours. Add extra RGB tuples to the 'colours' list.

#####Strobe
Headache inducing white flickering

#####Sparkles R
Random colours on random elements. A bit like rainbow but more glitzy

#####Stars
Random single lights will gently fade up to white than fade out again.

#####Larson 
Pretend your room is the Knight Industries 2000

#####Red Alert 
Shields Up! Man the photon torpedoes!

##### Manual and Pick Set
You can also set your own colour using the sliders. The motes will only update once the 'Manual' button is pressed. Or use the colour picker and then click 'Pick Set'. You can also set which of your 4 mote sticks are activated for this function. 
