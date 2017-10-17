/* jshint undef: true, node: true, esnext: true, asi: true */
/* global describe, it */
'use strict'

var assert = require('assert');
var c = require('../config/constants')
var conway = require('../lib/conway.js');

describe('conway', () => {
    
    describe('generateEmptyWorld', () => {
        it('should return a two dimentional array with the correct sizes', () => {
            let cells = conway.generateEmptyWorld()
            assert(cells.length === c.WIDTH)
            assert((cells[0]).length === c.HEIGHT)
        })
        it('should have only zeros', () => {
            let cells = conway.generateEmptyWorld()
            let sums = cells.map((e) => e.reduce((sum, value) => sum+value, 0))
            let sum = sums.reduce((sum, value) => sum+value, 0)         
            assert(sum === 0)
        })
    })

    describe('generateRandomWorld', () => {
        it('should return a two dimentional array with the correct sizes', () => {
            let cells = conway.generateRandomWorld()
            assert(cells.length === c.WIDTH)
            assert((cells[0]).length === c.HEIGHT)
        })
        it('should return an array of 1 and 0 only', () => {
            let cells = conway.generateRandomWorld()
            let only1and0 = (e) => {return ((e === 1) || (e === 0))}
            let areValid = cells.map((e) => e.reduce((all, elt) => only1and0(elt) && all, true))
            let isValid = areValid.reduce((all, elt) => elt && all, true)
            assert(isValid)
        })
    })

    describe('numberOfNeighbours', () => {
        it('should correctly count the number of neighbours for a generic cell in an empty world', () => {
            let cells = conway.generateEmptyWorld()
            let n = conway.numberOfNeighbours(cells, 3, 3)
            assert(n === 0)
        })
        it('should not count itself as a neighbour', () => {
            let cells = conway.generateEmptyWorld()
            cells[3][3] = 1
            let n = conway.numberOfNeighbours(cells, 3, 3)
            assert(n === 0)
        })

        it('should correctly count the number of neighbours for a generic cell with 4 neighbours', () => {
            let cells = conway.generateEmptyWorld()
            cells[2][3] = 1
            cells[4][3] = 1
            cells[3][2] = 1
            cells[3][4] = 1
            let n = conway.numberOfNeighbours(cells, 3, 3)
            assert(n === 4)
        })

        it('should correctly count the number of neighbours for a low border cell with no neighbours', () => {
            let cells = conway.generateEmptyWorld()
            let n = conway.numberOfNeighbours(cells, 0, 0)
            assert(n === 0)
        })
        it('should correctly count the number of neighbours for a low border cell with 3 neighbours', () => {
            let cells = conway.generateEmptyWorld()
            cells[0][1] = 1
            cells[1][0] = 1
            cells[1][1] = 1
            let n = conway.numberOfNeighbours(cells, 0, 0)
            assert(n === 3)
        })
        
        it('should correctly count the number of neighbours for a high border cell with no neighbours', () => {
            let cells = conway.generateEmptyWorld()
            let n = conway.numberOfNeighbours(cells, c.WIDTH, c.HEIGHT)
            assert(n === 0)
        })
        it('should correctly count the number of neighbours for a high border cell with 3 neighbours', () => {
            let h = c.HEIGHT
            let w = c.WIDTH
            let cells = conway.generateEmptyWorld()
            cells[h-2][w-1] = 1
            cells[h-1][w-2] = 1
            cells[h-2][w-2] = 1
            let n = conway.numberOfNeighbours(cells, h-1, w-1)
            assert(n === 3)
        })
        
    })

    describe('newStatus', () => {
        it('should check that life can appear if exactly 3 neighbours', () => {
            let cells = conway.generateEmptyWorld()
            cells[2][3] = 1
            cells[4][3] = 1
            cells[3][2] = 1
            let newStatus = conway.newStatus(cells, 3, 3)
            assert(newStatus === 1)
        })
        it('should check that a cell will die if more than 3 neighbours', () => {
            let cells = conway.generateEmptyWorld()
            cells[3][3] = 1 // The cell we are killing
            cells[2][3] = 1
            cells[4][3] = 1
            cells[3][2] = 1
            cells[3][4] = 1
            let newStatus = conway.newStatus(cells, 3, 3)
            assert(newStatus === 0)
        })
        it('should check that a cell will die if less than 2 neighbours', () => {
            let cells = conway.generateEmptyWorld()
            cells[3][3] = 1 // The cell we are killing
            cells[2][3] = 1
            let newStatus = conway.newStatus(cells, 3, 3)
            assert(newStatus === 0)
        })
        it('should check that a cell can stay alive if it has 2 neighbours', () => {
            let cells = conway.generateEmptyWorld()
            cells[3][3] = 1 // The cell we are keeping alive
            cells[2][3] = 1
            cells[4][3] = 1
            let newStatus = conway.newStatus(cells, 3, 3)
            assert(newStatus === 1)
        })
        it('should check that a cell can stay alive if it has 3 neighbours', () => {
            let cells = conway.generateEmptyWorld()
            cells[3][3] = 1 // The cell we are keeping alive
            cells[2][3] = 1
            cells[4][3] = 1
            cells[3][2] = 1
            let newStatus = conway.newStatus(cells, 3, 3)
            assert(newStatus === 1)
        })

    })

});