# Mote Sticks and Google AIY (Voice control of lights)

_Captured: 2017-09-02 at 15:27 from [forums.pimoroni.com](http://forums.pimoroni.com/t/mote-sticks-and-google-aiy-voice-control-of-lights/4790)_

For those who have not yet bought an Amazon Echo, Google Home .... there is the Google Voice Kit and if you were lucky enough to get the hardware package that was attached to the current issue of The MagPi magazine then you have the basis for a way to do basic voice control.  
Pimoroni have also shown that even without the Google hardware you can make your own equivalent using off-the-shelf components.

I did get the Google kit that came with the magazine so I thought as a first project I would make it control the Pimoroni Mote Sticks (lights).

In essence it is simple voice-to-text.  
In my case the commands are:  
Kitchen Light   
where is one of "on", "off", (name of colour).

to get it to work you need to edit   
~/voice-recognizer-raspi/src/action.py

Near the top include:
    
    
    #imports for the "lights" command
    import webcolors
    import re
    import requests

Then after
    
    
    # =========================================
    # Makers! Implement your own actions here.
    # =========================================

include
    
    
    setlightapiprefix = "http://localhost:5000/mote/api/v1.0/"
    class setlight(object):
        def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword
    
    def run(self, voice_command):
    
        # Strip command name from front
        thiscolorname = voice_command.replace(self.keyword, '', 1)
        # Remove any leading/trailing whitespace - will be a space at the front
        thiscolorname = thiscolorname.strip()
    
        apisuffix = ''
        if thiscolorname.lower() ==  'on':
            apisuffix = 'on'
        elif thiscolorname.lower() == 'off':
            apisuffix = 'off'
        else:
            # Color names must not have spaces - e.g. "light blue" must be "lightblue"
            thiscolorname = re.sub(r"\s+", "", thiscolorname, flags=re.UNICODE)
            try:
                # webcolors defaults to getting color names (keywords) from CSS3 (at least at the time of writing this)
                # These are in English only - see https://www.w3.org/TR/css3-color/
                thiscolorhex = webcolors.name_to_hex(thiscolorname)
               # Strip the hash off the front
                thiscolorhex = thiscolorhex[1:]
                apisuffix = 'set/' + thiscolorhex
    
            except ValueError as e:
                logging.info("Color name not recognized:"+thiscolorname)
                self.say("Error  Color "+thiscolorname+" not recognized. Try a color from the rainbow in English")
                return
    
    
        r = requests.get(setlightapiprefix + apisuffix)
        # print(setlightapiprefix + apisuffix + " response code:" + str(r.status_code))
        return ""

Change the line with  
<http://localhost:5000/mote/api/v1.0/>  
to point to the IP address of your Mote Stick controller if it is not on the same machine as your voice kit.  
If you have more Motes dotted around on different RPi systems then the script would need changing a bit to pass in the host address that is appropriate for each set of Motes - e.g.  
Lounge -> 192.168.0.10  
Kitchen -> 192.168.0.20

Also this is using the v1.0 version of the Mote API that was documented by Pimoroni for connecting up the Homebridge system. However, they have another v1.0 API with a different syntax (so much for API versioning) and if you have that one then you would have to make some easy enough changes in the code where the on/off/color calls are made.

Then - after
    
    
        # =========================================
        # Makers! Add your own voice commands here.
        # =========================================

add
    
    
        actor.add_keyword(_('kitchen light'),setlight(say,_('kitchen light')))

Remember that Python is very particular about leading spaces on lines - so make sure that everything lines up correctly.

I used "kitchen light" as the speech prefix because  
* it sounded a bit more natural to say "kitchen light blue" than "light kitchen blue"  
* Having "light" as a prefix might confuse later inclusion of real Google Home commands  
* Having "kitchen" at the front provides the basis for future addition of more Motes (e.g. Lounge Light On)
    
    
    sudo pip install webcolors re requests
