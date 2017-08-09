# Home Automation using Raspberry Pi and Nodejs

_Captured: 2017-08-08 at 17:35 from [www.hackster.io](https://www.hackster.io/uisli21/home-automation-using-raspberry-pi-and-nodejs-c308b9)_

![Home Automation using Raspberry Pi and Nodejs](https://hackster.imgix.net/uploads/attachments/177373/Z?auto=compress%2Cformat&w=900&h=675&fit=min)

Version 1.0

Quick preview what I did till now:

;

;

![](https://hackster.imgix.net/uploads/attachments/209094/Unbenannt.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

<http://desouza.ch/projekte/coffee.mp4>

Well I moved to a new apartment and right at this time I had heard many things about the popularity of the IoT and the whole home automation stuff. So I thought, why not create an Web application to control my devices at home.

I had to decide if I want to write my app with C# or with a Web language. I was really intrested to make a real time application, so I decided to develop my app with NodeJs.

Before starting the project, let me explain the basics first.

I will use the Raspberry Pi as a master device, which can be controlled via the Browser/Internet. For each device and room, that I want to control, I use another Raspberry or Arduino as slave. The slaves will take command form the master via WiFi or via 433mHz. I will explain this better later in this project.

![](https://hackster.imgix.net/uploads/image/file/174517/Master%20-%20Slave.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Overview Configuration_

The Raspberry Pi that is configured as a slave will take some command from the master via some curl commands. How does this works? Well I configured my Raspberry Pi (slave) as webserver and on the webserver I host some PHP files. Now if I open those file via the browser or via an curl command, the Raspberry Pi opens the PHP file and run automatically a Skript with commands.

Now considering room scenario, an Raspberry Pi and Arduino will control devices and reads sensor data. Periodically, each room will have multiple controllable devices (i.e. Light(s), Fan, Wall Socket(s), Coffe machine, etc.), one PassiveIR (to detect human presence in the room), one temperature sensor (LM35 to collect room temperature) and LDR (to detect light intensity near room window).

![](https://hackster.imgix.net/uploads/image/file/174521/Room%20Config.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Room Configuration (Design Inspired by Anurag S. Vasanwala)_

To identify my devices i will give each device a solid IP Adress and for each command a PHP file.

For example:
    
    
    Coffemachine = IPADDRESS/espresso.php
    Coffemachine = IPADDRESS/Doppio.php
    Plant        = IPADDRESS/whaterOnAll.php
    Lights       = IPADDRESS/LightID/RoomName/ON
    Lights       = IPADDRESS/LightID/RoomName/OFF
    

Note: I have also some Hue lights witch will be controlled via Hue API.
    
    
    Hue Lights       = IPADDRESS/api/{User-ID}/StateAndComands/Value
    

The main problem with the Relais is, if you have a device that is connected to the relay, and the relay is set to off, you can't use the device anymore obviously. So the wall switch for the lights gets useless.

![](https://hackster.imgix.net/uploads/image/file/174529/relay%201.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

To resolve this problem you can either use a DPST relay or use a transistor. I will explain this later again. This is how I did it:

![](https://hackster.imgix.net/uploads/image/file/174534/relay%20Solution.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)
    
    
    //Requirements
    sudo apt-get update
    sudo apt-get install xrdp -y
    sudo apt-get install git-core git scons build-essential scons libpcre++-dev libboost-dev libboost-program-options-dev libboost-thread-dev libboost-filesystem-dev -y
     
    //Install NodeJS
    wget http://nodejs.org/dist/v6.3.0/node-v6.3.0.tar.gz
    tar -zxf node-v6.3.0.tar.gz
    cd node-v6.3.0
    ./configure
    make
    sudo make install
    sudo sh install-node.sh
    node --version
    npm ---version
    sudo node 
     
    // others
    Sudo apt-get install apache2 -y
    Sudo apt-get install proftpd -y   
    
    
    
    /* First App with nodeJS by Weslley De Souza*/
    /* Variables and Requires */var express = require("express")
    , app = express()
    , http = require("http").createServer(app)
    , bodyParser = require("body-parser")
    , io = require("socket.io").listen(http)
    , _ = require("underscore");
    app.locals.moment = require('moment');
    var datetime = require('node-datetime');
    var raspi = require('raspi-llio');            //Comment out, to run on Windows PC
     
    /* Server config *///Server's IP address
    app.set("ipaddr", "192.168.0.53");
    //Server's port number 
    app.set("port", 8080);
    //Specify the views folder
    app.set("views", __dirname + "/views");
    //View engine is Jade
    //app.set("view engine", "jade");       //If you want to code with Jade remove the "//"
     
    //Specify where the static content is
    app.use(express.static("public", __dirname + "/public"));
    //Tells server to support JSON requests
    app.use(bodyParser.json());
    /* Server routing */
     
    //Handle route "GET /", as in "http://localhost:8080/"
    app.get("/", function(request, response) {
    //Render the view called "index"  response.render("index");
    });
    /* Socket.IO events */
    io.on("connection", function(socket){
    console.log('Client has connectet to the server');
    });
    //Event on disconet (Is not working)
    io.on("disconnect", function(socket){
    console.log('Client has disconnectet !');
    });
     
    //Output IP & Port
    http.listen(app.get("port"), app.get("ipaddr"), function() {
    console.log("Server wurd gestartet und ist unter http://" + app.get("ipaddr") + ":" + app.get("port") + " erreichbar");
    });
    

![](https://hackster.imgix.net/uploads/attachments/178745/Sheme.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

I don't know the command to send some curl command directly from NodeJs, so I made a little loop script that checks the value of the GPIO pins. So if I write with NodeJs the GPIO pin 1 to value 1, the script run a command for GPIO 1.

For example: `if ($pin1 == 1){ curl -s 192.168.0.60/espresso.php}`

All Raspberry Pi slaves will be connect via Wireless, and the Wlan Power Saving will be set to Off!
    
    
    sudo nano /etc/network/interfaces
    //add line:
    wireless-power off
    sudo nano /etc/modprobe.d/8192cu.conf
    //add line
    options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
    

Example how to set up a Device to control it. I had at home a Pixie Coffee machine so I used that for my project.

;

;

![](https://hackster.imgix.net/uploads/attachments/177253/IMG_0573.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

![](https://hackster.imgix.net/uploads/attachments/178766/13.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

![](https://hackster.imgix.net/uploads/attachments/178770/12.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

Wire the Relay to the Raspberry. Script example for Doppio:
    
    
    pi@192.168.0.60's
    #!/bin/bash
     
    echo "Doppio"
    gpio export 4 in
    gpio export 13 in
     
    echo "Machine is on"
    #Warming up machine 
    gpio export 3 out
    gpio -g write 3 1
    sleep 34
     
    echo " Machine is ready"
    gpio export 4 out
    gpio -g write 4 1
    sleep 11.5
    gpio -g write 4 0
    sleep 0.5
    gpio -g write 4 1
    sleep 10
    gpio -g write 4 0
    sleep 0.5
    gpio -g write 4 1
    sleep 10.9
     
    echo "Doppio serviert"
    gpio -g write 4 0
    gpio export 4 in
    sleep 1
    echo "Machine is off"
    gpio -g write 3 0
    

<http://desouza.ch/projekte/coffee.mp4>

![](https://hackster.imgix.net/uploads/attachments/178740/hue_still.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)
    
    
    //------------------------------Connect to Hue Light -------------------------------//var hue = require("node-hue-api"),
    HueApi = hue.HueApi,
    lightState = hue.lightState;
    var displayResult = function(result) {
    console.log(result);
    };
    var displayError = function(err) {
    console.error(err);
    };
    var displayStatus = function(status) {
    console.log(JSON.stringify(status, null, 1));
    };
    var host = "192.168.0.50",
    username = "UAW718bnyTbHknwnu1JvGlokRbGoAVIVFxDwG**",
    api = new HueApi(host, username),
    state = lightState.create();
    // Return Hue Online State
    io.sockets.on('connection', function (socket) {
    socket.on('HUElights', function (connections) {
    console.log("Hue Online");
    })
    //--------------------------Toogle Light on Off-----------------------------//
    //Name of Button function = DayNight //
    io.sockets.on('connection', function (socket) {
    socket.on('DayNight', function(DayNight){
    console.log(DayNight);
    if (DayNight == false) {
        io.sockets.emit('DayNightFalse');
    }
    else{
        io.sockets.emit('DayNightTrue');
        api.setLightState(1, state.off())
            .done();
        setTimeout(function () {
            api.setLightState(2, state.off())
                .done();
        },5000)
        setTimeout(function () {
            api.setLightState(3, state.off())
                .done();
        },10000)
    }
    });
    });
    //------------------Button Light SLEEPROOM ----------------------------//   
    socket.on('LightOben', function (LightOben) {
    console.log(LightOben);
    if(LightOben == 1){
        api.setLightState(3, state.on())
            .done();
        io.sockets.emit('LightObenTrue');
    }
    else {
        api.setLightState(3, state.off())
            .done();
        io.sockets.emit('LightObenFalse');
    }
    })
    //----------------------Button Light All------------------------    
    socket.on('LightAll', function (lightAll) {
    console.log(lightAll);
    if (lightAll == true) {
        api.setLightState(3, state.on())
        api.setLightState(2, state.on())
        api.setLightState(1, state.on())
            .done();
        io.sockets.emit('LightAllTrue');
    }
    else {
        api.setLightState(3, state.off())
        api.setLightState(2, state.off())
        api.setLightState(1, state.off())
            .done();
        io.sockets.emit('LightAllFalse');
    }
    })
    });
    
    
    
    //------------------Light Event----CheckBox Sun Moon -------------------------------//
    function daynight(id) {
    var SunMoon = document.getElementById(id).checked;
    socket.emit('DayNight', SunMoon);
    }
    socket.on('DayNightFalse', function (DayNight) {
    console.log("False");
        $('#toggle--daynight').prop('checked', false);
    });
    socket.on('DayNightTrue', function () {
    console.log("True");
    $('#toggle--daynight').prop('checked', true);
    $('#toogle-modus').css({'opacity': 0.2}, 1000);
    setTimeout(function () {
        $('#toggle--daynight').prop('checked', false);
        $('#toogle-modus').removeClass("hidden-here");
        $('#toogle-modus').css({'opacity': 0.7}, 1000);
    }, 800)
    });
     
     
    //---------------------------BUTTON------------------------------------------//
    function lightOben() {
    var LightOben = $('input[name="LightOben"]:checked').length;
    console.log(LightOben)
    socket.emit('LightOben', LightOben);
    }
    socket.on('LightObenFalse', function (LightOben) {
    console.log("LightOben False");
    $('input[name="LightOben"]').prop('checked', false);
    document.getElementById('foo').jscolor.hide();
    });
    socket.on('LightObenTrue', function (LightOben) {
    console.log("LightOben True");
    $('input[name="LightOben"]').prop('checked', true);
    document.getElementById('foo').jscolor.show();
    });
    //----------------------------------------------------//
    function lightAll(id) {
    var LightAll = document.getElementById(id).checked;
    console.log(LightAll)
    socket.emit('LightAll', LightAll);
    }
    socket.on('LightAllFalse', function (LightAll) {
    console.log("Light All False");
    $('#LightAll').prop('checked', false);
    });
    socket.on('LightAllTrue', function (LightAll) {
    console.log("Light All True");
    $('#LightAll').prop('checked', true);
    });
    

![](https://hackster.imgix.net/uploads/attachments/178741/SwissRailPasses.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)
    
    
    io.sockets.on('connection', function (socket) {
    socket.on('SBB', function (connections) {
    console.log("Zug- Verbindungen");
    //Erste Verbinndung     var Abfahrt0 = (connections.connections[0].from.departure).toString().substr(11,5)
    var Von0 = (connections.connections[0].from.location.name).toString(1, 8);
    var Gleis0 =(connections.connections[0].from.platform);
    var Ankunft0=(connections.connections[0].to.arrival.toString().substr(11,5))
    //Zweite Verbindung     var Abfahrt1 = (connections.connections[1].from.departure).toString().substr(11,5)
    var Von1 = (connections.connections[1].from.location.name).toString(1, 8);
    var Gleis1 =(connections.connections[1].from.platform);
    var Ankunft1=(connections.connections[1].to.arrival.toString().substr(11,5))
    //Zweite Verbindung     var Abfahrt2 = (connections.connections[2].from.departure).toString().substr(11,5)
    var Von2 = (connections.connections[2].from.location.name).toString(1, 8);
    var Gleis2 =(connections.connections[2].from.platform);
    var Ankunft2=(connections.connections[2].to.arrival.toString().substr(11,5))
    //Zweite Verbindung     var Abfahrt3 = (connections.connections[3].from.departure).toString().substr(11,5)
    var Von3 = (connections.connections[3].from.location.name).toString(1, 8);
    var Gleis3 =(connections.connections[3].from.platform);
    var Ankunft3=(connections.connections[3].to.arrival.toString().substr(11,5))
    switch(Gleis0) {
     case "":
       Gleis0="Tram";
       break;
     default:
       Gleis0=(connections.connections[0].from.platform);
    }
    switch(Gleis1) {
     case "":
       Gleis1="Tram";
       break;
     default:
       Gleis1=(connections.connections[1].from.platform);
    }
    switch(Gleis2) {
     case "":
       Gleis2="Tram";
       break;
     default:
       Gleis2=(connections.connections[2].from.platform);
    }
    switch(Gleis3) {
     case "":
       Gleis3="Tram";
       break;
     default:
       Gleis3=(connections.connections[3].from.platform);
    }
    /*   Erste Verbinndung   */     socket.emit('SBBZEIT0', Abfahrt0);
    socket.emit('SBBGLEIS0', Gleis0);
    socket.emit('SBBANKUNFT0', Ankunft0);
    socket.emit('SBBZEIT1', Abfahrt1);
    socket.emit('SBBGLEIS1', Gleis1);
    socket.emit('SBBANKUNFT1', Ankunft1);
    socket.emit('SBBZEIT2', Abfahrt2);
    socket.emit('SBBGLEIS2', Gleis2);
    socket.emit('SBBANKUNFT2', Ankunft2);
    socket.emit('SBBZEIT3', Abfahrt3);
    socket.emit('SBBGLEIS3', Gleis3);
    socket.emit('SBBANKUNFT3', Ankunft3);
    
    
    
    <!--------------------------- Train Information ------------------------------------>   <div id="transit" style="cursor: pointer">
     <main id="main-train">
        <!--  <input style="display: none !important;" placeholder="Suchen" x-webkit-speech autocomplete="off"  /> -->
          <div class="tabelle-Zug">
              <table>
                  <thead>
                  <tr>
                      <th scope="col">Gleis</th>
                      <th scope="col">Zeit</th>
                      <th scope="col">Ankunft</th>
                      <th scope="col">Verspätung</th>
                  </tr>
                  </thead>
                  <tbody>
              <tr>
                  <td scope="row" data-label="Account"> <span id="SbbGleis0">    Laden..</span></td>
                  <td data-label="Amount">              <span id="SbbZeit0">     Laden.. </span></td>
                  <td>                                   <span id="SbbAnkunft0"> Laden..</span> </td>
                  <td>                                   <span id=""></span> </td>
              </tr>
              <tr>
                  <td scope="row" data-label="Account"> <span id="SbbGleis1">    Laden..</span></td>
                  <td data-label="Amount">              <span id="SbbZeit1">     Laden.. </span></td>
                  <td>                                   <span id="SbbAnkunft1"> Laden..</span> </td>
                  <td>                                   <span id="."></span> </td>
              </tr>
              <tr>
                  <td scope="row" data-label="Account"> <span id="SbbGleis2">    Laden..</span></td>
                  <td data-label="Amount">              <span id="SbbZeit2">     Laden.. </span></td>
                  <td>                                   <span id="SbbAnkunft2"> Laden..</span> </td>
                  <td>                                   <span id=".."></span> </td>
              </tr>
              <tr>
                  <td scope="row" data-label="Account"> <span id="SbbGleis3">    Laden..</span></td>
                  <td data-label="Amount">              <span id="SbbZeit3">     Laden.. </span></td>
                  <td>                                   <span id="SbbAnkunft3"> Laden..</span> </td>
                  <td>                                   <span id="..."></span> </td>
              </tr>
                  </tbody>
                  </table>
      </div>
      </main>
    </div>
    /* Javascript SBB */
    <script type="text/javascript">var socket = io('http://192.168.0.53:8080');
    function onload() {
    // ------------------------------------- SBB------------------------------------//        $.getJSON('http://transport.opendata.ch/v1/connections?from=europaplatz+bern&to=bern', function (connections) {
          socket.emit('SBB', connections);
          console.log(connections.connections[0].from.platform);
      });
      //
      socket.on('SBBZEIT0',   function      (data)  {document.getElementById    ("SbbZeit0").innerHTML = data;});
      socket.on('SBBGLEIS0',  function     (data)  {document.getElementById    ("SbbGleis0").innerHTML = data;});
      socket.on('SBBANKUNFT0',function   (data)  {document.getElementById    ("SbbAnkunft0").innerHTML = data;});
      socket.on('SBBZEIT1',   function      (data)  {document.getElementById    ("SbbZeit1").innerHTML = data;});
      socket.on('SBBGLEIS1',  function     (data)  {document.getElementById    ("SbbGleis1").innerHTML = data;});
      socket.on('SBBANKUNFT1',function   (data)  {document.getElementById    ("SbbAnkunft1").innerHTML = data;});
      socket.on('SBBZEIT2',       function      (data)  {document.getElementById    ("SbbZeit2").innerHTML = data;});
      socket.on('SBBGLEIS2',      function     (data)  {document.getElementById    ("SbbGleis2").innerHTML = data;});
      socket.on('SBBANKUNFT2',    function   (data)  {document.getElementById    ("SbbAnkunft2").innerHTML = data;});
      socket.on('SBBZEIT2', function      (data)  {document.getElementById    ("SbbZeit2").innerHTML = data;});
      socket.on('SBBGLEIS2', function     (data)  {document.getElementById    ("SbbGleis2").innerHTML = data;});
      socket.on('SBBANKUNFT2', function   (data)  {document.getElementById    ("SbbAnkunft2").innerHTML = data;});
      socket.on('SBBZEIT3', function      (data)  {document.getElementById    ("SbbZeit3").innerHTML = data;});
      socket.on('SBBGLEIS3', function     (data)  {document.getElementById    ("SbbGleis3").innerHTML = data;});
      socket.on('SBBANKUNFT3', function   (data)  {document.getElementById    ("SbbAnkunft3").innerHTML = data;});
      socket.on('SBBZEIT4', function      (data)  {document.getElementById    ("SbbZeit4").innerHTML = data;});
      socket.on('SBBGLEIS4', function     (data)  {document.getElementById    ("SbbGleis4").innerHTML = data;});
      socket.on('SBBANKUNFT4', function   (data)  {document.getElementById    ("SbbAnkunft4").innerHTML = data;});
    }
    
