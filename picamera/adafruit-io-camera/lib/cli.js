'use strict';

const CLI = require('adafruit-io').CLI,
      spawn = require('child_process').spawn,
      path = require('path'),
      fs = require('fs'),
      Yargs = require('yargs');

class CameraCLI extends CLI {

  constructor() {

    super('camera');

    this.completions = [
      'help',
      'config'
    ];

    this.yargs = Yargs(process.argv.slice(3));

  }

  init() {

    if(! process.env.AIO_CLIENT_USER || ! process.env.AIO_CLIENT_KEY)
      return this.requireAuth(this.yargs);

    this.completions = [
      'help',
      'config',
      'start',
      'restart',
      'stop'
    ];

    if(require('os').platform() === 'linux')
      this.completions.push('install', 'remove');

    this.yargs
        .usage('Usage: adafruit-io camera <command> [options]')
        .command('config', 'Configure Adafruit IO Auth', this.requireAuth.bind(this));

    if(require('os').platform() === 'linux') {
      this.yargs.command('install', 'Install camera service (linux only)');
      this.yargs.command('remove', 'Remove camera service (linux only)');
    }

    const argv = this.yargs
      .command('start', 'Start camera daemon')
      .command('restart', 'Restart camera daemon')
      .command('stop', 'Stop camera daemon')
      .command('help', 'Show help')
      .alias('f', 'feed').nargs('f', 1).default('f', process.env.AIO_CAMFEED || 'picam').describe('f', 'Adafruit IO Camera Feed Name')
      .alias('m', 'motion').boolean('m').describe('m', 'Motion Tracking')
      .alias('t', 'threshold').nargs('t', 1).default('t', process.env.MOTION_THRESH || '21').describe('t', 'Motion Threshold')
      .alias('c', 'change').nargs('c', 1).default('c', process.env.MOTION_MINCHANGE || '10').describe('c', 'Motion Minimum Change')
      .alias('s', 'seconds').nargs('s', 1).default('s', process.env.MOTION_MINSECONDS || '1').describe('s', 'Motion Minimum Seconds')
      .alias('r', 'rate').nargs('r', 1).default('r', process.env.CAM_RATE || '2').describe('r', 'Timelapse Capture Rate (seconds)')
      .alias('h', 'hflip').boolean('h').describe('h', 'Camera Horizontal Flip')
      .alias('v', 'vflip').boolean('v').describe('v', 'Camera Vertical Flip')
      .demand(1, 'You must supply a valid camera command')
      .argv;

    if(! argv)
      return;

    const command = argv._[0];

    if(command === 'help')
      return this.yargs.showHelp();

    if(command === 'config')
      return;

    if(command === 'start' || command === 'install') {

      process.env.AIO_CAMFEED = argv.feed;
      process.env.MOTION = argv.motion ? 'true' : 'false';
      process.env.MOTION_THRESH = argv.threshold;
      process.env.MOTION_MINCHANGE = argv.change;
      process.env.MOTION_MINSECONDS = argv.seconds;
      process.env.CAM_HFLIP = argv.hflip ? 'true' : 'false';
      process.env.CAM_VFLIP = argv.vflip ? 'true' : 'false';
      process.env.CAM_RATE = argv.rate;

      this.saveEnv();

    }

    if(! this[command])
      return this.yargs.showHelp();

    this[command]();

  }

  install() {

    if(require('os').platform() !== 'linux')
      return this.error('running the camera as a service is only supported on linux');

    this.logo();
    this.info('installing service...');

    this.foreverService('install');
    this.info(`camera service is now installed and pushing images to Adafruit IO`);

  }

  remove() {

    if(require('os').platform() !== 'linux')
      return this.error('running the camera as a service is only supported on linux');

    this.foreverService('remove');
    this.info('removing service...');
    this.spawn('killall', ['raspistill']);

  }

  start() {

    this.logo();
    this.info('starting camera...');

    this.forever('start');
    this.info(`camera daemon started and is pushing images to Adafruit IO`);

  }

  restart() {
    this.spawn('killall', ['raspistill']);
    this.forever('restart');
    this.info('restarting camera...');
  }

  stop() {
    this.forever('stop');
    this.info('stopping camera...');
    this.spawn('killall', ['raspistill']);
  }

  saveEnv() {

    let out = '';

    Object.keys(process.env).forEach(key => {
      if(/^(AIO|CAM|MOTION)/.test(key)) out += `${key}=${process.env[key]}\n`;
    });

    if(out) {
      this.constructor.getConfigPath()
        .then(f => {
          fs.writeFileSync(f, out);
        })
        .catch(this.error);
    }

  }

  spawn(command, args) {

    const child = spawn(command, args, {
      cwd: path.join(__dirname, '..'),
      env: process.env,
      detached: true
    });

    child.stderr.on('data', this.error);
    child.on('exit', function(code) {
      process.exit(code);
    });

  }

  requireAuth(yargs) {

    const argv = yargs
      .usage('Usage: adafruit-io camera config [options]')
      .alias('u', 'username').demand('username').nargs('u', 1).describe('u', 'Adafruit IO Username')
      .alias('k', 'key').demand('key').nargs('k', 1).describe('k', 'Adafruit IO Key')
      .command('help', 'Show help')
      .argv;

    process.env.AIO_CLIENT_USER = argv.username;
    process.env.AIO_CLIENT_KEY  = argv.key;

    this.saveEnv();

  }

}

exports = module.exports = CameraCLI;
