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

var hueRange = 120;
var hueStart = 0;
var maxBrightness = 0.2;

function convertHsvToRgb(h, s, v) {
  var i = Math.floor(h * 6);
  var f = h * 6 - i;
  var p = v * (1 - s);
  var q = v * (1 - f * s);
  var t = v * (1 - (1 - f) * s);
  var b, g, r;

  switch (i % 6) {
  case 0:
    r = v;
    g = t;
    b = p;
    break;
  case 1:
    r = q;
    g = v;
    b = p;
    break;
  case 2:
    r = p;
    g = v;
    b = t;
    break;
  case 3:
    r = p;
    g = q;
    b = v;
    break;
  case 4:
    r = t;
    g = p;
    b = v;
    break;
  case 5:
    r = v;
    g = p;
    b = q;
    break;
  }

  var red = r * 255;
  var green = g * 255;
  var blue = b * 255;

  return [ red, green, blue ];
}

function showGraph(value, red, green, blue) {
  var brightness, hue, rgb;

  value *= blinkt.NUM_PIXELS;

  for (var i = 0; i < blinkt.NUM_PIXELS; i++) {
    hue = ((hueStart + ((i / blinkt.NUM_PIXELS) * hueRange)) % 360) / 360;
    rgb = convertHsvToRgb(hue, 1, 1);
    red = Math.floor(rgb[0]);
    green = Math.floor(rgb[1]);
    blue = Math.floor(rgb[2]);

    if (value < 0) {
      brightness = 0;
    } else {
      brightness = Math.min(value, 1) * maxBrightness;
    }

    blinkt.setPixel(i, red, green, blue, brightness);

    value--;
  }

  blinkt.show();
}

setInterval(function() {
  // Get a value between 0 and 1
  var time = Date.now() * 2;
  var value = (Math.sin(time) + 1) / 2;

  showGraph(value, 255, 0, 255);
}, 100);
