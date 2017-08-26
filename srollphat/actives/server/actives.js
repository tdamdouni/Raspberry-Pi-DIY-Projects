var app = require('http').createServer(handler)
var io = require('socket.io')(app);
var fs = require('fs');
var url = require('url') ;

var apiKey = "DR8EN37VFU3CR997"; // Replace with your own key (must be the same one as in the Python code!)

app.listen(7070);

var active = 0;

function handler(req, res) {

  var queryObject = url.parse(req.url,true).query;

  if (queryObject['key'] == apiKey) {
    res.writeHead(200);
    res.end(String(active));
  } else {
    res.writeHead(403);
    res.end();
  }

}

var actives = io.of('/actives');

actives.on('connection', function (socket) {

  active +=1;

  socket.on('disconnect', function (socket) {
    active -=1;
  });

});
