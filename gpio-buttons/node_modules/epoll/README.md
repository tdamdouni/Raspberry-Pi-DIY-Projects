## epoll

A low-level **Node.js** binding for the Linux epoll API for monitoring multiple
file descriptors to see if I/O is possible on any of them.

This module was initially written to detect EPOLLPRI events indicating that
urgent data is available for reading. EPOLLPRI events are triggered by
interrupt generating [GPIO](https://www.kernel.org/doc/Documentation/gpio/)
pins. The epoll module is used by [onoff](https://github.com/fivdi/onoff)
to detect such interrupts.

## Installation

    $ npm install epoll

If you're using Node.js v4 or higher and seeing lots of compile errors when
installing epoll, it's very likely that gcc/g++ 4.8 or higher are not
installed. See
[Node.js v4 and native addons](https://github.com/fivdi/onoff/wiki/Node.js-v4-and-native-addons)
for details.

If you're using Node.js v0.10.29 on the Raspberry Pi and seeing a compile
error saying that `‘REPLACE_INVALID_UTF8’ is not a member of ‘v8::String’`
see [Node.js v0.10.29 and native addons on the Raspberry Pi](https://github.com/fivdi/onoff/wiki/Node.js-v0.10.29-and-native-addons-on-the-Raspberry-Pi).

If you're using Node.js v0.10.29 on the BeagleBone Black and seeing a compile
error saying that `‘REPLACE_INVALID_UTF8’ is not a member of ‘v8::String’`
see [Node.js v0.10.29 and native addons on the BeagleBone Black](https://github.com/fivdi/onoff/wiki/Node.js-v0.10.29-and-native-addons-on-the-BeagleBone-Black).

## API

  * Epoll(callback) - Constructor. The callback is called when epoll events
    occur and it gets three arguments (err, fd, events).
  * add(fd, events) - Register file descriptor fd for the event types specified
    by events.
  * remove(fd) - Deregister file descriptor fd.
  * modify(fd, events) - Change the event types associated with file descriptor
    fd to those specified by events.
  * close() - Deregisters all file descriptors and free resources.

Event Types

  * Epoll.EPOLLIN
  * Epoll.EPOLLOUT
  * Epoll.EPOLLRDHUP
  * Epoll.EPOLLPRI
  * Epoll.EPOLLERR
  * Epoll.EPOLLHUP
  * Epoll.EPOLLET
  * Epoll.EPOLLONESHOT

Event types can be combined with | when calling add or modify. For example,
Epoll.EPOLLPRI | Epoll.EPOLLONESHOT could be passed to add to detect a single
GPIO interrupt.

## Example - Watching Buttons

The following example shows how epoll can be used to detect interrupts from a
momentary push-button connected to GPIO #4 (pin P1-7) on the Raspberry Pi.
The source code is available in the [example directory]
(https://github.com/fivdi/epoll/tree/master/example/watch-button) and can
easily be modified for using a different GPIO on the Pi or a different platform
such as the BeagleBone.

The first step is to export GPIO #4 as an interrupt generating input using
the export bash script from the examples directory.

    $ [sudo] ./export

export:
```bash
#!/bin/sh
echo 4 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio4/direction
echo both > /sys/class/gpio/gpio4/edge
```

Then run watch-button to be notified every time the button is pressed and
released. If there is no hardware debounce circuit for the push-button, contact
bounce issues are very likely to be visible on the console output.
watch-button terminates automatically after 30 seconds.

    $ [sudo] node watch-button

watch-button:
```js
var Epoll = require('../../build/Release/epoll').Epoll,
  fs = require('fs'),
  valuefd = fs.openSync('/sys/class/gpio/gpio4/value', 'r'),
  buffer = new Buffer(1);

// Create a new Epoll. The callback is the interrupt handler.
var poller = new Epoll(function (err, fd, events) {
  // Read GPIO value file. Reading also clears the interrupt.
  fs.readSync(fd, buffer, 0, 1, 0);
  console.log(buffer.toString() === '1' ? 'released' : 'pressed');
});

// Read the GPIO value file before watching to
// prevent an initial unauthentic interrupt.
fs.readSync(valuefd, buffer, 0, 1, 0);

// Start watching for interrupts.
poller.add(valuefd, Epoll.EPOLLPRI);

// Stop watching after 30 seconds.
setTimeout(function () {
  poller.remove(valuefd).close();
}, 30000);
```

When watch-button has terminated, GPIO #4 can be unexported using the
unexport bash script.

    $ [sudo] ./unexport

unexport:
```bash
#!/bin/sh
echo 4 > /sys/class/gpio/unexport
```

## Example - Interrupts Per Second

The following example shows how epoll can be used to determine the number of
hardware interrupts that can be handled per second on the Raspberry Pi.
The source code is available in the [example directory]
(https://github.com/fivdi/epoll/tree/master/example/interrupts-per-second) and
can easily be modified to use different GPIOs on the Raspberry Pi or a
different platform such as the BeagleBone.

In this example, GPIO #7 is wired to one end of a 1kΩ current limiting
resistor and GPIO #8 is wired to the other end of the resistor. GPIO #7 is an
input and GPIO #8 is an output.

The first step is to export GPIOs #7 and #8 using the export bash script from
the examples directory.

    $ [sudo] ./export

export:
```bash
#!/bin/sh
echo 7 > /sys/class/gpio/export
echo 8 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio7/direction
echo both > /sys/class/gpio/gpio7/edge
echo out > /sys/class/gpio/gpio8/direction
```

Then run interrupts-per-second. interrupts-per-second toggles the state of the
output every time it detects an interrupt on the input. Each toggle will
trigger the next interrupt. After five seconds, interrupts-per-second prints
the number of interrupts it detected per second.

    $ [sudo] node interrupts-per-second

interrupts-per-second:
```js
var Epoll = require('../../build/Release/epoll').Epoll,
  fs = require('fs'),
  inputfd = fs.openSync('/sys/class/gpio/gpio7/value', 'r+'),
  outputfd = fs.openSync('/sys/class/gpio/gpio8/value', 'r+'),
  value = new Buffer(1),  // The three Buffers here are global
  zero = new Buffer('0'), // to improve performance.
  one = new Buffer('1'),
  count = 0,
  time;

// Create a new Epoll. The callback is the interrupt handler.
var poller = new Epoll(function (err, fd, events) {
  var nextValue;

  count++;

  // Read GPIO value file. Reading also clears the interrupt.
  fs.readSync(inputfd, value, 0, 1, 0);

  // Toggle GPIO value. This will eventually result
  // in the next interrupt being triggered.
  nextValue = value[0] === zero[0] ? one : zero;
  fs.writeSync(outputfd, nextValue, 0, nextValue.length, 0);
});

time = process.hrtime(); // Get start time.

// Start watching for interrupts. This will trigger the first interrupt
// as the value file already has data waiting for a read.
poller.add(inputfd, Epoll.EPOLLPRI);

// Print interrupt rate to console after 5 seconds.
setTimeout(function () {
  var rate;

  time = process.hrtime(time); // Get run time.
  rate = Math.floor(count / (time[0] + time[1] / 1E9));
  console.log(rate + ' interrupts per second');

  // Stop watching.
  poller.remove(inputfd).close();
}, 5000);
```

When interrupts-per-second has terminated, GPIOs #7 and #8 can be unexported
using the unexport bash script.

    $ [sudo] ./unexport

unexport:
```bash
#!/bin/sh
echo 7 > /sys/class/gpio/unexport
echo 8 > /sys/class/gpio/unexport
```

Here are some results from the "Interrupts Per Second" example.

**BeagleBone, 720MHz, Ångström v2012.12, Kernel 3.8.13, epoll v0.0.6:**

Node.js | Interrupts / Second
:---: | ---:
v0.11.7 | 7152
v0.10.20 | 5861
v0.8.22 | 6098

**BeagleBone Black, 1GHz, Debian, Kernel 3.8.13, epoll v0.1.11:**

Node.js | Interrupts / Second
:---: | ---:
v0.10.25 | 9133

**Raspberry Pi, 700Mhz, Raspbian, Kernel 3.2.27+, epoll v0.0.6:**

Node.js | Interrupts / Second
:---: | ---:
v0.11.07 | 4071
v0.10.16 | 3530
v0.8.14 | 3591

**Raspberry Pi 2, 900Mhz, Raspbian, Kernel 3.18.5-v7+, epoll v0.1.11:**

Node.js | Interrupts / Second
:---: | ---:
v0.10.36 | 10438

