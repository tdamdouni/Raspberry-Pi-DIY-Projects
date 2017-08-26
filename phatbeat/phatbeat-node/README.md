# phatbeat-node

This package provides basic support for the [Pimoroni pHAT BEAT](https://shop.pimoroni.com/products/phat-beat) device via Node.js. It gives control over the LEDs and buttons included on the pHAT BEAT device.

### Installing

Using [npm](https://www.npmjs.com/):

    $ npm install --save phatbeat

### Usage

There are currently two main areas of functionality available; LED control and button monitoring.

#### Button Monitoring

Buttons are made monitorable by utilising a readable stream within node. The buttons are initialised using the GPIO pin number (the rpio library uses the physical GPIO numbering system rather than the BCM). To make this easier, an array containing pin number against physical button is accessible:

```javascript
let phatbeat = require('phatbeat');
let buttons = phatbeat.getButtonPins();
console.log(buttons);
/*
[ { pin: 29, name: 'FAST_FORWARD' },
  { pin: 31, name: 'PLAY_PAUSE' },
  { pin: 33, name: 'REWIND' },
  { pin: 36, name: 'VOL_UP' },
  { pin: 37, name: 'VOL_DOWN' },
  { pin: 32, name: 'POWER' } ]
*/
```

To initialise and attach to a button stream:

```javascript
let phatbeat = require('phatbeat');
//this attaches the monitoring to the underlying GPIO pin
let fastForwardStream = phatbeat.ButtonStream(29);
```
You are able to either consume the underlying stream directly or attach to events specifically.

##### Stream Based

```javascript
//this example will instantly pipe out the results of the stream to the terminal window.
//the format will be pin number, state (29,1). the state will either be 1 (pressed) or 0 (released)
fastForwardStream.pipe(process.stdout)
```

##### Event Based

```javascript
//Three events are exposed and are emitted whenever an underlying state change is detected
fastForwardSteam.on("pinChange", function(pin, pinState){
    //pin is the pin number that has triggered the event
    //pin state is either 1 (pressed) or 0 (released)
});

fastForwardSteam.on("monitoring", function(pin){
    //pin is the pin number that has been attached for monitoring
});

fastForwardSteam.on("end", function(pin){
    //pin is the pin number that has been attached for monitoring
});
```

As the readable streams are only consumable as a stream, in order to 'detach' the events, clean up the GPIO connection and release the pin from monitoring (as well as trigging the 'end' event), the initialised button can be held for over 5 seconds and then released. This may well be changed to something more accessible and obvious in future!

#### LED Control

Each LED on the 8x2 array is able to be controlled individually and can have its colour changed independently. In order to start controlling the LEDs, they need to be initialised and the GPIO connections set up:

````javascript
let phatbeat = require('phatbeat');
//the init_led function sets up the appropriate GPIO pins
//optional parameter of brightness of leds, this is a decimal between 0.1 and 1.0
phatbeat.init_led(0.8);
````

Once initialised, you have a number of options available to control the LEDs:

````javascript
//changes every LED to the same colour / settings
//method signature takes in RGB colour values
//boolean paramter states whether or not the changes made should be redrawn immediately or staged
//final parameter is optional for new brightness value, the previous value will be retained if not
phatbeat.changeAllLEDs(255, 0, 0, true, 0.8)


//changes single LED by array index to the provide settings
//method signature takes in index of the LED to change (0-15)
//RGB colour values
//boolean paramter states whether or not the changes made should be redrawn immediately or staged
//final parameter is optional for new brightness value, the previous value will be retained if not
phatbeat.changeSingleLED(7, 255, 0, 0, true, 0.8)


//changes all LEDs in the specified channel
//method signature takes in RGB colour values
//int value of the channel to change the LEDs in (0, 1)
//boolean paramter states whether or not the changes made should be redrawn immediately or staged
//final parameter is optional for new brightness value, the previous value will be retained if not
phatbeat.changeAllChannelLEDs(255, 0, 0, 1, true, 0.8);


//writes the current value of the staged LED array to the GPIO pins for display
//this command is called automatically if the 'redraw' boolean is passed the change methods
phatbeat.redraw()


//sets all LEDs to 'off'
//optional parameter of whether to redraw the changes instantly or to be staged, default is to stage
phatbeat.turnOffAllLEDs(true);


//cleanly disconnects the GPIO pins used
//note: this only detaches the LEDs pins, the state of the LEDs will remain as per last redraw
module.exports.teardown = teardown;
````

### Dependencies

- rpio

This is the core package used to communicate directly with the pHAT BEAT over the GPIO pins. In testing, this was the fastest performing of the existing GPIO npm packages which I tried out. This was essential for being able to quickly toggle the LEDs etc. Other packages had responses around 1000ms to issue a command via the GPIO pins whereas this package seems to be able to toggle an LED on and then back off within 100ms (see 'scroll' example) on my Raspberry Pi Zero W.

### Dev Dependencies

- express
- fs
- path
- babel-cli
- babel-present-env
- jest

Half are used purely in the examples to show the possible functionality, others used for package setup.

### Examples

- **button_events**

An example showing the event based control of the hardware buttons.

- **button_stream**

An example showing the direct readable consumption of the button stream.

- **button-web**

An example showing writing events from the button stream out to a webpage for monitoring, control etc.

- **led_control**

A form to show that the LEDs can be controlled via a web portal.

- **scroll**

A simple test to show the speed at which LED states can be altered, it seems to be able to consistantly issue a LED on / LED off toggle within a 100ms window. Due to the way that the LEDs are changed via the pHATBEAT (all LED statuses are written via the data pin for every operation), this is fundamentally the same as being able to change the status of every LED to a different colour and off again (or to a different colour) within this 100ms period.

### Tests

#### Automated Testing

As almost all of the functionality of the code is based on hardware dependencies, the only things that can really be tested are the underlying configuration of what is available on the pHATBEAT. The number of LEDs and buttons are confirmed as matching the current hardware specification (16 LEDs (8 per channel) and 6 hardware buttons).

#### Manual Testing

I have tried out all of the functions on my own [Pirate Radio](https://shop.pimoroni.com/products/pirate-radio-pi-zero-w-project-kit) and it all seems to work fine for me. Any problems, just log an issue on github and I will look into it!

### License

rpio was written by [jperkin](https://github.com/jperkin) which was released under the ISC license. That library has code written by Mike McCauley under the GPL (see the [rpio github page](https://github.com/jperkin/node-rpio) for further details).

The rest of the code is mine and released under the ISC license. It is based upon the Pimoroni [python library](https://github.com/pimoroni/phat-beat) written for the pHAT BEAT device available on their [website](https://shop.pimoroni.com/products/phat-beat).