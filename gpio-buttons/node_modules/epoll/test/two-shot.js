'use strict';

/*
 * Make sure two EPOLLONESHOT events can be handled.
 *
 * This test expects a newline as input on stdin.
 */
var Epoll = require('../build/Release/epoll').Epoll,
  util = require('./util'),
  eventCount = 0,
  epoll,
  stdin = 0; // fd for stdin

epoll = new Epoll(function (err, fd, events) {
  eventCount += 1;

  if (eventCount === 1) {
    setTimeout(function () {
      epoll.modify(fd, Epoll.EPOLLIN | Epoll.EPOLLONESHOT);
    }, 100);
  } else if (eventCount === 2) {
    setTimeout(function () {
      util.read(fd); // read stdin (the newline)
      epoll.remove(fd).close();
    }, 100);
  } else {
    console.log('*** Error: unexpected event');
  }
});

epoll.add(stdin, Epoll.EPOLLIN | Epoll.EPOLLONESHOT);

