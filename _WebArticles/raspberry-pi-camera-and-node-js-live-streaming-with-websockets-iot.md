# Raspberry Pi, Camera and Node.js – Live Streaming with Websockets #IoT

_Captured: 2017-08-23 at 21:50 from [thejackalofjavascript.com](http://thejackalofjavascript.com/rpi-live-streaming)_

A few days ago Bala Kolluru has reached out to me asking if we can control a Raspberry Pi camera module using Web browser, so he can view a live stream from any HTML5 powered device. I was intrigued by this idea and wanted to give it a try.

In this post, we will see how we can implement a system that can "stream" a video from our pi to a browser. The completed system would look like

Pretty sweet right! I am able to see my aquarium from any where and check on my only gold fish. This can be extended to do anything.

For instance, you can hook the camera up pointing at the front door, as soon as someone rings the bell, you can see who is at the door by opening the video stream URL in your mobile/tablet/computer and confirm if you need to wear pants to open the door.

So let us see how we can build such an awesome multi-purpose system.

You can find the complete code for this system [here](https://github.com/arvindr21/pi_livestreaming).

## Prerequisites

If you are new to Raspberry pi and have not yet installed Node.js on it, I would recommend going through [Getting Started with Raspberry pi and Node.js](http://thejackalofjavascript.com/getting-started-raspberry-pi-node-js/).

If you are new to electronics devices and circuits, I would recommend going through the [video lectures](http://www.allaboutcircuits.com/videos/index.html) from All About Circuits.

### Components needed

  1. 1 - Raspberry pi B+
  2. 1 - Raspberry pi camera

If you have not already set up the camera module, please follow [this](http://thejackalofjavascript.com/rpi-video-the-intruder/#camera).

## Understanding MJPEG

Based on what I have googled and understood, there is no straight forward way of streaming the live video from the camera module to a web browser.

After going through a [few similar solutions](https://www.youtube.com/watch?v=TgUQCSk3nUE), I kind of sort of decided that MJPEGs are the way to go when dealing with Live streaming from the Pi.

MJPEG is Motion JPEG. You can know more about MJPEG in the below video

In this post we are **not** really using MJPEG from a technology standpoint, but we are using a similar principle.

The idea is that we keep clicking pictures using the camera say for every 100ms and then save it to the same file. And then we keep sending the same image to the client as it changes every time.

This is really not the best of solutions, but it kind of gets the job done. I am looking for other alternatives too and will update this post as it goes.

## Building the system

So, the idea is very simple, we will have a web server setup on the Pi. When we get a request to start the stream, we will trigger a child process in node that will start capturing the picture, once for every 100ms.

Then we have a file watcher on that image file and whenever the file changes, we trigger the client to load the new image.

We are using Web Sockets to emit and act on the events accordingly.

Now, login to your pi via ssh - terminal/putty. As soon as you ssh into pi, you will be landing inside the _/home/pi_ folder. We will create a new folder here named _node_programs._ And inside this folder, we will be maintaining all our programs. Run

mkdir node_programs

To step inside that folder, run

For this post, we will create a new folder named _liveStreaming_ and will step inside this folder. Run

Note : You can run multiple commands separated by a _&&._

First we will initialize a new node project here. Run

Fill it up as applicable.

Now, we will install express and socket.io modules on our pi. Run

npm install express socket.io --save

Once they are installed, create a new file named _index.js._ And we will open the same in the nano editor. Run

nano index.js

Paste the below code into the nano editor

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172 
var express = require('express');var app = express();var http = require('http').Server(app);var io = require('socket.io')(http);var fs = require('fs');var path = require('path');var spawn = require('child_process').spawn;var proc;app.use('/', express.static(path.join(__dirname, 'stream')));app.get('/', function(req, res) {res.sendFile(__dirname + '/index.html');});var sockets = {};io.on('connection', function(socket) {sockets[socket.id] = socket;console.log("Total clients connected : ", Object.keys(sockets).length);socket.on('disconnect', function() {delete sockets[socket.id];// no more sockets, kill the streamif (Object.keys(sockets).length == 0) {app.set('watchingFile', false);if (proc) proc.kill();fs.unwatchFile('./stream/image_stream.jpg');}});socket.on('start-stream', function() {startStreaming(io);});});http.listen(3000, function() {console.log('listening on *:3000');});function stopStreaming() {if (Object.keys(sockets).length == 0) {app.set('watchingFile', false);if (proc) proc.kill();fs.unwatchFile('./stream/image_stream.jpg');}}function startStreaming(io) {if (app.get('watchingFile')) {io.sockets.emit('liveStream', 'image_stream.jpg?_t=' + (Math.random() * 100000));return;}var args = ["-w", "640", "-h", "480", "-o", "./stream/image_stream.jpg", "-t", "999999999", "-tl", "100"];proc = spawn('raspistill', args);console.log('Watching for changes...');app.set('watchingFile', true);fs.watchFile('./stream/image_stream.jpg', function(current, previous) {io.sockets.emit('liveStream', 'image_stream.jpg?_t=' + (Math.random() * 100000));})}

Things to notice

**Line 1 - 6** : Essential requires

**Line 8** : Cache spawn method on child_process

**Line 9** : Global proc variable that we store the spawned process

**Line 11** : Make the _stream_ folder as a static folder

**Line 14** : Default route that will dispatch the _index.html_

**Line 18** : Global sockets object. This will store all the connected sockets

**Line 22** : When a client connects to the server, a new socket will be created. This is store in the global variable.

**Line 25** : We delete the disconnected client from the global object and if there are no more clients we will stop the streaming (power saving)

**Line 36** : We start the streaming on start-stream event.

**Line 42** : We start the server

**Line 56** : If the capturing is already started, we will not re-init the same. And then emit the last saved image to the client

**Line 62** : If the capturing is not started, we will start a new child process and then spawn it with raspistill command. And then register a watch on the file which changes. And whenever the file changes we emit a URL to all the connected clients.

**Note** : The _t param on the image is to avoid caching

Argument to the raspistill command

  * -w : width 640px
  * -h : height 480px
  * -o : output file ./stream/image_stream.jpg
  * -t : Timeout before the camera stops capturing
  * -tl - Time Limit between captures 100ms

A simple Express/Socket IO server

Let us save the file now. To save the program, press (ctrl+x). This will ask you to save the file. Press Y and press enter key to complete the operation.

Now we will create a new folder named _stream_ at the root of the _liveStreaming _folder. This is where our image will be saved.

Finally the Websocket client

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556 
<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Stream My Aquarium</title><!-- Bootstrap CSS --><link href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet"><style type="text/css"> #stream {height: 99%;margin: 0px auto;display: block;margin-top: 20px;}</style><!-- jQuery --><script src="http://code.jquery.com/jquery.js"></script><!-- Bootstrap JavaScript --><script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script><script src="/socket.io/socket.io.js"></script><script>var socket = io();socket.on('liveStream', function(url) {$('#stream').attr('src', url);$('.start').hide();});function startStream() {socket.emit('start-stream');$('.start').hide();}</script></head><body class="container"><h1 class="text-center">My Aquarium<small>Powered by PI</small></h1><hr><button type="button" id="" class="btn btn-info start" onclick="startStream()">Start Camera</button><div class="row"><img src="" id="stream"></div></body></html>

Things to notice

**Line 28** : Init sockets

**Line 29** : When there is new image saved, liveStream event will be broadcasted. And then we will fetch the image.

**Line 34** : We start streaming when a user clicks on the Start button. If the video has already started by another user, we simply hide the button and show the last saved image.

**Line 51** : The Image tag

That is it! save the file as we did above and then we will start the node server. Run

node index.js

And then access the port 3000 on your Raspberry pi port. My pi runs on 192.168.2.2, so my URL would be

http://192.168.2.2:3000

Click on start camera and Bam!! You should see the live feed.

As mentioned earlier it is a big laggy and buggy. You can tweak -tl - Time Limit between captures to < 50ms and see how it works for you.

Hope this post gave you an ideas as how to "stream" a video from your pi camera to the browser.

Thanks for reading! Do comment.  
@arvindr21
