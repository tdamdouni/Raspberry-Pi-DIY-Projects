'use strict';

/*
 * Verify that add and modify accept all valid event types. See issue #2.
 */
var Epoll = require('../build/Release/epoll').Epoll,
  epoll = new Epoll(function () {}),
  stdin = 0; // fd for stdin

try {
  epoll.add(stdin, Epoll.EPOLLIN).remove(stdin)
    .add(stdin, Epoll.EPOLLOUT).remove(stdin)
    .add(stdin, Epoll.EPOLLRDHUP).remove(stdin)
    .add(stdin, Epoll.EPOLLPRI).remove(stdin)
    .add(stdin, Epoll.EPOLLERR).remove(stdin)
    .add(stdin, Epoll.EPOLLHUP).remove(stdin)
    .add(stdin, Epoll.EPOLLET).remove(stdin)
    .add(stdin, Epoll.EPOLLONESHOT)
    .modify(stdin, Epoll.EPOLLIN)
    .modify(stdin, Epoll.EPOLLOUT)
    .modify(stdin, Epoll.EPOLLRDHUP)
    .modify(stdin, Epoll.EPOLLPRI)
    .modify(stdin, Epoll.EPOLLERR)
    .modify(stdin, Epoll.EPOLLHUP)
    .modify(stdin, Epoll.EPOLLET)
    .modify(stdin, Epoll.EPOLLONESHOT)
    .remove(stdin);
} catch (ex) {
  console.log('*** Error: ' + ex.message);
} finally {
  epoll.close();
}

