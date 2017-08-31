const PythonShell = require('python-shell');
const pi = require('node-raspi');
const MA = require('moving-average');

const config = require('./config');

const options = {
  scriptPath: __dirname
};
const script = 'script.py';

const factor = config.get('temperature.factor');
const duration = config.get('interval.duration');
const timeInterval = duration * 5;
const ma = MA(timeInterval);


exports.readValues = () => {
  return new Promise((resolve, reject) => {
    PythonShell.run(script, options, function (err, results) {
      if (err) return reject(err);

      // results is an array consisting of messages collected during execution
      const result = results[0]; // should only be 1
      const data = JSON.parse(result);
      data.temperature = calibrateTemp(data.temperature, getCpuTemp(), factor);
      resolve(data);
    });
  });
};

function getCpuTemp() {
  return pi.getThrm();
}

function calibrateTemp(sensorTemp, cpuTemp, factor) {
  const calibrated = sensorTemp - ((cpuTemp - sensorTemp) / factor);

  ma.push(Date.now(), calibrated);

  // console.log(sensorTemp, cpuTemp);
  // console.log('calibrated value is', calibrated);
  // console.log('moving average now is', ma.movingAverage());
  // console.log('moving variance now is', ma.variance());

  return ma.movingAverage();
}
