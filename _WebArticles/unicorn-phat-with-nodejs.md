# Unicorn pHat with NodeJS

_Captured: 2017-09-01 at 12:27 from [forums.pimoroni.com](http://forums.pimoroni.com/t/unicorn-phat-with-nodejs/3113)_

Hello!

I have a confession: I'm not a Python person. So, as soon as I received my Unicorn pHat I searched for a way to program it using NodeJS.  
I found a really nice Node module wrapping the C library `rpi_ws281x`. It is called `node-rpi-ws281x-native` and it is available through npm or Github.

Here is a tiny example to get you up and running:

  * First you need NodeJS. On the downloads page [here2](https://nodejs.org/en/download/) select the ARM v6 tarball. I usually select the link in my browser and then use wget in an ssh terminal.
  * Create a folder for your project somewhere. I created a `node-unicorn` folder on my home directory: `mkdir node-unicorn`
  * In that directory create a new NodeJS project with the command `npm init`. Press `enter` for all the questions and this will create a `package.json` for you.
  * Install the main module with the command: `npm install node-rpi-ws281x-native --save`
  * Create a file called `index.js` with the following code inside:
    
    
    var NUMBER_OF_LEDS = 32; // 32 leds in the Unicorn pHat
    
    var strip = require('rpi-ws281x-native');
    strip.init(NUMBER_OF_LEDS);
    strip.setBrightness(50); // A value between 0 and 255
    
    // The RGB colours of the LEDs. for instance 0xff0000 is red, 0x0000ff is blue, etc.
    var leds = [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0    
    ];
    
    // Loop every 0.1 sec: randomise an index and a colour and display it
    strip.render(leds);
    var interval = setInterval(function() {
        var randomIndex = Math.floor(Math.random() * NUMBER_OF_LEDS);
        var randomColour = Math.floor(Math.random() * 0xffffff);
        leds[randomIndex] = randomColour;
        console.log('Rendering colour ' + randomColour + ' at index ' + randomIndex);
        strip.render(leds);
    }, 100);
    
    // After 10 secondes, stop.
    setTimeout(function () {
        console.log('Stop!');
        clearInterval(interval);
        strip.reset();
    }, 10000);

  * Exactly as the Python library, you need to execute this code as root using: `sudo node index.js`
  * For 10 seconds, every tenth of a second, the programm will pick a random LED and assign a random colour to it.

I know the library is lacking the nice `set_pixel(x, y, r, g, b)` and all the other high level functions. But it is not that hard to implement.

Now I'm trying to find how I could use this for a real life application :-D

  


NUMBER_OF_LEDS = ; strip = (); strip.init(NUMBER_OF_LEDS); strip.setBrightness(); leds = [ ,,,,,,,, ,,,,,,,, ,,,,,,,, ,,,,,,, ]; strip.render(leds); interval = setInterval({ randomIndex = .floor(.random() * NUMBER_OF_LEDS); randomColour = .floor(.random() * ); leds[randomIndex] = randomColour; .log( + randomColour + + randomIndex); strip.render(leds); }, ); setTimeout({ .log(); clearInterval(interval); strip.reset(); }, );
