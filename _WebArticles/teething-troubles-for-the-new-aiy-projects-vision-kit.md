# Teething Troubles for the New AIY Projects Vision Kit?

_Captured: 2018-01-03 at 06:14 from [blog.hackster.io](https://blog.hackster.io/teething-troubles-for-the-new-aiy-projects-vision-kit-625ed4e9287a)_

Announced [at the end of November](https://blog.hackster.io/announcing-the-aiy-projects-vision-kit-234505bc6eef) last year, the AIY Projects [Vision Kit](https://aiyprojects.withgoogle.com/vision/) -- the second kit from Google for the Raspberry Pi -- followed closely in the footsteps of their [successful Voice Kit](https://blog.hackster.io/building-voice-controlled-objects-with-googles-aiy-projects-voice-kit-352d3272cede) earlier in the year.

A limited run of 2,000 units of the new kit [made it into the hands of makers](https://twitter.com/pcsforme/status/946824346949115904) just before the New Year, with a full rollout expected in early spring.

![](https://cdn-images-1.medium.com/freeze/max/60/1*kTqlYgKoIA2FyqavuyUrSw.png?q=20)![](https://cdn-images-1.medium.com/max/1600/1*kTqlYgKoIA2FyqavuyUrSw.png)

> _Vision Bonnet mounted on top of a Raspberry Pi Zero and connected to a Camera module. (📷: Alasdair Allan)_

However in the wake of the release, there have been reports of problems from early adopters with both the hardware, and software that accompanied it.

Some of the issues seem to have been caused a last minute change by Google, merging support for both the Voice and Vision Kits [into a single SD card](https://github.com/google/aiyprojects-raspbian/issues/215) image for the Raspberry Pi that would work with both kits.

Unfortunately the late change, shipping just before the holidays, meant that the [latest image](https://dl.google.com/dl/aiyprojects/vision/aiyprojects-2017-12-18.img.xz) initially appears to support only the Voice Kit, with the Vision Kit example code buried several directories down making it [hard to find](https://twitter.com/Growthologist/status/947521710374473728).

There were also [reports](https://twitter.com/pcsforme/status/947258877522972672) that the short flexible ribbon cable connecting the Raspberry Pi to the Vision Bonnet shorted between the 3.3V and GND pins on the camera connector. This was tracked down to an incorrect labelling at the factory. Plugging it into the way the label tells you to shorts the connector. You have to plug it in backwards, with the "Pi" end towards the Bonnet.

Confusion about which way around the ribbon cables should be inserted into the sockets, whether the pins should be facing or away from the PCB, has also lead to exacerbated confusion amongst some people

There has been confusion [around the supported camera versions](https://github.com/google/aiyprojects-raspbian/issues/224) as well. While a lot of makers are still using the older V1.3 camera boards, rather than the newer higher specification V2.1 boards, the Vision Kit only supports the newer boards.

There were also a number of people having problems due to the lack of pre-soldered 40-pin connectors on the Raspberry Pi Zero. The Pi Zero doesn't come with headers pre-soldered; this surprised a lot of people, and led to a few problems [due to header soldering](https://github.com/google/aiyprojects-raspbian/issues/217#issuecomment-354906355).

While none of these problems are serious by themselves, all of them combined has led [Micro Center](http://www.microcenter.com/) to take the remaining stock of Vision Kits off the shelves today until Google updates the documentation and SD card image, making getting started with the kit easier.

Despite [rumors](https://twitter.com/radamar/status/948301042713636864), the kits have not been recalled, and you don't have to return your kit. But if you have your hands on with the Vision Kit right now and you're having problems getting things to work, there are a few practical steps you can take to diagnose what's going wrong.

You can see if you're running it on the right hardware by checking the revision number of your Raspberry Pi board.
    
    
    **$** cat /proc/cpuinfo | grep Revision  
    Revision	: 9000c1
    
    
    900092 -- Pi Zero without camera connector, no wireless  
    **900093** -- Pi Zero with camera connector, no wireless  
    **9000c1** -- Pi Zero W with camera connector + Wi-Fi/Bluetooth

The Vision Kit should work with both `900093` and `9000c1` revisions of the board, but not the original `900092` version without the camera connector.

If you're unsure whether you've soldered your 40-pin connector to your Raspberry Pi Zero correctly, then a good first test is to use the [Pin Test utility](http://wiringpi.com/the-gpio-utility/pin-test/) that ships with Gordon Henderson's [WiringPi](http://wiringpi.com/) library. You should download the [latest version of the library](http://wiringpi.com/download-and-install/) and make sure you **remove** the Vision Bonnet before running the pin test or it will return incorrect results.

If you're not sure whether the rest of your hardware is put together correctly, or if you're wondering whether the Raspberry Pi is talking to the Vision Bonnet at all, you can check your `dmesg` for errors, and compare it to output [from a 'good' boot](https://github.com/google/aiyprojects-raspbian/issues/217#issuecomment-354838431).
    
    
    **$ **dmesg  
    [    0.000000] Booting Linux on physical CPU 0x0  
    [    0.000000] Linux version 4.9.59+ (dc4@dc4-XPS13-9333) (gcc version 4.9.3 (crosstool-NG crosstool-ng-1.22.0-88-g8460611) ) #1047 Sun Oct 29 11:47:10 GMT 2017  
        .  
        .   
        .  
    [   92.772028] Unregistered device pwm22  
    **$**

Finally, make sure all your ribbon cables are connected the right way around, with the pins facing the PCBs when connecting them to the Raspberry Pi, Vision Bonnet, and the Camera.

The only real hardware problem with the kit is the faulty cable marking on the short ribbon cable joining the Raspberry Pi and the Vision Bonnet. Google is currently in the process of updating the documentation, but for now just ignore the label and plug it in the wrong way around.

However if you're still having problems getting things to work, look out for a new more friendly SD card image, and updates to the [assembly guide](https://aiyprojects.withgoogle.com/vision/#assembly-guide) to help, which should go live later today.

> "The AIY team is excited to see Vision Kit making it's way to the workbenches of creative makers and a few have already given useful feedback. From your suggestions, we've updated the [Vision Kit Assembly Guide](https://aiyprojects.withgoogle.com/vision/#assembly-guide) with a few points of clarification and [the SD card image](https://aiyprojects.withgoogle.com/vision/#assembly-guide-1-get-the-vision-kit-sd-image) to make it easier to get started. Be sure to reach out to us at [s](about:invalid#zSoyz)[upport-aiyprojects@google.com](mailto:support-aiyprojects@google.com) if you run into any issues and [join our mailing list for product notifications](https://services.google.com/fb/forms/aiycommunicationpreferences/) as Vision Kit comes to more retailers soon." -- Billy Rutledge, Director of AIY Projects at Google

While I've had pre-production hardware on my desk for a few weeks now, I'm expecting to get my hands a retail boxed version of the Vision Kit this week. I'll be sitting down and putting it together, and getting it working this weekend, so expect a step-by-step walkthrough when I do.

Despite teething troubles, I'm optimistic about the long-term influence of the Vision Kit, with its the ability to run trained networks "at the edge" nearer the raw data, reducing barriers to deploying machine learning applications out in the world.
