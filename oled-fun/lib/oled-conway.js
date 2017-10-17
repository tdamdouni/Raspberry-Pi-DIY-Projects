/* jshint undef: true, node: true, esnext: true, asi: true */

'use strict'

let Oled = require('oled-i2c-bus'),
    i2c = require('i2c-bus'),
    i2cBus = i2c.openSync(1),
    c = require('../config/constants'),
    utils = require('./utils'),
    conway = require('./conway')

let opts = {
    width: c.WIDTH,
    height: c.HEIGHT,
    address: c.I2C_ADDR
}

let oled = new Oled(i2cBus, opts)
oled.clearDisplay()
oled.turnOnDisplay()

let cells = conway.generateRandomWorld()

function step() {
    oled.clearDisplay()
    oled.drawPixel(utils.conwayToOledPixels(cells))
    cells = conway.evolveOneStep(cells)
}

setInterval(step, 300)


