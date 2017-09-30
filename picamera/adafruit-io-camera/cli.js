#!/usr/bin/env node

process.title = 'adafruit-io';

const CLI = require('adafruit-io').CLI;

CLI.getConfigPath().then(path => {

  require('dotenv').config({silent: true, path: path});

  const cli = new CLI();

  cli.sub.camera = require('./lib/cli');
  cli.completions.push('camera');

  cli.yargs.command('camera', 'Connect your Raspberry Pi camera to Adafruit IO');

  cli.init();

}).catch(console.error);
