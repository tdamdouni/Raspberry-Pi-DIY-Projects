# Raspberry pi, a Buzzer and Node.js – An IoT Doorbell

_Captured: 2017-08-23 at 22:04 from [thejackalofjavascript.com](http://thejackalofjavascript.com/rpi-buzzer-node-iot-doorbell/)_

In this post, we will build an embedded system - A Doorbell, with Raspberry pi B+, A Buzzer and Node.js. This embedded system will act as both a normal Doorbell with a button switch and the same doorbell can be controlled over internet. Simple right?

The final output of this embedded system would look like

The completed code can be found [here](https://github.com/arvindr21/pi_DoorBell).

So, let us get started.

## Prerequisites

If you are new to Raspberry pi and have not yet installed Node.js on it, I would recommend going through [Getting Started with Raspberry pi and Node.js](http://thejackalofjavascript.com/getting-started-raspberry-pi-node-js/).

If you are new to electronics devices and circuits, I would recommend going through the [video lectures](http://www.allaboutcircuits.com/videos/index.html) from All About Circuits.

### Components needed

  1. 1 - Raspberry pi B+
  2. 1 - Breadboard
  3. 1 - 68 Ohms resistor
  4. 1 - 10K Ohm resistor
  5. 1 - LED (optional)
  6. 1 - Toggle Button
  7. 4 - Female to Male connectors
  8. 5 - Male to Male connectors
  9. 1 - Piezo Buzzer

If you are new to Raspberry Pi GPIO, please refer [this](http://thejackalofjavascript.com/raspberry-pi-node-js-led-emit-morse-code/#gpio).

## Building the IoT Doorbell

There are 3 pieces involved in building the complete system.

  1. Hardware - Circuit
  2. Software - Pi program
  3. Software - A Client that can remotely control the Pi

We will start off with building the circuit. The circuit will consist of a Buzzer and a button switch hooked up with the pi. Once that is done, we will write the Node.js program that will listen to the button for changes and then trigger the Buzzer.

Now, to control the buzzer remotely, we will write a simple HTTP server on the pi, that will toggle the buzzer when it receives a HTTP request.

### Hardware - Circuit

Before we get started off we will take a look at what are Pull-up/Pull-down resistors.

When you are dealing with digital components, they either have an ON/HIGH state or a OFF/LOW state. But in a switch, they have another state called as a Floating state. This state sometimes triggers a false ON state or a false OFF state, depending on the circuit. To avoid this erroneous reading, we introduce a Pull-up/Pull-down resistors.

You can know more about Pull-up/Pull-down resistors in this video

In our circuit we will include a pull-down resistor of 10K ohms value. Below is the circuit diagram, that we are going to set up on the breadboard.

The red wire on the top left will be connected to Pin 1 on the Raspberry Pi (_Info on GPIO pins [here](http://thejackalofjavascript.com/raspberry-pi-node-js-led-emit-morse-code/#gpio)_). And Pin 5 will be connected to the black wire that would be our ground. This setup makes the first 1 row of the breadboard a power bus and the second row a ground bus. From now on, we will connect our components to these rows as applicable.

Next, we will work on the Buzzer circuit. The buzzer circuit is pretty simple. We will start off with the out from GPIO pin 17 to the breadboard. This is connected to a 68 ohms resistor. This resistor is then connected to the buzzer's positive end. And the negative end is grounded.

Finally our button switch setup. Before we do that, lets take a quick look at how the switch works

When the button is open, the two leads on each side are connected. And when the button is closed, all 4 leads are connected. You can find more info on the button switch [here](http://mbeded.blogspot.in/2012/04/4-legged-push-button-working.html).

Here is where the pull down resistor comes into picture. When the switch is open, there is some floating current between the 2 leads. When this is connected to the pi to complete the circuit, the GPIO pin reads random high and low values.

To complete the button circuit, we will take one end of the button and connect it with the 5v supply. That is row 1 in the breadboard. And the other leg on the same side will be connected to a 10K Ohm pull down resistor. And that would be connected to the Ground, row 2 of breadboard.

The other side of the push button, will be connect to GPIO pin 18 on the pi. So when the button is pressed, A high signal will be sent to to pin 18 and this will be used to trigger the buzzer.

If you want to check the current flow, you can add a LED between the buzzer and the ground like

Simple right? This completes the circuit part.

### Software - Pi program

Now, we will write the Node code to control the buzzer, based on the inputs from the button switch.

Login to your pi via ssh - terminal/putty. As soon as you ssh into pi, you will be landing inside the _/home/pi_ folder. We will create a new folder here named _node_programs._ And inside this folder, we will be maintaining all our programs. Run

To step inside that folder, run

For this post, we will create a new folder named _doorBell _and will step inside this folder. Run

mkdir doorBell && cd doorBell

Note : You can run multiple commands separated by a _&&._

First we will initialize a new node project here. Run

Fill it up as applicable.

Now, we will use a node module named _[onoff](https://www.npmjs.org/package/onoff)_ to interact with the GPIO pins from inside our Node.js code. This is the simplest way to interact with the pi from our node program. Run

npm install onoff --save

Next, we will create a new file named _index.js._ And we will open the same in the nano editor. Run

nano index.js

Paste the below code into the nano editor

12345678910111213141516 
var Gpio = require('onoff').Gpio,buzzer = new Gpio(17, 'out'),button = new Gpio(18, 'in', 'both');button.watch(function(err, value) {if (err) exit();buzzer.writeSync(value);});function exit() {buzzer.unexport();button.unexport();process.exit();}process.on('SIGINT', exit);

#### Things to Notice

**Line 2** : We mark GPIO pin 17 as an output - this is our Buzzer

**Line 3** : We mark GPIO pin 18 as an input - this is our Button Switch

**Line 5** : We watch for changes in the button. If the button is pressed, the value will be 1. The same will be set as the output of the buzzer. And when release, the value will be 0.

**Line 10** : The logic for a clean exit.

Let us save the file and run the program. To save the program, press (ctrl+x). This will ask you to save the file. Press Y and press enter key to complete the operation.

To run the program, execute

sudo node index.js

Now, when you press the button, the buzzer will "buzz". If you added an LED, it will blink too.

Simple and easy right!

Taking this to the next level, we control this buzzer over the internet.

### Software - A Client that can remotely control the Pi

Imagine this, you have parked your car in the cellar and by the time you reach your home on the top floor, your main door is open for you! How about that?

We can achieve this sweet feature by connecting our Doorbell to the internet, say with the pi. And using an App on your phone, you will trigger the doorbell, when you are parking your car in the cellar. And bam!! by the time you reach your home, the door is open. (_Don't ask me, what happens if no one is at home_)

Let us add that piece of functionality to the code. For that we will create a simple HTTP Server with Node.js. And expose the URL to our app. And now, our App can control the Doorbell!.

So, let us get started. Inside the _doorBell_ folder, create another file named _server.js_.

nano server.js

Paste the below code into it

1234567891011121314151617181920212223242526272829303132333435363738 
var http = require("http"),port = 8088;module.exports = function(buzzer) {var server = http.createServer(function(request, response) {if (request.url === '/trigger' && request.method == 'GET') {// turn on the buzzer buzzer.writeSync(1);// turn off the buzzer after 2 secondssetTimeout(function() {buzzer.writeSync(0);}, 2000);response.writeHeader(200, {"Content-Type": "application/json","Access-Control-Allow-Origin": "*"});response.write('{ "status": true }');response.end();} else {response.writeHeader(200, {"Content-Type": "application/json","Access-Control-Allow-Origin": "*"});response.write('{ "status": true }');response.end();}});server.listen(port);console.log("Server Running on " \+ port + ".\nLaunch http://localhost:" \+ port);return server;}

This is a very light weight Node.js HTTP server. On Line 17, we check the URL and Method. If they match our criterion, we will trigger the buzzer, wait for 2 seconds and turn it off. And then we send back a success to the client.

And if the URL and Method do not match, we will reply back with a status false.

Finally, we will include this logic in _index.js_

12345678910111213141516171819 
var Gpio = require('onoff').Gpio,buzzer = new Gpio(17, 'out'),button = new Gpio(18, 'in', 'both');// start the servervar server = require('./server')(buzzer);button.watch(function(err, value) {if (err) exit();buzzer.writeSync(value);});function exit() {buzzer.unexport();button.unexport();process.exit();}process.on('SIGINT', exit);

Do notice Line 6.

That is it, restart the program by running

sudo node index.js

And you should see the console log. But there is a small issue here. Our server is on localhost and only the devices that are connected to the same network can access the pi. This is not really "IoT".

So, let us expose our localhost as a publicly accessible URL. For that we will use [ngrok](https://ngrok.com/). To set up ngrok on our pi, grab the download link from the homepage corresponding to **Linux/ARM**. And then you can run a wget.

For that let us CD back to the _/home/pi_ folder and create a new folder named _ngrok._

cd /home/pi && mkdir ngrok && cd ngrok

Then from inside the _ngrok_ folder, run

wget https://api.equinox.io/1/Applications/ap_pJSFC5wQYkAyI0FIVwKYs9h1hW/Updates/Asset/ngrok.zip?os=linux&arch=arm&channel=stable -O ngrok.zip

This will take a few minutes, please be patient. Once the download is completed, we will unzip it. Run

unzip ngrok.zip

Note : If you have issues download with wget, you can use the Pi's GUI with VNC and then download it from the website.

Now, that is done, we will restart the node server. Run

sudo node index.js

Open a **new** terminal/putty into the Pi and cd into the _ngrok_ folder. And from there run

8088 is the port number we have used in _server.js_. This will give you a public URL. You can use either the http or https version. Open a browser on your computer and navigate to http://41b9687d.ngrok.com/trigger where http://41b9687d.ngrok.com needs to be replaced with your ngrok URL.

If everything is okay, as soon as you fire the request, your buzzer will be "buzzing". Awesome right!

To give a decent interface, we will create a file named _index.html _anywhere on our computer. This will be like our "app", but inside a browser. Update _index.html_ as below

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647 
<!DOCTYPE html><html lang=""><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Doorbell</title><!-- Bootstrap CSS --><link href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet"><!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries --><!-- WARNING: Respond.js doesn't work if you view the page via file:// --><!--[if lt IE 9]><script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script><script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script><![endif]--></head><body><h1 class="text-center">Trigger Doorbell</h1><br/><br/><div class="container"><div class="col-md-12"><button type="button" class="btn btn-primary btn-block">Trigger</button></div></div><!-- jQuery --><script src="http://code.jquery.com/jquery.js"></script><!-- Bootstrap JavaScript --><script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script><script type="text/javascript">$(function() {$('button').on('click', function() {$('button').prop('disabled', true).text('Trigerring');$.get('http://41b9687d.ngrok.com/trigger', function(data) {$('button').prop('disabled', false).text('Trigger');});});})</script></body></html>

If you have a WAMP, LAMP, MAMP or XAMPP server, host this file in the _htdocs/www_ folder. Or if you have python installed on your machine, you can simply run python -m SimpleHTTPServer or python -m http.server.

What ever way you host this web page, you should have a URL that looks like http://localhost:8000. That will dispatch the _index.html_ page.

Now from here if you click on _Trigger_ button, the buzzer should go off. Sweet and simple IoT Doorbell.

You can use the same circuit and logic with a simple LED in place of the buzzer. To toggle your porch light or the hallway. Here is a quick example.

If you checked out my other post [Raspberry Pi, Node.js and a LED - Emit Morse Code](http://thejackalofjavascript.com/raspberry-pi-node-js-led-emit-morse-code/), where we emit morse code with the help of a LED. We can extend that example to use a buzzer to emit a sound as well. The code is same as the LED, except we replace the LED with the buzzer. Take a look

That was the famous SOS message. Simple right!

Hope this post gave you a basic idea on reading inputs from components and performing actions based on it. And how easily you can convert any pi component to an "Internet Thingy"

Thanks for reading! Do comment.  
@arvindr21
