'use strict';

/*
 * Make sure the process terminates when epoll is used and 'nothing' is
 * actually done. The epoll addon calls uv_ref and uv_unref to keep nodes
 * event loop alive. Here we make sure that the addon isn't keeping the event
 * loop alive unnecessarily long. If the process terminates, everything is ok.
 * If it hangs, there is a problem.
 */
var Epoll = require('../build/Release/epoll').Epoll,
  epoll0 = new Epoll(function () {}),
  epoll1 = new Epoll(function () {});

