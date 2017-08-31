const { join } = require('path');
module.exports = require('loke-config').create('envirophatmqtt', { appPath: join(__dirname, '/../') });
