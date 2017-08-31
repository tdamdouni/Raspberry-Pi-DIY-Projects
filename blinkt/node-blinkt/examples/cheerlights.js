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

var http = require('http');

var blinkt = require('../src/blinkt');

blinkt.setClearOnExit();

function convertHexToRgb(hex) {
  hex = '0x' + hex.substring(1);

  var red = hex >> 16;
  var green = hex >> 8 & 0xff;
  var blue = hex & 0xff;

  return [ red, green, blue];
}

function getColor(callback) {
  var options = {
    hostname: 'api.thingspeak.com',
    path: '/channels/1417/field/2/last.json',
    timeout: 2 * 1000
  };

  var req = http.get(options, function(res) {
    var contentType = res.headers['content-type'];
    var statusCode = res.statusCode;
    var error;

    if (statusCode !== 200) {
      error = new Error('Request failed! Status code: ' + statusCode);
    } else if (!/^application\/json/.test(contentType)) {
      error = new Error('Invalid Content-Type! Expected application/json but received ' + contentType);
    }

    if (error) {
      res.resume();

      return callback(error);
    }

    res.setEncoding('utf8');

    var rawData = '';

    res.on('data', function(chunk) {
      rawData += chunk;
    });
    res.on('end', function() {
      var color;

      try {
        color = JSON.parse(rawData).field2;

        callback(null, color);
      } catch (e) {
        callback(e);
      }
    });
  });

  req.on('error', callback);
}

setInterval(function() {
  getColor(function(error, color) {
    if (error) {
      console.error(error);
      return;
    }

    var colors = convertHexToRgb(color);
    var red = colors[0];
    var green = colors[1];
    var blue = colors[2];

    for (var i = 0; i < blinkt.NUM_PIXELS; i++) {
      blinkt.setPixel(i, red, green, blue);
    }

    blinkt.show();
  });
}, 5 * 1000);
