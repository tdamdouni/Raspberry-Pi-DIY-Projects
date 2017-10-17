# Conway game of live on a tiny Oled screen

This is a simple NodeJS application to run a [Conway's game](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) of life on the Raspberry Pi and display the cells on an oled screen.

The screen I use is the [PiOled from Adafruit](https://www.adafruit.com/product/3527).
you can also buy it from our [pirate friends from Pimoroni](https://shop.pimoroni.com/collections/raspberry-pi/products/adafruit-pioled-128x32-monochrome-oled-add-on-for-raspberry-pi).

## TLDR

```
git clone https://github.com/Kylir/oled-fun.git
cd oled-fun
npm install
node lib/oled-conway.js
```

## In action

Look at this! So tiny! So useless! So beautiful!

![Image of oled-conway](https://github.com/Kylir/oled-fun/raw/master/img/oled-conway.jpg)

## Magic

All the Magic of the display comes from a superb NodeJS module called [oled-i2c-bus](https://www.npmjs.com/package/oled-i2c-bus). I'm just using it...


## Assumptions

+ You have a working Raspberry Pi.
+ You have a working PiOled screen (might work with another oled screen... try changing the I2C addr and the screen size.)
+ NodeJS is installed.
+ Git is installed.

## Installation

+ Clone this repository:

```sh
git clone https://github.com/Kylir/oled-fun.git
```

+ In the repository folder, install the dependencies:

```sh
cd oled-fun
npm install
```

## Run the program

```sh
node lib/oled-conway.js
```

you should see a randomly generated *world* evolving every 0.3 second.

## More...?

+ Tweak the configuration for a different I2C address or a different screen size:

Open the file `config/constants.js` and change the values.

+ Run the unit tests:

```
npm test
```

+ Why is there no semi colons?

You don't need them in Javascript. Try it for few weeks and tell me you want to go back... 
