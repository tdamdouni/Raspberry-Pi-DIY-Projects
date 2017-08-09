# Configuring a Raspberry Pi as an always-on dashboard

_Captured: 2017-08-05 at 17:33 from [medium.com](https://medium.com/pmb-digital/configuring-a-raspberry-pi-as-an-always-on-dashboard-dd734a7c7eb0?source=userActivityShare-c79006fee040-1501947194)_

![](https://cdn-images-1.medium.com/max/2000/1*VZj48FaqRvMwUqE68kyBow.jpeg)

# Configuring a Raspberry Pi as an always-on dashboard

The Raspberry Pi makes for an excellent and cheap PC to hook up to an HDMI screen as a dashboard. However, when setting it up there are a couple of things you can do to make your life easier. This is a collection of tips that I gathered from around the Interwebs as I went through the process of setting one up for my office so that it booted up directly into the dashboard without any intervention from my part (besides adding power)

#### Boot to Desktop

Assuming you don't want to monitor an ncurses based application in a terminal, you'll probably want a web browser. Set up the Pi to boot directly into Desktop mode:
    
    
    sudo raspi-config

#### Protect your proxy authentication details

If like me, you work on a corporate network, there's a good chance you'll have a proxy server of some kind that you need to authenticate to. Leaving your login details lying about in a plain text file or environment variable is never a good idea, so use [Cntlm](http://cntlm.sourceforge.net) to protect them.

To install Cntlm you'll need to use your corporate proxy server initially, so create the environment variable:
    
    
    export http_proxy=http://loginname:password@yourproxy:8080

(it will be cleared when you next reboot, so just remember to do that)

Then, install Cntlm:
    
    
    sudo apt-get install cntlm

Once Cntlm is installed, edit the config file at _/etc/cntlm.conf_ and update the _Username_, _Domain_ and _Proxy_ settings:
    
    
    Username yourlogin  
    Domain yourdomain  
    Proxy yourcorporateproxy:8080

Save the file, exit to the shell and run cntlm to generate the keys that you need:
    
    
    sudo cntlm -v -H -c /etc/cntlm.conf

You'll be prompted for your proxy server password, enter that and Cntlm will return three encrypted keys. The three lines are _PassLM_, _PassNT_ and _PassNTLMv2_, each followed by a 32 character string. Copy these three lines and paste them into your cntlm.conf file. You can now restart Cntlm:
    
    
    sudo service restart cntlm

To configure the proxy server settings for the shell, edit the _/etc/environment_ file and add this line:
    
    
    export http_proxy=http://127.0.0.1:3128

You can now configure _apt_ to use this proxy server -- edit the _/etc/apt/apt.conf.d/10proxy_ file and add this line:
    
    
    Acquire::http::proxy “http://127.0.0.1:3128/";

You can now use <http://127.0.0.1:3128> as your proxy server in all applications and Cntlm will proxy the authenticated requests for you.

#### Loading Chromium at startup in kiosk mode

If you're displaying a dashboard of some kind, chances are you've built it as a web application. Using [Chromium](http://www.chromium.org/Home) in Kiosk mode will give you the latest browser support. First, install Chromium:
    
    
    sudo apt-get install chromium

Then, edit the _/etc/xdg/lxsession/LXDE/autostart_ file and add the following line:
    
    
    @chromium —-proxy-server=127.0.0.1:3128 —-kiosk <http://yourapp>

#### Disabling screen blank

Since this is a dashboard screen (and won't have a keyboard and mouse attached) you need to make sure that the screen doesn't blank due to inactivity. First install these utils:
    
    
    sudo apt-get install unclutter x11-xserver-utils

Then, again edit the _/etc/xdg/lxsession/LXDE/autostart_ file and add the following lines:
    
    
    @xset s off  
    @xset -dpms  
    @xset s noblank

If your autostart file has a line for the screen saver, comment it out.

#### Removing the Session Restore prompt

At some point you'll lose power to the Pi, and when it boots back up Chromium will pop a helpful message at the top of the screen about an unsafe shutdown and offering to restore your session. With no mouse attached this can be pretty annoying.

Add the following to you .profile to help Chromium forget that you didn't shut down correctly:
    
    
    sed -i 's/\("exited_cleanly": *\)false,/\1true,/' .config/chromium/Default/Preferences
