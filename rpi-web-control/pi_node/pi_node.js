// Require
var sensorLib = require('node-dht-sensor');
var express = require('express');
var app = express();

// Configure app
app.set('views', __dirname + '/views')
app.set('view engine', 'jade')
app.use(express.static(__dirname + '/public'))

// Serve interface
app.get('/interface', function(req, res){
    res.render('interface');
});

var piREST = require('pi-arest')(app);

// Set Pi properties
piREST.set_id('1');
piREST.set_name('my_RPi');

// Make measurements from sensors
var dht_sensor = {
    initialize: function () {
        return sensorLib.initialize(11, 4);
    },
    read: function () {
        var readout = sensorLib.read();
        
        piREST.variable('temperature',readout.temperature.toFixed(2));
        piREST.variable('humidity', readout.humidity.toFixed(2));
        
        console.log('Temperature: ' + readout.temperature.toFixed(2) + 'C, ' +
            'humidity: ' + readout.humidity.toFixed(2) + '%');
        setTimeout(function () {
            dht_sensor.read();
        }, 2000);
    }
};
if (dht_sensor.initialize()) {
    dht_sensor.read();
} else {
    console.warn('Failed to initialize sensor');
}

var server = app.listen(3000, function() {
    console.log('Listening on port %d', server.address().port);
});
