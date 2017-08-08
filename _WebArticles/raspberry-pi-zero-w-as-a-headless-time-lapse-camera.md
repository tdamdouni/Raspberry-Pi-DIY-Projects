# Raspberry Pi Zero W as a headless time-lapse camera

_Captured: 2017-05-21 at 10:48 from [www.jeffgeerling.com](https://www.jeffgeerling.com/blog/2017/raspberry-pi-zero-w-headless-time-lapse-camera)_

> **tl;dr**: There are many ways to capture time-lapse videos. But this one is cheap, completely wireless, and mine. If you want to skip the post and go straight for the glory, grab a copy of my [Time-lapse app for the Raspberry Pi](https://github.com/geerlingguy/pi-timelapse).

Time-lapses transform subtle, slow processes into something beautiful, and often make us think about things in new ways. For example, have you ever thought about just how heavy a wet snow is? The trees in your yard might know a thing or two about that! Check out a time-lapse I recorded this morning some mighty oak tree branches, as they relaxed upward as if in relief from the wet snow falling off:

Quality time-lapse photography used to require expensive equipment special knowledge, so it remained the domain of the specialist. Fast forward to 2017, and we have a $10 computer and a $30 camera that can create a wireless time-lapse device that can produce footage in any modern resolution--even up to 4K! Sure there are many cameras with built in intervalometers and lenses you can use to make more creative images... but would you be willing to leave your expensive equipment in places or situations where you risk damaging them? $50 of equipment, maybe... $1000+, no way! (At least, not for fun and exploration.)

The Raspberry Pi has freed me to think in new directions for computing (for example, check out my [Raspberry Pi Dramble](http://www.pidramble.com) project), and it's also allowing me to expand my photography horizons. And if you want to tinker as well, all you need is this little guy:

![Raspberry Pi Zero with Camera Cable and microSD card](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/images/raspberry-pi-zero-w-with-camera-cable-and-microsd-card.jpg)

_The Raspberry Pi Zero W._

For _this_ year's [Pi Day](http://www.piday.org) (3.14), I decided to grab a Raspberry Pi Zero W from Micro Center, write up a small app, and record time-lapses. And I've decided to open source all my work, and share this blog post so you, too, can enjoy watching life in fast-forward!

## Requirements

There are some programs you can download that are more automated, but (a) they usually require the use of a keyboard and monitor (which we don't want to use), and (b) they usually consume more power (meaning less battery life) and are less customizable than I desire.

Here are the things I wanted to have:

  * 100% portable--doesn't have to be plugged into mains electricity.
  * Stable, custom exposure and color control (so the video doesn't flicker).
  * Easy assembly of footage after the time-lapse is captured (to a gif or a video).
  * Reliable timing (so I can calculate how many frames/how much time-warp factor to record).

So for starters, I made sure I had the right hardware on hand. I'll run through my parts list, then explain the setup process below.

## Parts needed

![Raspberry Pi Zero W Time-Lapse portable AUKEY battery pack](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/images/raspberry-pi-w-time-lapse-portable-aukey-battery.jpg)

  * [MicroSD card](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1489459938&sr=1-1&keywords=samsung+evo+microsd&linkCode=ll1&tag=mmjjg-20&linkId=b40f0fe88f33fc4032c1ca9126e79d9a) (bigger is better--but [read my comprehensive microSD benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards) for some important caveats!)
  * USB battery power supply (I use the [AUKEY 30,000 mAh](https://www.amazon.com/AUKEY-30000mAh-Portable-Charger-Micro-USB/dp/B01F8IRIN0/ref=as_li_ss_tl?ie=UTF8&qid=1489466317&sr=8-1&keywords=aukey+30000+battery&linkCode=ll1&tag=mmjjg-20&linkId=35ca778b230c25ec01f79846dab973de) power supply, but any rated at 10,000 mAh or more will go for days)
  * (Optional) camera case (I like the one Adafruit sells, but any will do--helpful in rigging the camera, since it needs to be still!)
  * Another computer to use to set things up and view the results
  * A WiFi network (this allows the rig to be fully portable and remote-controllable)

## Setting things up

I'll assume you're using a Mac for the setup process, but you can do the same thing on Windows if you use Ubuntu Bash or some other command line emulator that allows SSH access... and if you use Linux, you're golden--just pop open a Terminal window and follow along!

In this guide, we'll set up the Raspberry Pi _headless_--you don't need an extra monitor, keyboard, and mouse to plug into the Pi (nor do you need all the extra adapter cables to get it all hooked up!)

### Put Raspbian on the microSD card

  1. Mount the microSD card (I use a microSD to SD adapter, then plug that into my USB SD card reader) on your Mac.
  2. [Download Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) (either as a .torrent or the direct .img download).
  3. Open Terminal, run `diskutil list` to see all connected volumes.
  4. Note the microSD card path (usually `/dev/disk2` or `/dev/disk3`).
  5. Unmount the microSD card: `diskutil unmountDisk /dev/disk2`
  6. Write the image you downloaded to the card: `sudo dd if=~/Downloads/2017-03-02-raspbian-jessie-lite.img of=/dev/rdisk2 bs=1m` (should take a minute or less if you have a decent microSD card)

### Initialize SSH and WiFi configuration.

  1. Open the `boot` volume on your Mac (should auto mount after the disk image is finished writing).
  2. Create an `ssh` file to [tell the Pi to enable SSH when it boots up](https://www.raspberrypi.org/documentation/remote-access/ssh/) by default: `touch /Volumes/boot/ssh`
  3. Create a `wpa_supplicant.conf` file to tell the Pi to connect to your WiFi network on boot. Create a new file with that title in the `boot` volume, with the contents below:
    
        network={
        ssid="YOUR_SSID"
        psk="YOUR_PASSWORD"
        key_mgmt=WPA-PSK
    }
    

  4. Eject the microSD card, and stick it in the Raspberry Pi.

At this point, the Pi is fresh and new, and will boot up and connect to your WiFi network, allowing you to administer it via SSH.

### Connect to the Pi

Assuming your WiFi network uses DHCP to assign IP addresses to devices (this is almost universally true), you need to figure out the IP address your Pi acquired when it booted. Use one of the following two options:
    
    
    # Use nmap.
    $ sudo nmap -sP 10.0.1.1/24
    
    # Use Fing.
    $ brew install fing
    $ sudo fing 10.0.1.1/24
    

(Note: Check your computer's local network IP address--if it's something like `192.168.0.x`, then you need to use `192.168.0.1/24` instead of `10.0.1.1/24`.)

Either of these options will scan the network for a bit, then output a list of Host addresses and MAC/Hardware addresses. `nmap` additionally prints human-readable manufacturer labels, so it's even easier to identify devices labeled with `(Raspberry Pi Foundation)` on your network!

Once you have found the Pi's IP address, log into it: `ssh pi@[IP-ADDRESS-HERE]` (the default password is `raspberry`). Since this is the first time the Pi is being used, it needs to be configured:

  1. `sudo raspi-config`
  2. Set a new password (first option in the list).
  3. Set a hostname (e.g. `pi-zero-timelapse`).
  4. Go to 'Interfacing Options', then 'Camera', then choose 'Yes' to enable the camera interface.
![Raspberry Pi Zero raspi-config Terminal SSH configure hostname](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/images/enter-hostname-pi-zero-raspi-config.png)

_Aren't the graphics amazing?_

## Create your own Time Lapse script

Now that the Pi is set up, and you're connected to it, you need to install a few libraries so you can call them in your Python time-lapse script:
    
    
    sudo apt-get install -y python-picamera python-yaml imagemagick
    

Then create a script named `timelapse.py` (`nano timelapse.py` to open it in the nano text editor), with the contents:

`from picamera import PiCamera  
  
camera = PiCamera()  
camera.capture('image.jpg')`

This is basically how the guide in Raspberry Pi's official documentation works ([Time-lapse animations with a Raspberry Pi](https://www.raspberrypi.org/learning/timelapse-setup/worksheet/)). But at this point, we want to go a bit deeper, and have a more flexible way to control the timelapse--the length, the exposure settings, color temperature, etc.

To that end, I've built a little Python app (really, it's a glorified script... but nowadays everyone calls anything resembling software an 'App', so I might as well, too) that you can download from GitHub to have greater control over your time-lapses!
    
    
    <!doctype html><html><body><style type="text/css">body{padding:0;margin:0;font-size:14px;font-family:"Helvetica Nenu",Hevetica,Arial,sans-serif;overflow:hidden}body.ready{border:1px solid #eee;border-radius:5px;border-color:#eee #ddd #bbb;box-shadow:rgba(0,0,0,.14) 0 1px 3px}.github-card{border-radius:5px;padding:8px 8px 0;background:#fff;color:#555;position:relative}.github-card a{text-decoration:none;color:#4183c4;outline:0}.github-card a:hover{text-decoration:underline}.github-card .header{position:relative}.github-card .button{position:absolute;top:0;right:0;padding:4px 8px 4px 7px;color:#555;text-shadow:0 1px 0 #fff;border:1px solid #d4d4d4;border-radius:3px;font-size:13px;font-weight:700;line-height:14px;background-color:#e6e6e6;background-image:-webkit-linear-gradient(#fafafa,#eaeaea);background-image:-moz-linear-gradient(#fafafa,#eaeaea);background-image:-ms-linear-gradient(#fafafa,#eaeaea);background-image:linear-gradient(#fafafa,#eaeaea)}.github-card .button:hover{color:#fff;text-decoration:none;background-color:#3072b3;background-image:-webkit-linear-gradient(#599bdc,#3072b3);background-image:-moz-linear-gradient(#599bdc,#3072b3);background-image:-ms-linear-gradient(#599bdc,#3072b3);background-image:linear-gradient(#599bdc,#3072b3);border-color:#518cc6 #518cc6 #2a65a0;text-shadow:0 -1px 0 rgba(0,0,0,.25)}.user-card .header{padding:3px 0 4px 57px;min-height:48px}.user-card .header a{color:#707070;text-decoration:none}.user-card .header a:hover strong{text-decoration:underline}.user-card img{position:absolute;top:0;left:0;width:48px;height:48px;background:#fff;border-radius:4px}.user-card strong{display:block;color:#292f33;font-size:16px;line-height:1.6}.user-card ul{text-transform:uppercase;font-size:12px;color:#707070;list-style-type:none;margin:0;padding:0;border-top:1px solid #eee;border-bottom:1px solid #eee;zoom:1}.user-card ul:after{display:block;content:'';clear:both}.user-card .status a{color:#707070;text-decoration:none}.user-card .status a:hover{color:#4183c4}.user-card .status li{float:left;padding:4px 18px;border-left:1px solid #eee}.user-card .status li:first-child{border-left:0;padding-left:0}.user-card .footer{font-size:12px;font-weight:700;padding:11px 0 10px;color:#646464}.user-card .footer a{color:#646464}.repo-card .header{padding:3px 0 4px 57px}.repo-card .avatar,.repo-card .avatar img{position:absolute;top:0;left:0;width:48px;height:48px;background:#fff;border-radius:4px}.repo-card .header a{color:#707070}.repo-card .header strong{display:block;font-size:18px;line-height:1.4}.repo-card .header strong a{color:#292f33}.repo-card .header sup{font-size:10px;margin-left:3px;color:#797979}.repo-card .content{padding:6px 0 10px}.repo-card .content p{margin:0 5px 0 0;font:18px/24px Georgia,"Times New Roman",Palatino,serif;overflow:hidden;clear:both;word-wrap:break-word}.repo-card .footer{border-top:1px solid #eee;padding:8px 0 6px}.repo-card .status{font-size:10px;padding-right:10px;text-transform:uppercase}.repo-card .status strong{font-size:12px;padding-right:5px}</style><script id="user-card" type="text/template"><div class="header"><a class="avatar" href="https://github.com/{login}"><img src="{avatar_url}&s=48"><strong>{name}</strong><span>@{login}</span></a><a class="button" href="https://github.com/{login}">Follow</a></div><ul class="status"><li><a href="https://github.com/{login}?tab=repositories"><strong>{public_repos}</strong>Repos</a></li><li><a href="https://gist.github.com/{login}"><strong>{public_gists}</strong>Gists</a></li><li><a href="https://github.com/{login}/followers"><strong>{followers}</strong>Followers</a></li></ul><div class="footer">{job}</div></script><script id="repo-card" type="text/template"><div class="header"><a class="avatar" href="https://github.com/{login}"><img src="{avatar_url}&s=48"></a><strong class="name"><a href="https://github.com/{full_name}">{name}</a><sup class="language">{language}</sup></strong><span>{action}<a href="https://github.com/{login}">{login}</a></span><a class="button" href="https://github.com/{full_name}">Star</a></div><div class="content"><p>{description}{homepage}</p></div><div class="footer"><span class="status"><strong>{forks_count}</strong>Forks</span><span class="status"><strong>{watchers_count}</strong>Stars</span></div></script><script>function querystring(){var e=window.location.href,r;var t=e.slice(e.indexOf("?")+1).split("&");var a=[];for(i=0;i<t.length;i++){r=t[i].split("=");a.push(r[0]);a[r[0]]=r[1]}return a}var qs=querystring();(function(e){var r="https://api.github.com/",t;function a(e,r){try{if(window.localStorage){if(r){r._timestamp=(new Date).valueOf();localStorage[e]=JSON.stringify(r)}else{var t=localStorage[e];if(t){return JSON.parse(t)}return null}}}catch(a){}}function n(e,r){var t=e;var a=r.split(".");for(var n=0;n<a.length;n++){if(t){t=t[a[n]]}else{break}}if(t===undefined||t===null){return""}return t}function i(r,a){var i=e.getElementById(r+"-card");var s=/{([^}]+)}/g;var o=i.innerHTML;var l=o.match(s);for(t=0;t<l.length;t++){o=o.replace(l[t],n(a,l[t].slice(1,-1)))}return o}function s(e,r){var t=a(e);if(t&&t._timestamp){if((new Date).valueOf()-t._timestamp<1e4){return r(t)}}if(qs.client_id&&qs.client_secret){e+="?client_id="+qs.client_id+"&client_secret="+qs.client_secret}var n=new XMLHttpRequest;n.open("GET",e,true);n.onload=function(){r(JSON.parse(n.response))};n.send()}function o(r,a){var n=r.getElementsByTagName("a");for(t=0;t<n.length;t++){(function(e){e.target="_"+(qs.target||"top")})(n[t])}e.body.appendChild(r);e.body.className="ready";if(parent!==self&&parent.postMessage){var i=Math.max(e.body.scrollHeight,e.documentElement.scrollHeight,e.body.offsetHeight,e.documentElement.offsetHeight,e.body.clientHeight,e.documentElement.clientHeight);parent.postMessage({height:i,sender:qs.identity||"*"},"*")}}function l(t){var n=r+"users/"+t;s(n,function(r){r=r||{};var s=r.message;var l="0";if(s){r=a(n)||r;l="?"}else{a(n,r)}r.login=t;r.name=p(r.name);r.public_repos=f(r.public_repos)||l;r.public_gists=f(r.public_gists)||l;r.followers=f(r.followers)||l;var c="Not available for hire.";if(r.hireable){var u="";if(r.email){u="mailto:"+r.email}else if(r.blog){u=r.blog}else{u=r.html_url}c='<a href="'+u+'">Available for hire.</a>'}if(s){c=s}r.job=c;var g=e.createElement("div");g.className="github-card user-card";g.innerHTML=i("user",r);o(g)})}function c(t,n){var l=r+"repos/"+t+"/"+n;s(l,function(r){r=r||{};var n=r.message;var s="0";if(n){r=a(l)||r;s="?"}else{a(l,r)}r.login=t;r.avatar_url="";if(r.owner&&r.owner.avatar_url){r.avatar_url=r.owner.avatar_url}r.forks_count=f(r.forks_count)||s;r.watchers_count=f(r.watchers_count)||s;if(r.fork){r.action="Forked by "}else{r.action="Created by "}var c=r.description;if(!c&&r.source){c=r.source.description}if(!c&&n){c=n}r.description=p(c)||"No description";var u=r.homepage;if(!u&&r.source){u=r.source.homepage}if(u){r.homepage=' <a href="'+u+'">'+u.replace(/https?:\/\//,"").replace(/\/$/,"")+"</a>"}else{r.homepage=""}var g=e.createElement("div");g.className="github-card repo-card";g.innerHTML=i("repo",r);o(g)})}function u(){}function f(e){if(!e)return null;if(e===1e3)return 1;if(e<1e3)return e;e=e/1e3;if(e>10)return parseInt(e,10)+"k";return e.toFixed(1)+"k"}if(!qs.user){u()}else if(qs.repo){c(qs.user,qs.repo)}else{l(qs.user)}function p(e){return e.replace(/</g,"&lt;").replace(/>/g,"&gt;")}})(document);(function(e,r,t,a,n,i,s){e["GoogleAnalyticsObject"]=n;e[n]=e[n]||function(){(e[n].q=e[n].q||[]).push(arguments)},e[n].l=1*new Date;i=r.createElement(t),s=r.getElementsByTagName(t)[0];i.async=1;i.src=a;s.parentNode.insertBefore(i,s)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create","UA-21475122-2","auto");var t=qs.user;if(qs.repo)t+="/"+qs.repo;ga("send","pageview",{title:t});</script></body></html>

## Going deeper

With the `pi-timelapse` app, you can build timelapses like the one at the top of this post pretty easily. Some of the features I've built so far include:

  * Easy configuration via a `config.yml` file
  * Resolution control
  * Intervalometer control (number of images and interval between images)
  * Ability to generate an animated gif or an mp4 video after capture is complete (experimental)
  * Manual exposure control (optional): ISO, shutter speed, and white balance

Here's how to set things up:

  1. Change directories into the `pi` user's home directory: `cd ~` (the tilde means 'home', which is `/home/pi` in this case).
  2. Download the project: `git clone https://github.com/geerlingguy/pi-timelapse.git`
  3. Change directories into the `pi-timelapse` directory: `cd pi-timelapse`
  4. Create your configuration file: `cp example.config.yml config.yml` (this copies the example file to `config.yml`).
  5. Configure the time-lapse: `nano config.yml` (in the nano editor, Ctrl-O saves ('writes out') the file, and Ctrl-X exits).
  6. Start a time-lapse: `python timelapse.py`

After the number of frames you configured have been captured, there will be a folder named `series-[date-and-time]` in the directory with the pi-timelapse project. That directory contains all the images that were captured, numbered in a sequence like `image00001.jpg`, `image00002.jpg`, etc. And if you configured a gif or video to be created, then you'll see a `.gif` and/or `.m4v` video in the pi-timelapse project directory too.

You can use `ls` to display the contents of the directory, and `cd [folder]` to go into a folder, or `cd ..` to go back one directory.

At this point, if you want to view these things, you'll either need to [use `scp` to copy a file from the Pi to your computer](http://unix.stackexchange.com/a/188289), or use an FTP client that works with SFTP (I use [Transmit](https://panic.com/transmit/), but [Cyberduck](https://cyberduck.io/) is a great, free alternative).

## More Examples

Here's a video I shot at 1 frame every 15 seconds of cirrus clouds in the sky in front of my house:

And a shot of an earlier snow melting (as it was falling!) in my backyard:

And here's a gif I captured of myself, showing one of the risks of working at an adjustable-height standing desk:

![Standing Desk Problems - Animated Gif](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/images/gif-standing-desk-problems.gif)

I haven't had time to build any more elaborate time-lapses, mostly because they often take hours (or days!), depending on what I'm trying to capture, and I've still been honing the software in the short term.

## Summary

Grab the [Raspberry Pi Time-Lapse App](https://github.com/geerlingguy/pi-timelapse) from GitHub, and start making some time-lapses of your own!

My next steps are:

  * Build a weatherproof enclosure that I can lock down to a post or otherwise secure outdoors, so I can record more of the nature around the house.
  * Optimize the software so I can deliver videos directly to places like Dropbox or a network share (right now I have to SCP the files to my computer).
  * Test other Pi models (Pi 3, Pi 2, etc.) to see how they fare in terms of power consumption vs. efficiency for shorter time-lapses.

And if you're interested in getting into the nitty-gritty, check out the [contents of the `timelapse.py` script](https://github.com/geerlingguy/pi-timelapse/blob/master/timelapse.py), and read the [official `picamera` module documentation](http://picamera.readthedocs.io/en/release-1.10/api_camera.html) for a ton of useful background information.
