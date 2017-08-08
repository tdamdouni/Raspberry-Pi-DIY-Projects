# Raspberry Pi Carputer 2 – XBMC Skin & Scripts 

_Captured: 2016-01-11 at 11:34 from [nikrooz.co.uk](http://nikrooz.co.uk/raspberry-pi-carputer-2/)_

This post has been a _long_ time coming. In fact, so long that I no longer have the Zafira that I installed the carputer in. But I still have all the code and workings out burning a hole in my hard drive, and questions keep coming in asking how it was all done. So I'll try to explain a little more and put some code up.

If you want to skip my explanations and go straight to the code, I've put various bits on Github:

  * All-important OBD script, with parsers for GM's data strings: [XBMC-rpi-service.script.OBD](https://github.com/anikrooz/XBMC-rpi-service.script.OBD)
  * GPIO backend script, for two-way GPIO to.from your skin: [XBMC-rpi-service.script.gpio](https://github.com/anikrooz/XBMC-rpi-service.script.gpio)
  * And the modified 7tft skin. Please read below for provisos. [XBMC-Skin.seventft](https://github.com/anikrooz/XBMC-Skin.seventft)

## Getting data into XBMC

One of the biggest challenges with using XBMC as a display is getting the data from GPIO and from your OBD bluetooth chip onto XBMC's display. For this I wrote a couple of services, based on an album info-finding script, to set and get properties on a particular window of the skin. In my application, the service starts on load of the 'Home' window. This is the window that I adapted to show various data. I kept the music and volume data so that this Home window is what you'll nearly always be looking at.

Running the script is as simple as:

1
`<onload>Runscript(script.OBD, backend=true))</onload>`

for the OBD script.  
Or

1
`<onload>Runscript(script.GPIO, backend=true, ins=0, ins=1)</onload>`

for the GPIO script - notice the 'ins' passed to it; this tells the script to set these particular GPIO pins to IN and keep the skin property up-to-date.

I chose to use the 'gpio' command and run it with os.system call from python for compatibility - this command can be run as a normal user once it's set up, if I remember correctly. And while it doesn't monitor the IN pins as an interrupt, the service checks every 1/2 a second so for the purpose of illuminating lights on the screen (making bits visible) it's fine.

## Toggling GPIO

12
`<code><onfocus>SetProperty(GPIOon, 17)</onfocus>``<onunfocus>SetProperty(GPIOoff, 17)</onunfocus>`

should do it. Notice this sets a property on the skin. The GPIO script has this little bit of code in its loop that checks those properties:

1234
`if` `xbmc.getCondVisibility(``"!IsEmpty(Window(home).Property(GPIOon))"``):``self``.ons.append(``self``.window.getProperty(``'GPIOon'``))``self``._StartOnActions()``self``.window.clearProperty(``'GPIOon'``)`

## Displaying data

For simple on/off values, as you'll get from the GPIO script, you'll probably want to make an image or a control group visible or not:

1234567891011
`<``control``>``<``description``>Test</``description``>``<``type``>image</``type``>``<``id``>0</``id``>``<``width``>63</``width``>``<``height``>60</``height``>``<``posx``>100</``posx``>``<``posy``>128</``posy``>``<``texture``>handbrake.png</``texture``>``<``visible``>SubString(Window(home).Property(GPIO0), "0")</``visible``>``</``control``>`

For other values, here's an example of what I used for the OBD info:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091
`<!-- OBD Stuff -->``<``control` `type``=``"group"` `id``=``"77"``>``<``visible``>SubString(Window(home).Property(OBD-Conn), "OK")</``visible``>``<``control``>``<``description``>BattImg</``description``>``<``type``>image</``type``>``<``id``>0</``id``>``<``width``>40</``width``>``<``height``>40</``height``>``<``posx``>490</``posx``>``<``posy``>60</``posy``>``<``texture``>battery.png</``texture``>``</``control``>``<``control``>``<``description``>Vbatt</``description``>``<``type``>label</``type``>``<``id``>555</``id``>``<``posx``>530</``posx``>``<``posy``>78</``posy``>``<``info``>Window(home).Property(OBD-Voltage),,v</``info``>``<``font``>alwin24bold</``font``>``<``align``>left</``align``>``<``textcolor``>ffff6103</``textcolor``>``<!--<visible>!Control.HasFocus(5)</visible>\-->``</``control``>``<``control``>``<``description``>BR-Throttle</``description``>``<``type``>label</``type``>``<``id``>93</``id``>``<``posx``>635</``posx``>``<``posy``>537</``posy``>``<``font``>alwin24bold</``font``>``<``textcolor``>ffff6103</``textcolor``>``<``label``>ACC ped</``label``>``<``alignx``>center</``alignx``>``<``info``>Window(home).Property(OBD-Throttle),,%</``info``>``</``control``>``<``control``>``<``description``>TR-MPG</``description``>``<``type``>label</``type``>``<``id``>93</``id``>``<``posx``>625</``posx``>``<``posy``>9</``posy``>``<``font``>alwin24bold</``font``>``<``textcolor``>ffff6103</``textcolor``>``<``alignx``>center</``alignx``>``<``info``>Window(home).Property(OBD-MPG)</``info``>``</``control``>``<``control` `type``=``"fadelabel"` `id``=``"95"``>``<``description``>TL-AvMPG</``description``>``<``posx``>6</``posx``>``<``posy``>9</``posy``>``<``width``>200</``width``>``<``visible``>true</``visible``>``<``scroll``>false</``scroll``>``<``scrollout``>false</``scrollout``>``<``pauseatend``>5000</``pauseatend``>``<``label``>Trip: 0 mi</``label``>``<``info``>Window(home).Property(OBD-AvMPG),Av:, mpg</``info``>``<``info``>Window(home).Property(OBD-TripL),T: , L</``info``>``<``info``>Window(home).Property(OBD-TripP),T: ,p</``info``>``<``info``>Window(home).Property(OBD-TripMi),T: , Mi</``info``>``<``font``>alwin24bold</``font``>``<``resetonlabelchange``>false</``resetonlabelchange``>``<!--<textcolor>FFB2D4F5</textcolor>\-->``<``textcolor``>ffff6103</``textcolor``>``</``control``>``<``control` `id``=``"671"``>``<``description``>ThrottleProgressbar</``description``>``<``type``>progress</``type``>``<``posx``>577</``posx``>``<``posy``>53</``posy``>``<``width``>101</``width``>``<``height``>461</``height``>``<``reveal``>true</``reveal``>``<!--<info>Window(home).Property(OBD-BoostPercent)</info>\-->``<``texturebg``>progress_mid-homeR.png</``texturebg``>\-->``<``lefttexture``>-</``lefttexture``>``<``midtexture``>progress_back-homeR.png</``midtexture``>``<``righttexture``>-</``righttexture``>``<!--<overlaytexture>progress_over_vertL.png</overlaytexture>\-->``</``control``>``...`

There are a few good examples there.

  * Firstly, the whole group doesn't function if OBD is not connected.
  * Second, notice the formatting on the <info> tags - <info>[value],PREFIX,SUFFIX</info>
  * And notice the TL-AvMPG section: It cycles through a few properties, changing every 5s.
  * Then the ThrottleProgressbar is a progress bar with distinct texture .png images. I just used the 'mid' texture and the reveal tag, to make it more natural.

I regret not having taken more videos of this but [this video](https://www.youtube.com/watch?v=MPohQJgiQ0s) shows how the progress bars work.

## The skin

The [XBMC-Skin.seventf](https://github.com/anikrooz/XBMC-Skin.seventft)t skin was originally made by a German guy named djtoll. It's an awesome skin and some serious work has gone into it. When I found it, it wasn't compatible with XBMC / Kodi version 12 and up, since they changed the way things work. My github version is one that I've made work with XBMC 12+, but only for my particular needs. It will only work at PAL16x9 resolution, because that's what I used. And the progress bar images, etc. that I added are only in that resolution.

**Pull requests welcome!**

I've seen this said many times about open source projects, and I'm trying to learn what it means. Yes, I'm new to github and all that but it would be great if this project got better and compatible with more cars now the source it out there.

If you use the seventft skin in another resolution, and add compatibility, please try to merge your changes in. It would be great to see my work our work benefit other people.
