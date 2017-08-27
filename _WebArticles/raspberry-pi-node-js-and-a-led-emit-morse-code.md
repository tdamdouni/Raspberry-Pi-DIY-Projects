# Raspberry Pi, Node.js and a LED – Emit Morse Code

_Captured: 2017-08-23 at 22:03 from [thejackalofjavascript.com](http://thejackalofjavascript.com/raspberry-pi-node-js-led-emit-morse-code/)_

In this post, we will get our hands a bit dirty with Raspberry Pi, Node.js and a LED. We will be writing a simple program in Node.js to turn a LED on and off. Then we will extend this logic to build a simple piece of embedded system that can take a piece of string and emit its morse code.

Interesting right? Below is a quick video as what we will be building

The above LED is emitting the Morse code for SOS. That is (… ___ …) [Dot Dot Dot, Dash Dash Dash, Dot Dot Dot]. Nice right?

You can get the completed code [here](https://github.com/arvindr21/Pi_MorseCode).

So, let us get started.

## Prerequsites

If you are new to Raspberry pi and have not yet installed Node.js on it, I would recommend going through [Getting Started with Raspberry pi and Node.js](http://thejackalofjavascript.com/getting-started-raspberry-pi-node-js/).

If you are new to electronics devices and circuits, I would recommend going through the [video lectures](http://www.allaboutcircuits.com/videos/index.html) from All About Circuits.

### Components needed

  1. 1 - Raspberry pi B+
  2. 1 - Breadboard
  3. 1 - 68 Ohms resistor
  4. 1 - LED
  5. 2 - Female to male wires

## What is GPIO?

GPIO stands for General Purpose Input Output pins.

> These pins are a physical interface between the Pi and the outside world. At the simplest level, you can think of them as switches that you can turn on or off (input) or that the Pi can turn on or off (output).
> 
> Inputs don't have to come from a physical switch; it could be input from a sensor or a signal from another computer or device, for example. The output can also do anything, from turning on an LED to sending a signal or data to another device. If the Raspberry Pi is on a network, you can control devices that are attached to it from anywhere** and those devices can send data back.

You can read more about Raspberry Pi GPIO [here](http://www.raspberrypi.org/documentation/usage/gpio/).

Raspberry pi B+ has 26 GPIO pins.

The remaining ones are either power or ground pins.

Below is the superimposed image of the pin layout on a pi

## Turn On Turn Off

Now that we have a basic understanding of GPIO, we will leverage one of pi's GPIO pins to turn a LED on and off.

There are 2 parts to getting this task done. Part 1 is building a circuit that has a LED connected to the pi. Part 2 is the Javascript code that triggers the state of the LED.

So, let us focus on Part I. We will build the circuit. For this we will assemble the following schematic on a breadboard.

The left end of the above circuit will be connected to Pin 9 - GND pin of pi (Left Column, 5th pin). And the right end of the above circuit will be connected to Pin 11(Left Column, 6th pin).

This completes our circuit. Now to the application logic. Connect the pi to your computer. And ssh from terminal/putty into pi. We will be using command line to tools to write the code.

So, as soon as you ssh into pi, you will be landing inside the _/home/pi_ folder. We will create a new folder here named _node_programs._ And inside this folder, we will be maintaining all our programs. Run

To step inside that folder, run

For this post, we will create a new folder named _ledBlink _and will step inside this folder. Run

mkdir ledBlink && cd ledBlink

Note : You can run multiple commands separated by a _&&. _

First we will initialize a new node project here. Run

Fill it up as applicable.

Now, we will use a node module named _[onoff](https://www.npmjs.org/package/onoff)_ to interact with the GPIO pins from inside our Node.js code. This is the simplest way to interact with the pi from our node program. Run

npm install onoff --save

Next, we will create a new file named _index.js_ inside the _ledBlink_ folder. To create a new file, you can follow any of the 2 ways. First

touch index.js

This will create an empty file named _index.js_. Second

nano index.js

This will create a new file named _index.js_ and will open the file for editing in the built in nano editor. Even though you are following the first approach, to edit the file, you need to run step 2.

Once the file is opened in the nano editor, paste the below.

12345678910111213 
var Gpio = require('onoff').Gpio,led = new Gpio(17, 'out');var iv = setInterval(function(){led.writeSync(led.readSync() === 0 ? 1 : 0)}, 500);// Stop blinking the LED and turn it off after 5 seconds.setTimeout(function() {clearInterval(iv); // Stop blinkingled.writeSync(0); // Turn LED off.led.unexport(); // Unexport GPIO and free resources}, 5000);

**Things to notice**

**Line 1** : We include the GPIO module of _onoff_ to interact with pi's GPIO pins

**Line 2** : We tell our program that we are going to use a GPIO pin and it is of the type output. That is pi provides the input to that pin based on the logic we write. We will name the output of this pin as led, as logically we have a led placed here.

**Line 4** : We start a new setInterval() to run the code inside it every 500 milliseconds.

**Line 5** : For every Gpio pin, we have a method named writeSync(). This method takes in a 1 or a 0. If it is 1, it will command the pi to supply 3.3v to this pin and if it is 0, it will command the pi to stop the supply. This way, we control the pin.

And led.readSync() tells us if this pin is in state 1 or 0. depending on that, we will toggle the values. That is if the value is 0, we set the value to 1 and if 1, we set the value to 0. Thus making the LED "blink" every 500ms. Simple right?

**Line 13** : After 5 seconds, we terminate the setInterval() and clear the state of the pin and release all the resources.

Let us save the file and run the program. To save the program, press (ctrl+x or cmd+x). This will ask you to save the file. Press Y and press enter key to complete the operation.

To run the program, execute

sudo node index.js

And you should see the LED blinking for 5 seconds before the program exits. Simple right. Now you can see the power of pi. How it can interact with the outside world and control stuff.

## Morse Code

> **Morse code** is a method of transmitting text information as a series of on-off tones, lights, or clicks that can be directly understood by a skilled listener or observer without special equipment.

If you are new to Morse code, checkout [learnmorsecode.com](http://www.learnmorsecode.com/).

This is how you read the above diagram

> Place your pencil where it says START and listen to morse code.  
Move down and to the right every time you hear a DIT (a dot).  
Move down and to the left every time you hear a DAH (a dash).

So this will create a unique code for each of the alphabets, numbers and a few special characters. Like

A simple and efficient language!

Now, we will write a program that will emit the Morse Code for a given string. To keep the blinking at a constant rate and in our control, we will use a node module named sleep. Run

npm install sleep --save

Now, we will create a new file named _morseCode.js,_ inside the _ledBlink_ folder. Run

nano morseCode.js

Now, paste the below code to _morseCode.js_

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687 
var Gpio = require('onoff').Gpio,led = new Gpio(17, 'out'),sleep = require('sleep'),_baseTime = 128000, //micro secondssleepTime = _baseTime,btwCodes = _baseTime * 2,btwLetters = _baseTime * 4,btwWords = _baseTime * 8;var text = (process.argv[2] ? process.argv[2] : '').toLowerCase();var MorseCode = {pattern: {'a': '._','b': '_...','c': '_._.','d': '_..','e': '.','f': '.._.','g': '__.','h': '....','i': '..','j': '.___','k': '_._','l': '._..','m': '__','n': '_.','o': '___','p': '.__.','q': '__._','r': '._.','s': '...','t': '_','u': '.._','v': '..._','w': '.__','x': '_.._','y': '_.__','z': '__..','1': '.____','2': '..___','3': '...__','4': '...._','5': '.....','6': '_....','7': '__...','8': '___..','9': '____.','0': '_____'},active: function(t) {led.writeSync(1);},inactive: function() {led.writeSync(0);}}var _t = text.split('');for(var i = 0; i < _t.length; i++) {var _l = _t[i];if(_l == ' ') { // if the char is a space sleep.usleep(btwWords);}else {var _c = MorseCode.pattern[_l].split('');sleep.usleep(btwLetters);console.log('Letter Starts >> ', _l);for(var j = 0; j < _c.length; j++) {console.log("code >> ", _c[j]);MorseCode.active();if(_c[j] == '.') {sleep.usleep(sleepTime);MorseCode.inactive();sleep.usleep(btwCodes);}else {sleep.usleep(sleepTime * 3);MorseCode.inactive();sleep.usleep(btwCodes);}}}};

**Things to notice**

**Line 1,3** : require node modules

**Line 2** : Declare the pin to be a out.

**Line 4-8** : A base time, based on which the speed of transmission/blinking can be controlled.

_sleepTime_ - Time before which we reset the state of the LED to 0

_btwCodes_ - Time between 2 dits or dahs or a dit and a dah for a given letter.

_btwLetters_ - Time between each letter

_btwWords_ - Time between each word

This way, we can control the speed of transmission/LED blinking.

** Line 11** : We read the text from command line

**Line 14-50** : We build an object with the mapping of character and its morse code.

**Line 53** : A helper function to make the the LED active

**Line 56** : A helper function to make the the LED inactive

**Line 60/61** : We will split the input string and iterate over it

**Line 65/66** : If the current character is a space, we will sleep for " btwWords"

**Line 69** : We split the Morse code for a character and check if it is a dit or a dah.

**Line 76** : If the code is a dit, we sleep for " sleepTime". This is time that the LED stays lit.

**Line 81** : If the code is a dah, we sleep for " sleepTime * 3". This is time that the LED stays lit.

**Line 77/82** : We reset the state of the LED

**Line 78/83** : We wait for " btwCodes" before we start processing the next code.

Simple and easy right! Save the file by pressing ctrl + x and then Y and then enter key.

To run the program execute

sudo node morseCode.js "Hello World"

And you should see the below log in the console.

12345678910111213141516171819202122232425262728293031323334353637383940414243 
pi@raspberrypi ~/node_programs/ledBlink $ sudo node morseCode.js "Hello World"Letter Starts >> hcode >> .code >> .code >> .code >> .Letter Starts >> ecode >> .Letter Starts >> lcode >> .code >> _code >> .code >> .Letter Starts >> lcode >> .code >> _code >> .code >> .Letter Starts >> ocode >> _code >> _code >> _Letter Starts >> wcode >> .code >> _code >> _Letter Starts >> ocode >> _code >> _code >> _Letter Starts >> rcode >> .code >> _code >> .Letter Starts >> lcode >> .code >> _code >> .code >> .Letter Starts >> dcode >> _code >> .code >> .

And the LED will blink according to this.

Below is a recording of the program with "Morse Code" as input

Hope this post gave you a decent idea on GPIO and how you can control them.

Thanks for reading! Do comment.  
@arvindr21
