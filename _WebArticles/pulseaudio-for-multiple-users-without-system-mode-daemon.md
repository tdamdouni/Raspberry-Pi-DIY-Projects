# Pulseaudio for multiple users, without system-mode daemon

_Captured: 2017-09-04 at 10:43 from [billauer.co.il](http://billauer.co.il/blog/2014/01/pa-multiple-users/)_

This is a simple and quick solution for those of us who want to run certain programs as a different user on the same desktop, for example running several user profiles of a browser at the same time. The main problem is usually that Pulseaudio doesn't accept connections from a user other than the one logged in on the desktop.

It's often suggested to go for a [system mode](http://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SystemWide/) Pulseaudio daemon, but judging from the developer's [own comments](http://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/WhatIsWrongWithSystemWide/) on this, and the friendly messages left in the system's log when doing this, like
    
    
    Jan 18 16:35:33 ocho pulseaudio[11158]: main.c: OK, so you are running PA in system mode. Please note that you most likely shouldn't be doing that.
    Jan 18 16:35:33 ocho pulseaudio[11158]: main.c: If you do it nonetheless then it's your own fault if things don't work as expected.
    Jan 18 16:35:33 ocho pulseaudio[11158]: main.c: Please read http://pulseaudio.org/wiki/WhatIsWrongWithSystemMode for an explanation why system mode is usually a bad idea.
    Jan 18 16:35:33 ocho pulseaudio[11158]: module.c: module-hal-detect is deprecated: Please use module-udev-detect instead of module-hal-detect!
    Jan 18 16:35:33 ocho pulseaudio[11158]: module-hal-detect-compat.c: We will now load module-udev-detect. Please make sure to remove module-hal-detect from your configuration

it's probably not such a good idea. Plus that in my case, the sound card wasn't detected in system wide mode, probably because some configuration issue, which I didn't care much about working on. The bottom line is that the software's authors don't really want this to work.

### Opening a TCP socket instead

The simple solution is given on [this forum thread](http://forums.fedoraforum.org/showthread.php?t=190954). This works well when there's a specific user always logged on, and programs belonging to other dummy users are always run for specific purposes.

The idea behind this trick is to open a TCP port for native Pulseaudio communication, only it doesn't require authentication, as long as the connection comes from 127.0.0.1, i.e. from the host itself. This opens the audio interface to any program running on the computer, including recording from the microphone. This makes no significant difference security-wise if the computer is accessed by a single user anyhow (possible spyware is likely to run with the logged in user ID anyhow, which has full access to audio either way).

This solution works on Fedora Core 12, but it's probably the way to do it on any distribution released since 2009 or so.

_Edit: It has been suggested in the comments below to use a UNIX socket instead of TCP. Haven't tried it, but it seems like a better solution._

### To do as the desktop's user

So let's get to the hands-on: First, copy /etc/pulse/default.pa into a file with the same name in the .pulse directory, that is
    
    
    cp /etc/pulse/default.pa ~/.pulse/

And then edit the file, adding the following line at the end:
    
    
    load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1

At this point, restart the pulseaudio deamon,
    
    
    $ pulseaudio -k
    $ pulseaudio -D

### To do as the "fake" user

Now **switch to the second user**, and create a file named client.conf under that user's .pulse subdirectory
    
    
    $ echo "default-server = 127.0.0.1" > ~/.pulse/client.conf

Note that default.pa and client.conf are in completely different directories, each belonging to a different user!

Surprisingly enough, that's it. Any program running as the second user now has sound access.
