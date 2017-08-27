# Raspberry pi, PIR Sensor and Node.js – An IoT Intruder Alert system

_Captured: 2017-08-23 at 22:05 from [thejackalofjavascript.com](http://thejackalofjavascript.com/rpi-pir-sensor-node-iot-intruder-alert/)_

In this post, we will build an Internet of Things Intruder alert system. This system uses a PIR Sensor along with the Raspberry pi. When the PIR Sensor detects a change in a given surrounding, it will trigger the Pi to send out an email to a user with the time of intrusion. Sweet right!

The final system would look like

You can find the completed code [here](https://github.com/arvindr21/pi_intruderAlert).

So, let us get started.

## Prerequisites

If you are new to Raspberry pi and have not yet installed Node.js on it, I would recommend going through [Getting Started with Raspberry pi and Node.js](http://thejackalofjavascript.com/getting-started-raspberry-pi-node-js/).

If you are new to electronics devices and circuits, I would recommend going through the [video lectures](http://www.allaboutcircuits.com/videos/index.html) from All About Circuits.

### Components needed

  1. 1 - Raspberry pi B+
  2. 1 - Breadboard
  3. 1 - PIR Sensor
  4. 9 - Female to Male connectors

If you are new to Raspberry Pi GPIO, please refer [this](http://thejackalofjavascript.com/raspberry-pi-node-js-led-emit-morse-code/#gpio).

## Building the IoT Intruder Detection System

The Intruder system we are going to build will have 2 parts to it.

  1. Hardware - Circuit
  2. Software - Pi Program

We will start off with building the circuit. Once that is done, we will work on the Node.js program.

### Hardware - Circuit

Before we start off we will understand what a Passive InfraRed sensor is.

> PIR sensors allow you to sense motion, almost always used to detect whether a human has moved in or out of the sensors range. They are small, inexpensive, low-power, easy to use and don't wear out. For that reason they are commonly found in appliances and gadgets used in homes or businesses. They are often referred to as PIR, "Passive Infrared", "Pyroelectric", or "IR motion" sensors.

A PIR sensor would look like

If you open the top white color lens-dome, it would look like

> The PIR sensor itself has two slots in it, each slot is made of a special material that is sensitive to IR. The lens used here is not really doing much and so we see that the two slots can 'see' out past some distance (basically the sensitivity of the sensor). When the sensor is idle, both slots detect the same amount of IR, the ambient amount radiated from the room or walls or outdoors. When a warm body like a human or animal passes by, it first intercepts one half of the PIR sensor, which causes a_ positive differential_ change between the two halves. When the warm body leaves the sensing area, the reverse happens, whereby the sensor generates a negative differential change. These change pulses are what is detected.

The above images and text are taken from the [Adafruit](http://www.adafruit.com/) website. You can know more about PIR sensor from their [website](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview).

Now that we have a decent idea on what a PIR sensor is and how it works, we will quickly assemble a circuit.

The logic is pretty simple. The PIR sensor positive pin is connected to Pin 1 (5v) of the pi and then the negative pin to the ground on Pin 5. The Digital out pin is connected to GPIO pin 17. This pin will be set to high, when the PIR sensor detects a change.

Next, a simple buzzer circuit is connected to GPIO pin 18 and ground. The complete circuit would look like

When we receive a high on Pin 17, we trigger the buzzer and send an email with the help of Node.js. Pretty simple!

### Software - Pi program

Now, we will write the Node code to read the output from PIR sensor and control the buzzer.

Login to your pi via ssh - terminal/putty. As soon as you ssh into pi, you will be landing inside the _/home/pi_ folder. We will create a new folder here named _node_programs._ And inside this folder, we will be maintaining all our programs. Run

To step inside that folder, run

For this post, we will create a new folder named _intruderDetection_ and will step inside this folder. Run

mkdir intruderDetection && cd intruderDetection

Note : You can run multiple commands separated by a _&&._

First we will initialize a new node project here. Run

Fill it up as applicable.

Now, we will use a node module named _[onoff](https://www.npmjs.org/package/onoff)_ to interact with the GPIO pins from inside our Node.js code. This is the simplest way to interact with the pi from our node program. Run

npm install onoff --save

We will add another node.js module named [nodemailer](http://www.nodemailer.com/). This module will be used to send out emails when there is an intrusion. Run

npm install nodemailer --save

Next, we will create a new file named _index.js._ And we will open the same in the nano editor. Run

nano index.js

Paste the below code into the nano editor

12345678910111213141516171819 
var Gpio = require('onoff').Gpio,buzzer = new Gpio(18, 'out'),pir = new Gpio(17, 'in', 'both');pir.watch(function(err, value) {if (err) exit();buzzer.writeSync(value);console.log('Intruder detected');if(value == 1) require('./mailer').sendEmail();});console.log('Pi Bot deployed successfully!');console.log('Guarding the Magic pencil...');function exit() {buzzer.unexport();pir.unexport();process.exit();}

**Things to notice**

**Line 2** : We register GPIO pin 18 as output pin. This will be the trigger for the buzzer.

**Line 3** : we register GPIO pin 17 as input pin. This will be triggered when the PIR digital out send a high signal

**Line 5** : We watch for changes in the PIR sensor digital pin. Then we write the value to the buzzer. The value we get for the first time is 1, which will last for ~1 second. Then another signal of 0 would be dispatched. This is typically a ~1 second pulse.

**Line 9 :** We trigger the mailer module and send the email. (_Which we will create next_)

**Line 15** : Has the code for a clean exit.

Let us save the file now. To save the program, press (ctrl+x). This will ask you to save the file. Press Y and press enter key to complete the operation.

Next, we will create the mailer module. Run

And update _mailer.js _as below

**Things to notice**

**Line 1** : We require nodemailer module

**Line 3** : We register a new transporter. You can check out nodemailer to find out more about it

**Line 14** : We add a timer, so that an email is not triggered within 10 seconds. You can customize this on line 19.

**Line 23** : We build the mailOptions object.

**Line 30** : We send the email.

Save the program by pressing (ctrl+x), then Y and press enter key to complete the operation.

Let us run the program now. Execute

sudo node index.js

And now when you move your hand in front of the sensor, it should trigger the buzzer and then send an email.

Simple and Easy! An IoT intruder alert system that sends you an email when it detects something!

Thanks for reading! Do comment.  
@arvindr21
