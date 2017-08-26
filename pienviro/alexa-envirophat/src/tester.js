#!/usr/bin/env node

'use strict'

// Fires the intent - does not go through Lambda

let func = require('./intentHandler');

func((err,res)=> {console.log(res)})
