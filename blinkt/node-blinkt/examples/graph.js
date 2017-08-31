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
blinkt.setBrightness(0.1);

function showGraph(value, red, green, blue) {
  value *= blinkt.NUM_PIXELS;

  for (var i = 0; i < blinkt.NUM_PIXELS; i++) {
    if (value < 0) {
      red = green = blue = 0;
    } else {
      red = Math.floor(Math.min(value, 1) * red);
      green = Math.floor(Math.min(value, 1) * green);
      blue = Math.floor(Math.min(value, 1) * blue);
    }

    blinkt.setPixel(i, red, green, blue);

    value--;
  }

  blinkt.show();
}

setInterval(function() {
  // Get a value between 0 and 1
  var time = Date.now();
  var value = (Math.sin(time) + 1) / 2;

  showGraph(value, 255, 0, 255);
}, 100);
