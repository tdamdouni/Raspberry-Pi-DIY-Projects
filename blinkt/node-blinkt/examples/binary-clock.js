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

var blinkt = require('../src/blinkt');

blinkt.setClearOnExit();

var MODE_HOUR = 0;
var MODE_MIN = 1;
var MODE_SEC = 2;

var mode = 0;
var timeInMode = 0;
var timeToStayInMode = 3;

var lh = 0;
var lm = 0;

setInterval(function() {
  var t = new Date();
  var h = t.getHours();
  var m = t.getMinutes();
  var s = t.getSeconds();
  var b, bit, g, i, r;

  console.log([ h, m, s, mode, timeInMode ]);

  if (h !== lh) {
    mode = MODE_HOUR;
    timeInMode = 0;
  } else if (m !== lm) {
    mode = MODE_MIN;
    timeInMode = 0;
  }

  lm = m;
  lh = h;

  blinkt.clear();

  if ((s % 2) === 0) {
    blinkt.setPixel(1, 64, 64, 64);
  }

  if (mode === MODE_HOUR) {
    blinkt.setPixel(0, 255, 0, 0);

    for (i = 0; i < 6; i++) {
      bit = (h & (1 << i)) > 0;
      r = 128 * bit;
      g = 128 * bit;
      b = 128 * bit;

      blinkt.setPixel(7 - i, r, g, b);
    }
  }

  if (mode === MODE_MIN) {
    blinkt.setPixel(0, 0, 255, 0);

    for (i = 0; i < 6; i++) {
      bit = (m & (1 << i)) > 0;
      r = 128 * bit;
      g = 128 * bit;
      b = 128 * bit;

      blinkt.setPixel(7 - i, r, g, b);
    }
  }

  if (mode === MODE_SEC) {
    blinkt.setPixel(0, 0, 0, 255);

    for (i = 0; i < 6; i++) {
      bit = (s & (1 << i)) > 0;
      r = 128 * bit;
      g = 128 * bit;
      b = 128 * bit;

      blinkt.setPixel(7 - i, r, g, b);
    }
  }

  blinkt.show();

  timeInMode += 1;

  if (timeInMode === timeToStayInMode) {
    mode += 1;
    mode %= 3;
    timeInMode = 0;
  }
}, 1000);
