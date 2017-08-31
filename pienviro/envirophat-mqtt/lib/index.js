const mqtt = require('mqtt');

const config = require('./config');
const { readValues } = require('./readvalues');

let mqttClient;
let mqttConnected = false;
let interval;

const logger = console;
const mqttUri = 'mqtt://' + config.get('mqtt.host');
const topic = config.get('mqtt.topic');
const duration = config.get('interval.duration');

exports.start = () => {
  mqttClient  = mqtt.connect(mqttUri);

  mqttClient.on('connect', function () {
    logger.info('MQTT connected');
    mqttConnected = true;
  });

  mqttClient.on('close', console.log);
  mqttClient.on('offline', console.log);
  // mqttClient.on('error', console.error);
  // mqttClient.on('message', console.log);
  
  // mqttClient.on('message', function (topic, message) {
  //   // message is Buffer 
  //   console.log(message.toString())
  // })

  const run = () => {
    readValues()
    .then(emit)
    .catch(err => console.error(err.stack));
  };

  interval = setInterval(run, duration);
  run();
};

exports.stop = () => {
  clearInterval(interval);
};

function emit(valueMap) {
  if (!mqttConnected) return;

  const data = Object.assign({}, valueMap, { timestamp: new Date() });
  mqttClient.publish(topic, JSON.stringify(data));
  logger.info(`Publish: ${topic} ${JSON.stringify(data)}`);
}
