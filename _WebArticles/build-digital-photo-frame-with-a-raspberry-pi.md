# Build digital photo frame with a Raspberry Pi

_Captured: 2018-01-16 at 18:36 from [www.codeproject.com](https://www.codeproject.com/Articles/1223258/Build-digital-photo-frame-with-a-Raspberry-Pi)_

## Introduction

A custom digital photo frame powered by a Raspberry Pi. I'm using Html5 canvas element to display images, along with the weather, time and date information.

## Prerequisites

You need to configure raspberry pi and install an operating system, which I have covered in my previous [article](https://www.codeproject.com/Articles/1221357/Running-a-NET-Core-Web-Crawler-on-a-Raspberry-Pi).

## Using the code

The Html code to display photos, along with the weather, time and date information:
    
    
    <div class="container" style="overflow: hidden;">
            <div class="event">
                <h1 style="margin-bottom: 5px;font-family:Alegreya Sans;text-align: center;"><span style="padding-left:15px;" id="dateHead"></span></h1>
                <h1 style="margin-bottom: 5px;font-family:Alegreya Sans;"><span style="padding-left:15px;" id="weatherHead"></span></h1>
                <h4 style="margin-top: 5px;font-family:Alegreya Sans;"><span style="padding-left:15px;font-size:18px;" id="weatherBody"></span></h4>
                <h1 style="margin-bottom:5px;font-family:Alegreya Sans;text-align: center;"><span id="timeHead"></span></h1>
            </div>
           <canvas id="photoGallery" style="background-color :black;top: 0px;left: 0px;">
                    Your browser does not support the HTML5 canvas tag.
           </canvas>
    </div>

The HTML <canvas> element is used to draw graphics, via JavaScript. Here is the javascript code to load images in canvas.
    
    
    var imgIndex = 0;
    var photoTimer = 10000;
    var weatherTimer = 1000 * 60 * 60;
    var clockTimer = 1000;
    var canvas = document.getElementById('photoGallery');
    var context = canvas.getContext('2d');
    var img = new Image();
    img.src = images[imgIndex];
    img.onload = function () {
          var width = window.innerWidth;
          var height = window.innerHeight;
          context.canvas.width = width;
          context.canvas.height = height;
          context.drawImage(img, 0, 0, width, height);
    };
    
    setClock();
    setInterval(loadPhoto, photoTimer);
    setInterval(getWeather, weatherTimer);
    setInterval(setClock, clockTimer);
    
    function loadPhoto() {
       imgIndex = imgIndex >= images.length ? 0 : ++imgIndex;
       img.src = images[imgIndex];
    }
    
    function setClock() {
      var d = new Date();
      $("#dateHead").html(d.toDateString());
      $("#timeHead").html(d.toLocaleTimeString());
    }
    
    function getWeather() {
     $.simpleWeather({
        location: 'Burlington,CA',
        woeid: '',
        unit: 'c',
        success: function (weather) {
            html = weather.city + ', ' + weather.region + '&nbsp;&nbsp;&nbsp;' + weather.temp + '&deg;' + weather.units.temp;
            $("#weatherHead").html(html);
            html = 'Feel like ' + eval(weather.wind.chill + weather.temp) + '&deg;' + '&nbsp;&nbsp;' + weather.currently + '&nbsp;&nbsp;' +             weather.wind.direction + '&nbsp;&nbsp;' + weather.wind.speed + '&nbsp;&nbsp;' + weather.units.speed;
            $("#weatherBody").html(html);
        },
        error: function (error) {
            $(".weather").html('<p>' + error + '</p>');
        }
      });
    
    $(function () {
        getWeather();
    });

The above code snippet uses jquery [simpleweather](http://simpleweatherjs.com/) plugin to display weather information for a given location. Currently, I'm displaying photos from flicker, however, Google photos, Calendar or flicker API can be integrated, which i will cover in next article. Also, i'm using weather location 'Burlington,CA', which can be pulled using HTML5 [Geolocation API.](https://www.w3schools.com/html/html5_geolocation.asp) Here is our html output.

![](https://www.codeproject.com/KB/Raspberry-Pi/1223258/gal1.PNG)

## Setup Raspberry Pi

The Raspberry Pi setup has been covered in my [previous article](https://www.codeproject.com/Articles/1221357/Running-a-NET-Core-Web-Crawler-on-a-Raspberry-Pi) here. Next, we will install the NGINX web server in Raspberry Pi. First install the nginx package by typing the following command in to the Terminal:
    
    
    sudo apt-get install nginx

Next, we will replace nginx default page with our code either using ftp or in terminal.
    
    
    sudo nano /var/www/html/index.nginx-debian.html

and start the server with:
    
    
    sudo /etc/init.d/nginx start

Now, launch the page in raspberry pi chromium by typing http://localhost, in a browser you can enter Fullscreen mode by pressing the F11 key on the keyboard. Here is my demo below.

![](https://www.codeproject.com/KB/Raspberry-Pi/1223258/photo1.PNG)

![](https://www.codeproject.com/KB/Raspberry-Pi/1223258/photo2.PNG)

## Points of Interest

I will be covering integration with Google photos, Calendar or flicker API in next article.
