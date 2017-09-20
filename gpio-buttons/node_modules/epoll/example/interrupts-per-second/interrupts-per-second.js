'use strict';

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

  count += 1;

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

