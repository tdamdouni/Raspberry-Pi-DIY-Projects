# Build a homemade spying machine with a Raspberry-Pi, Firebase, AngularJS and some Python

_Captured: 2017-08-05 at 17:31 from [medium.com](https://medium.com/@rotemtam/build-a-homemade-spying-machine-with-a-raspberry-pi-firebase-and-some-python-9ef74bec301c?source=userActivityShare-c79006fee040-1501947054)_

# Build a homemade spying machine with a Raspberry-Pi, Firebase, AngularJS and some Python

![](https://cdn-images-1.medium.com/max/1200/1*3T9bYd_VQJDbdULDNtph-Q.jpeg)

My favorite characters in spy movies were always the gadget-making-mad-scientists building crazy little machines which help the spy-hero to pull off his amazing feats. Q has always been a much more appealing character than Bond to me, as was Donatello over Leonardo as my favorite Ninja-Turtle.

Cheap new hardware and the quickly-growing "maker" mindset give us a small opportunity to step into the shoes of such childhood heroes.

In this article, I will show you how to build a nifty little device that will allow you to monitor which wifi-enabled devices are present in your home, even when you're away. We'll be building a web-based app which we'll use to view this data from anywhere we have an internet connection. This way you have your Bond-like little device in which you can check up devices which are close to anywhere where you can give it some electricity.

> Disclaimer: this article is created for educational purposes, do not spy on your friends and family as it is unfriendly and immoral! (it may also be illegal)

As you may well know, your smartphone or tablet are constantly looking for known WiFi networks as they do so they send over radio waves unencrypted messages known as "Probe" messages to check if any of the wifi networks which they are already familiar with are around. Different devices behave differently, some probe for networks constantly in the background, while other do this only when you open the screen and try to use the internet. The thing that's interesting to us in this project is that while your device probes for wifi networks it broadcasts it's MAC-address (a uniqe number identifying itself). If we're able to listen to these communications, we'll be able to log who is physically around us, since most people constantly carry their smartphone with them.

#### Our setup

This is how we're going to pull this off:

  * We will set up a Raspberry Pi B+ with a WiFi dongle
  * We will run airodump-ng on our Pi in the background to listen for probe messages
  * We will write a small python program to process the out from airodump and send it to a Firebase database
  * We will write a small web-client to read realtime data from Firebase and show us which devices are near our Pi or have been recently.

#### Setting up your Pi to monitor for probe messages

In order to monitor probe messages we'll be using a tool called [airodump-ng](http://www.aircrack-ng.org/doku.php?id=airodump-ng&DokuWiki=95560e9f99bfee4d78e81aa1436e2cf1), which is a part of the [aircrack-ng](http://www.aircrack-ng.org/) suite used for all sorts of wifi-related functions (such as cracking the key of password-protected wifi networks). Let's install it.

wget http://download.aircrack-ng.org/aircrack-ng-1.2-beta3.tar.gz

sudo apt-get -y install libssl-dev libnl-genl-3-dev libnl-3-dev iw

tar -zxvf aircrack-ng-1.2-beta3.tar.gz

cd aircrack-ng-1.2-beta3/

make

sudo make install
[view raw](https://gist.github.com/rotemtam/1e08f6b73befd5faef81/raw/d814ff4349d824d5f73ccf2aaca1c117f3542bdc/airodump-on-pi) [airodump-on-pi](https://gist.github.com/rotemtam/1e08f6b73befd5faef81#file-airodump-on-pi) hosted with ❤ by [GitHub](https://github.com)

> _<https://gist.github.com/rotemtam/1e08f6b73befd5faef81>_

For the purpose of this article, I assume that you have a Wifi dongle which supports "monitor-mode" and that it's set up on the interface "wlan0". We create the following shell script which will basically put your wifi dongle in monitoring mode and then activate airodump-ng and tell it to save all output to a .csv file in your /tmp folder.

#!/bin/bash

# put wlan0 in monitoring mode

sudo airmon-ng start wlan0 

# activate airodump and have it output data to /tmp directory

sudo airodump-ng --output-format csv --write /tmp/capture mon0 
[view raw](https://gist.github.com/rotemtam/e4e0c84d9dd6fbac5ec2/raw/233852b8bd2b123bff6bbec9141840a074a0f557/activate_airodump.sh) [activate_airodump.sh](https://gist.github.com/rotemtam/e4e0c84d9dd6fbac5ec2#file-activate_airodump-sh) hosted with ❤ by [GitHub](https://github.com)

> _<https://gist.github.com/rotemtam/e4e0c84d9dd6fbac5ec2>_

You can run this in the background, using screen for example.

#### Use Python and Firebase to make realtime data available

[Firebase](https://www.firebase.com/) (recently acquired by Google) is a pretty cool product that allows your to create realtime apps very easily. In our project we'll be using python to write data about devices (called "Stations") our Pi will discover using airodump-ng, to a Firebase database and later we'll write a little angularjs-based app to pull this data and display it in realtime. Cool thing about Firebase is that it lets you create save and read data from the cloud without needing to build a server-side cloud-hosted app, say using Django or Rails.

Go ahead and open a new account at Firebase, they have a free "hacker" plan which is more than enough to get you started.

With airodump-ng running in the background, we will use the following python script to continuously poll the .csv file created by it, format it and then use [Mike Huynh's python wrapper for the Firebase RESTful API](https://github.com/mikexstudios/python-firebase) to push the data to our Firebase database.

import subprocess, StringIO, csv

from simplejson import dumps

from firebase import Firebase

from time import sleep, time

# to install Firebase, pip install -e git://github.com/mikexstudios/python-firebase.git#egg=python-firebase

firebase = Firebase('https://<your_app>.firebaseio.com/stations')

def fetch_data():

# get the newest capture.csv file, then use awk to get only Station data

cmd = r"cat /tmp/`ls -Art /tmp | grep capture | tail -n 1` | awk '/Station/{y=1;next}y'"

data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

f = StringIO.StringIO(data)

# convert the data to a list of dict() objects

conv = lambda row: {'station_mac':row[0], 'first_time_seen':row[1], 'last_time_seen':row[2], 'power':row[3]}

data = [row for row in csv.reader(f, delimiter=',') if len(row) != 0]

return [conv(row) for row in data] 

while True:

print firebase.put(fetch_data())

sleep(1)
[view raw](https://gist.github.com/rotemtam/9ca5e26d6989ad7f5da7/raw/07e53a5c6162d6be709ef33661645caac20d52a8/push_data.py) [push_data.py](https://gist.github.com/rotemtam/9ca5e26d6989ad7f5da7#file-push_data-py) hosted with ❤ by [GitHub](https://github.com)

> _<https://gist.github.com/rotemtam/9ca5e26d6989ad7f5da7>_

This script should be running in the background on your Pi as well.

#### Create a simple client to show the data in realtime

![](https://cdn-images-1.medium.com/max/1200/1*T36BlXGC-bnNE8XDBB-55Q.png)

In order to view all the data collected by our Pi via the Internet, we'll create an angularjs based webapp which will display information about devices seen by our Pi. It will only take a few minutes to do with yeoman's [angular-firebase generator](https://www.npmjs.org/package/generator-angularfire).

We won't go step by step in actually creating the app, for which you can get the code at : <https://github.com/rotemtam/pi-mac-monitor> (see instructions in the README), but here's some information about how it works.

The web-app only has one view and a single controller. The controller uses the [angular-fire](https://github.com/firebase/angularFire) plugin, which allows us to have realtime data in our angular $scope, and have the view be update when the data changes on the server.

View:

<table class="table table-striped" ng-if="stations.length">

<thead>

<tr>

<th>Station MAC</th>

<th>First Seen</th>

<th>Last Seen</th>

</tr>

</thead>

<tbody>

<tr ng-repeat="station in stations">

<td>{{station['station_mac']}}</td>

<td>{{station['first_time_seen']}}</td>

<td>{{station['last_time_seen']}}</td>

</tr>

</tbody>

</table>
[view raw](https://gist.github.com/rotemtam/3cc7d46e5ff1bbf4eaaf/raw/29e675199dbd0fa1b8f483abde0ffe97d340fa59/pi-mac-monitor-view-snippet.html) [pi-mac-monitor-view-snippet.html](https://gist.github.com/rotemtam/3cc7d46e5ff1bbf4eaaf#file-pi-mac-monitor-view-snippet-html) hosted with ❤ by [GitHub](https://github.com)

> _<https://gist.github.com/rotemtam/3cc7d46e5ff1bbf4eaaf>_

Controller:

angular.module('monitorApp')

.controller('MonitorCtrl', function ($scope, fbutil, $timeout) {

$scope.stations = fbutil.syncArray('stations', {limit: 15});

// display any errors

$scope.stations.$loaded().catch(alert);

});
[view raw](https://gist.github.com/rotemtam/95b5e84ee9946767435a/raw/85496fff84d8cd46e6255dec9593a6222d06b6fa/pi-mac-monitor.js) [pi-mac-monitor.js](https://gist.github.com/rotemtam/95b5e84ee9946767435a#file-pi-mac-monitor-js) hosted with ❤ by [GitHub](https://github.com)

> _<https://gist.github.com/rotemtam/95b5e84ee9946767435a>_

#### Summary

That's it! in less then an hour you can be spying on your house members from afar! Just kidding, respect people's privacy!

**_Like This Post? _**_Check out __[Ezra_](http://referral.ezra-app.co)_, a new app I'm working on. Ezra gathers responses from people so you don't have to._
