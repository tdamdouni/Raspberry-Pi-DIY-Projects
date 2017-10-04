// app.js
var express = require('express');  
var app = express();  
var server = require('http').createServer(app);  
var io = require('socket.io')(server);
var fs = require('fs');

var temperature = 0;

// Static directory for html/css/js
app.use(express.static(__dirname + '/public/'));  

// Routing
app.get('/', function(req, res,next) {  
    res.sendFile(__dirname + '/public/index.html');
});

app.get('/about.html', function(req, res, next) {
	res.sendFile(__dirname + '/public/about.html');
});

app.get('/help.html', function(req, res, next) {
	res.sendFile(__dirname + '/public/help.html');
});

io.on('connection', function(client) {  
  console.log('Client connected...');

  client.emit('welcomeUpdate');

  client.on('join', function(data) {
    console.log(data);
  });

  client.on('timer', function() {
    console.log("Received timer event");
  });

  // Sensor updates
  client.on('tempReading', function(data) {
    temperature = data;
    console.log(data);
    console.log(temperature);
    client.broadcast.emit('tempUpdate', temperature);
    console.log("temperature update sent to frontend");
    writeLogFile("temp", temperature);
  });

  client.on('HumReading', function(data) {
    humidity = data;
    console.log(data);
    console.log(humidity);
    client.broadcast.emit('humUpdate', humidity);
    console.log("humidity update sent to frontend");
    writeLogFile("hum", humidity);
  });


  client.on('doorReading', function(data) {
    doorStatus = data;
    console.log("Door status : ");
    console.log(data);
    client.broadcast.emit('doorUpdate', data);
    console.log("door update sent to frontend");
    writeLogFile("door", doorStatus);
  });

  client.on('PhotoReading', function(data) {
    photoStatus = data;
    console.log("Photo status : ");
    console.log(data);
    client.broadcast.emit('photoUpdate', data);
    console.log("photo update sent to frontend");
    writeLogFile("photo", photoStatus);
  });

});

function writeLogFile(type,data) {
  var d = new Date();
  var current_hour = d.getHours();
  var current_min = d.getMinutes();
  var current_sec = d.getSeconds();
  var date = d.getUTCDate().toString() + "-" + d.getUTCMonth().toString() + "-" + d.getUTCFullYear().toString();
  var text = "";
  text += date+":";
  text += current_hour.toString()+":"+current_min.toString()+":"+current_sec.toString();
  if(type == "temp") {
    text += "::T:";
  } else if(type == "hum") {
    text += "::H:";
  } else if(type == "door") {
    text += "::D:";
  } else if(type == "photo") {
    text += "::P:";
  }
  text += data;
  text += "\n"
  console.log("Writing data to log file");
  fs.appendFile(date+".txt", text, function (err) {
    if(err) throw err;
    console.log("Data appended to the file");
  });
}

server.listen(5000, '192.168.43.210');  
