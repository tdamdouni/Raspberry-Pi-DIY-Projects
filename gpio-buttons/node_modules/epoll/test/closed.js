'use strict';

/*
 *
 */
var Epoll = require('../build/Release/epoll').Epoll,
  assert = require('assert'),
  poller = new Epoll(function () {}),
  stdin = 0;

assert(poller.closed === false);

function closePoller() {
  if (!poller.closed) {
    poller.remove(stdin).close();
  }
}

poller.add(stdin, Epoll.EPOLLIN);

closePoller();
closePoller();

assert(poller.closed === true);

