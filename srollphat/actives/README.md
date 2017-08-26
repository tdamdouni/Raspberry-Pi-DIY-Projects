# Actives 🎿

![alt tag](https://raw.github.com/davidmaitland/actives/master/demo.gif)

Display how many people are on your website using a Raspberry Pi Zero and a Pimoroni Scroll pHAT.

It uses web sockets to track how many people are on your website at and one point in time. On the Zero it uses the [scroll-phat library](https://github.com/pimoroni/scroll-phat) from Pimoroni.

There are three parts:

1. The server code that you will probably run on the same server that your website is being hosted from. It's written in Node.js and uses Socket.io to handle the web sockets. It also exposes a route that the Pi Zero will connect to for the active count.
2. The Pi Zero code. This is written in Python polls and updates the Scroll pHAT with the current count (limited to three digits currently). If it struggles to get an update from the server it turns the last LED on the display on.
3. The tracking code that you place on your web page. Every time someone gores onto your web site it will then open a persistent connection with the server code that tracks how many people are on the site.

There are some settings you can change in the server and Pi Zero code so checkout the files. Most importantly is the API key setting that prevents anyone from seeing how many people are on your web site.

## Setting up the server

1. Copy the `server` directory onto your server.
2. Install dependancies `npm install`.
3. Run the program `node actives.js` (Keep it running using [forever](https://github.com/foreverjs/forever) or screen).

## Setting up the Pi Zero

1. Copy the `zero` directory onto your Pi Zero.
2. Install dependancies `sudo pip install -r requirements.txt`.
3. Install the smbus module `sudo apt-get install python-smbus`.
4. Active i2c module under the advanced menu using `sudo raspi-config`.
5. Run the program `./actives.py`.

You can start the program on automatically boot by adding `/home/pi/zero/actives.py &` to your `/etc/rc.local` files, just above the `exit 0` line.

## Setting up your website (tracking code)

Add the tracking script near the bottom of your site (after `</body>` before `</html>`).

```
<script src="https://cdn.socket.io/socket.io-1.3.7.js"></script>
<script>var socket = io("http://MYSERVER.TLD:7070/actives")</script>
```
