/* jshint undef: true, node: true, esnext: true, asi: true */

'use strict'

const c = require('../config/constants')

module.exports = exports = {}

/*
Function to browse a conway world and convert it
into an array of coordinates suitable for the drawPixel() function:

For instance
[[0,...,0] , ...] -> [ [128, 1, 1], [128, 32, 1], [128, 16, 1], [64, 16, 1] ];

Note: we are keeping only the 1s as the screen will be cleared at every step
*/
exports.conwayToOledPixels = (cells) => {
    let pixels = []

    for (let i = 0; i<c.WIDTH ; i++ ) {
        for (let j = 0; j<c.HEIGHT ; j++ ) {
            if (cells[i][j] === 1) {
                pixels.push([i,j,1])
            }
        }
    }
    return pixels
}

// for debug purpose - print the state of the cells on the console.
exports.logWorld = (cells) => {
    console.log('--------------------')
    for (let i = 0; i<c.WIDTH ; i++ ) {
        let line = (cells[i]).reduce( (l, c) => {
            if (c === 1) {
                return l + 'O'
            } else {
                return l + ' '
            }
        }, '')
        console.log(line)
    }
    console.log('--------------------')
}