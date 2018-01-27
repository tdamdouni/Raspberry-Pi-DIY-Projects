# Adding Reboot and Shutdown Commands to the Raspberry Pi AIY Projects Google Assistant

_Captured: 2017-11-09 at 23:07 from [ktinkerer.co.uk](http://ktinkerer.co.uk/adding-reboot-shutdown-commands-raspberry-pi-aiy-projects-google-assistant/)_

**UPDATE! The Google AIY Project have now pulled my commands to do this into the official repository <https://github.com/google/aiyprojects-raspbian> so if you use the most up to date version from there it's no longer necessary to add this yourself. The box should now respond to "pi reboot" and "pi power off"**

The [MagPi magazine](https://www.raspberrypi.org/magpi/google-aiy-voice-magpi-57/) came with a fantastic kit to add create a voice interactive Google Assistant with a Raspberry Pi.

As with all headless pi projects shutting down or rebooting can be a pain, I usually end up using ssh, so my first simple project is to add shutdown and reboot as voice commands. It turned out to be pretty easy!

The file you need to edit is `~/voice-recognizer-raspi/src/action.py` find the section that looks like this:  
`# =========================================  
# Makers! Implement your own actions here.  
# =========================================`

`def make_actor(say):  
"""Create an actor to carry out the user's commands."""`

`

actor = actionbase.Actor()

actor.add_keyword(  
_('ip address'), SpeakShellCommandOutput(  
say, "ip -4 route get 1 | head -1 | cut -d' ' -f8",  
_('I do not have an ip address assigned to me.')))

actor.add_keyword(_('volume up'), VolumeControl(say, 10))  
actor.add_keyword(_('volume down'), VolumeControl(say, -10))  
actor.add_keyword(_('max volume'), VolumeControl(say, 100))

`

`actor.add_keyword(_('repeat after me'),  
RepeatAfterMe(say, _('repeat after me')))  
`  
add to the bottom of that section:

`actor.add_keyword(_('power off'), SpeakShellCommandOutput(say, "sudo shutdown now",_('failed to shutdown')))  
actor.add_keyword(_('reboot'), SpeakShellCommandOutput(say, "sudo shutdown -r now", _('failed to reboot')))`

I tried using the command "shutdown" at first but that seemed to be conflicting with a Chromecast command.

Save the file and restart the voice recognizer service `sudo systemctl restart voice-recognizer.service`

Now your pi will shutdown when you say "power off" and reboot when you say "reboot"!

UPDATE:  
I've made an updated version of this which responds to the command before it reboots / shuts down. I've put it on Github and you can find it here: <https://github.com/ktinkerer/aiyprojects-raspbian/blob/master/src/action.py>
