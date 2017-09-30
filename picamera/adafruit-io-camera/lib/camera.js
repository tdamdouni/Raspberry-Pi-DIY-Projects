'use strict';

const RaspiCam = require('raspicam'),
      Readable = require('stream').Readable,
      os = require('os'),
      path = require('path'),
      fs = require('fs');

class Camera extends Readable {

  constructor(options) {

    super();

    this.buffer = [];
    this.options = {
      mode: 'timelapse',
      timelapse: 3000,
      timeout: 999999999,
      quality: 10,
      nopreview: true,
      output: path.join(os.tmpdir(), 'aio_cam', 'cam.jpg')
    };

    Object.assign(this.options , options || {});

    this.camera = new RaspiCam(this.options);
    this.camera.start();
    this.camera.on('read', this.processImage.bind(this));
    this.camera.on('start', this.handleError.bind(this));
    this.camera.on('stop', this.handleError.bind(this));

  }

  handleError(err) {

    if(err)
      this.emit('error', err);

  }

  processImage(err, date, file) {

    if(err)
      return this.handleError(err);

    fs.readFile(path.join(os.tmpdir(), 'aio_cam', file), (err, data) => {

      if(err)
        return this.handleError(err);

      this.buffer.push(data);
      this.emit('image', file);

    });

  }

  _read() {

    if(! this.buffer.length)
      return this.once('image', this._read.bind(this));

    this.push(this.buffer.shift());

  }

}

exports = module.exports = Camera;
