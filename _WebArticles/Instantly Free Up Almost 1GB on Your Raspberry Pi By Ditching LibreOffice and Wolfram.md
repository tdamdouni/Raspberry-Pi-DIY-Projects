# Instantly Free Up Almost 1GB on Your Raspberry Pi By Ditching LibreOffice and Wolfram

_Captured: 2016-04-29 at 23:39 from [lifehacker.com](http://lifehacker.com/instantly-free-up-almost-1gb-on-your-raspberry-pi-by-di-1773831271?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+lifehacker%2Ffull+%28Lifehacker%29)_

![Instantly Free Up Almost 1GB on Your Raspberry Pi By Ditching LibreOffice and Wolfram](http://i.kinja-img.com/gawker-media/image/upload/s--d7sHXptf--/bg8ktpeckimibr3cwozn.png)

One of the really nice things about the newest builds of Raspbian is that it comes with just about all the software you need to get running. The downside of that is that all that software takes up a ton of space. RasPi.tv points out you can quickly snag about a 1GB back by deleting two apps: LibreOffice and Wolfram.

Obviously deleting apps frees up space, that's not a surprise to anyone, but it's easy to forget how important this is when you're working with an operating system that runs off a MicroSD card. Every little bit of space matters in this case, and if you're new to Linux or the Raspberry Pi, you might not know how exactly to go about freeing up space.

LibreOffice takes up around 250MB, while Wolfram clogs up about 650MB. This means they're too of the bigger space hogs on the Pi. Obviously, if you're using these programs, don't delete them. But if you aren't, getting rid of them is super easy. Just run these commands to get of Wolfram:
    
    
    sudo apt-get purge wolfram-engine  
    sudo apt-get clean  
    sudo apt-get autoremove  
    

You can do the same for LibreOffice by substituting `libreoffice*` in for `wolfram-engine` above. Other space wasting culprits could include `minecraft-pi` and `sonic-pi`. Of course, if you don't want _any _additional software, just use the [Raspbian Lite image](https://www.raspberrypi.org/downloads/raspbian/) from the get-go. The Lite image just includes the necessities to run Raspbian without any of the extra apps.

[How to Free Up Some Space On You Raspbian SD Card? Remove Wolfram and LibreOffice](http://raspi.tv/2016/how-to-free-up-some-space-on-your-raspbian-sd-card-remove-wolfram-libreoffice) | Raspi-TV
