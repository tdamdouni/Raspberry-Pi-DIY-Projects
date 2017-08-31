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

/*
 * Data from OpenWeatherMap
 * showGraph function adapted from cpu-temp.js
 */

var http = require('http');
var querystring = require('querystring');
var util = require('util');

var blinkt = require('../src/blinkt');

blinkt.setClearOnExit();
blinkt.setBrightness(0.1);

// Grab your API key here: http://openweathermap.org/appid
var API_KEY = '';
// List of city IDs can be downloaded here http://bulk.openweathermap.org/sample/city.list.json.gz
var CITY_ID = '';

var url = 'http://api.openweathermap.org/data/2.5/weather';

function drawThermo(temp) {
  var value = temp / 40 + (1 / 8);

  showGraph(value, 255, 0, 0);
}

function getTemperature(callback) {
  var payload = {
    appid: API_KEY,
    id: CITY_ID,
    units: 'metric'
  };

  var req = http.get(url + '?' + querystring.stringify(payload), function(res) {
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
      var temp;

      try {
        temp = JSON.parse(rawData).main.temp;

        console.log(util.format('Temperture = %d C', temp));

        callback(null, temp);
      } catch (e) {
        callback(e);
      }
    });
  });

  req.on('error', callback);
}

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
  getTemperature(function(error, temp) {
    if (error) {
      console.error(error);
      return;
    }

    drawThermo(temp);
  });
}, 2 * 60 * 1000);
