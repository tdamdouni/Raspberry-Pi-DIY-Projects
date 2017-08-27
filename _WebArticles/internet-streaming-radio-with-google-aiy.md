# Internet Streaming Radio with Google AIY

_Captured: 2017-08-25 at 11:27 from [www.hackster.io](https://www.hackster.io/vvanhee/internet-streaming-radio-with-google-aiy-1edff3)_

![Internet Streaming Radio with Google AIY](https://hackster.imgix.net/uploads/attachments/303732/thumb-aiy-ip_VBnqVbLVWr.png?auto=compress%2Cformat&w=900&h=675&fit=min)

The [Google AIY Voice Kit](https://aiyprojects.withgoogle.com/voice/) is a great way to get started with using voice commands to control a Raspberry Pi. As of 5/13/2017, the Google Assistant in this project does not play music like Google Home does. So I wanted to add the ability to play streaming radio or MP3s using voice activation. Using this method, you can get your Google AIY Voice project to play your favorite streaming radio on your voice command.

First, install mpd (music player daemon) and mpc (the controller for mpd).
    
    
    sudo apt-get install mpd mpc
    

Next, edit the configuration file as follows:
    
    
    sudo nano /etc/mpd.conf
    

You'll see some lines that look like the following:
    
    
    audio_output {
    type "alsa"
    name "My ALSA Device"
    #  device "hw:0,0" # optional
    #  mixer_type "hardware" # optional
    #  mixer_device "default"  # optional
    #  mixer_control  "PCM"  # optional
    #  mixer_index  "0"  # optional
    }
    

Change these lines to the following (uncomment device and mixer_type, and replace hardware with software):
    
    
    audio_output {type "alsa"
    name "My ALSA Device"
    device "hw:0,0" # optional
    mixer_type "software" # optional
    #  mixer_device "default"  # optional
    #  mixer_control  "PCM"  # optional
    #  mixer_index  "0"  # optional
    }
    

Next, look for the word "group" in mpd.conf and change it to "audio."
    
    
    group           "audio"
    

Now save the mpd.conf file and get back into terminal. Start and enable the mpd daemon so it will start on reboot.
    
    
    sudo systemctl start mpd
    sudo systemctl enable mpd
    

Now it's time to test your internet radio. Find a link to a streaming radio online. I found a .pls file for KEXP 90.1 Seattle, looked at it in a text editor, and found that the [KEXP stream can be accessed directly at http://50.31.180.202:80](http://50.31.180.202/). So to test out your player, type:
    
    
    mpc add http://50.31.180.202:80/ 
    mpc play
    

You should hear the audio stream now. To stop it, type:
    
    
    mpc stop
    

Now it's time to modify the `voice-recognizer-raspi` code so that it recognizes your command. Edit the python file using nano:
    
    
    nano /home/pi/voice-recognizer-raspi/src/action.py
    

First, add `import subprocess` in action.py after the other imports.

Next, after the "Implement your own actions here," put the following class. Make sure to change http://50.31.180.202:80/ to your radio station:
    
    
    # Play Radio of your choice (change http://50.31.180.202:80/ to your choice)
    class playRadio(object):
        def __init__(self, say):
            self.say = say
        def run(self, voice_command):
            self.say('Playing Radio')
            subprocess.call("mpc clear;mpc add http://50.31.180.202:80/;mpc play",shell=True)
    

Then after "add your own voice commands here" add:
    
    
    actor.add_keyword(_('my radio station'), playRadio(say))
    

Now (after you reload voice-recognizer), when you trigger the box and say "My radio station," your radio station will play.

The only problem now is that the radio station won't pause when you try to do another voice command. To make the box pause when you trigger voice recognition, you'll have to edit the main.py file to stop mpd when the trigger is activated.
    
    
    nano /home/pi/voice-recognizer-raspi/src/main.py
    

First, add `import subprocess` in main.py after the other imports. Then add the subprocess.call in the exact place shown below. This will first stop mpd and then start the Google Assistant listening again, as usual.
    
    
       def recognize(self): 
           if self.recognizer_event.is_set(): 
               # Duplicate trigger (eg multiple button presses) 
               return 
           #############stop mpc################ 
           subprocess.call("mpc stop", shell=True) 
           #####################################
           self.recognizer.reset() 
           self.recorder.add_processor(self.recognizer) 
           self._status('listening')  
    

Now `sudo systemctl restart voice-recognizer` to use the changes.

Now trigger the box, and say "My radio station." To stop it, trigger the box and ask another question or just say "thanks."

Enjoy your live streaming radio!

![Sensors oivvw6stxy](https://halckemy.s3.amazonaws.com/uploads/attachments/303735/sensors_OIvVW6StXY.png)
