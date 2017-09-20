'use strict';

/*
 * This test resulted in a segmentation fault in epoll v0.0.6. See issue #5.
 *
 * There were Ref/Unref issues in the epoll addon which resulted in epoll
 * instances being garbage collected while still in use.
 *
 * This test expects a newline as input on stdin. It should be piped in for
 * for best results:
 * echo | node no-gc-allowed
 */
var Epoll = require('../build/Release/epoll').Epoll;
var time = process.hrtime();
var stdin = 0; // fd for stdin 
var poller = new Epoll(function () {
  var timeSoFar = process.hrtime(time);
  if (timeSoFar[0] > 5) {
    // BB faults in ~2.5s, Pi faults in ~?s, so wait about 5s.
    // In order for the segfault to occur, V8 can't have anymore required
    // references to poller. If process.exit(0) is replaced with
    // poller.remove(0).close(), there will be a required reference, poller
    // won't be garbage collected, and there will be no segfault.
    process.exit(0);
  }
});

poller.add(stdin, Epoll.EPOLLIN);

