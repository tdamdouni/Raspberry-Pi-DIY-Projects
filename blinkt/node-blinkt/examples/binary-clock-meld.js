#!/usr/bin/env node

/*
 * Copyright (C) 2017 Alasdair Mercer, !ninja
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

'use strict';

var util = require('util');

var blinkt = require('../src/blinkt');

console.log('Hour = Red, Minute = Green, Second = Blue');

blinkt.setClearOnExit();
blinkt.setBrightness(0.2);

var onValue = 64;

setInterval(function() {
  var t = new Date();
  var h = t.getHours();
  var m = t.getMinutes();
  var s = t.getSeconds();
  var b, bitH, bitM, bitS, g, r;

  console.log(util.format('%d:%d:%d', h, m, s));

  blinkt.clear();

  // Blink LED 0
  var c = onValue * (s % 2);

  blinkt.setPixel(0, c, c, c);

  for (var i = 0; i < 6; i++) {
    // Grab the n'th bit from hour, min and second
    bitH = (h & (1 << i)) > 0;
    bitM = (m & (1 << i)) > 0;
    bitS = (s & (1 << i)) > 0;

    r = Math.floor(bitH * onValue);
    g = Math.floor(bitM * onValue);
    b = Math.floor(bitS * onValue);

    blinkt.setPixel(7 - i, r, g, b);
  }

  blinkt.show();
}, 1000);
