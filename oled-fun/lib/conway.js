/* jshint undef: true, node: true, esnext: true, asi: true */

'use strict'

const c = require('../config/constants')

module.exports = exports = {}

// Generate an array of WIDTH times HEIGHT cells filled with zeros.
exports.generateEmptyWorld = () => {
    let cells = []
    for (let i = 0; i<c.WIDTH ; i++ ) {
        cells[i] = []
        for (let j = 0; j<c.HEIGHT ; j++ ) {
            cells[i][j] = 0
        }
    }
    return cells
}

// Generate an array of WIDTH times HEIGHT cells filled with zeros and ones picked randomly.
exports.generateRandomWorld = () => {
    let cells = []
    for (let i = 0; i<c.WIDTH ; i++ ) {
        cells[i] = []
        for (let j = 0; j<c.HEIGHT ; j++ ) {
            cells[i][j] = Math.floor(Math.random() * 2)
        }
    }
    return cells
}

// Count how many neighbours cell (x,y) has.
exports.numberOfNeighbours = (cells, x, y) => {
    let count = 0
    for (let i = x-1; i <= x+1; i++) {
        for (let j = y-1; j <= y+1; j++) {
            if ( (typeof cells[i] !== 'undefined') && (typeof cells[i][j] !== 'undefined')) {
                if (x !== i || y !== j) {
                    count += cells[i][j]
                }
            }
        }
    }
    return count
}

// Compute the new status of one cell
// Alive and n < 2 -> dead
// Alive and n == 2 or n == 3 -> alive
// Alive and n > 3 -> dead
// Dead and n == 3 -> alive
exports.newStatus = (cells, x, y) => {
    let currentStatus = cells[x][y]
    let n = exports.numberOfNeighbours(cells, x, y)

    if (currentStatus === 0) {
        if (n === 3) {
            return 1
        } else {
            return 0
        }
    } else {
        if (n < 2 || n > 3) {
            return 0
        } else {
            return 1
        }
    }
}

// Takes a "world" and make it evolve one step.
exports.evolveOneStep = (cells) => {
    let newCells = []
    for (let i = 0; i<c.WIDTH ; i++ ) {
        newCells[i] = []
        for (let j = 0; j<c.HEIGHT ; j++ ) {
            newCells[i][j] = exports.newStatus(cells, i, j)
        }
    }
    return newCells
}