# Siri: Open my garage door..

_Captured: 2015-10-31 at 13:31 from [www.raspberrypi.org](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=25118&p=231345)_

Hi, this is my first real Raspberry Pi project - SiriProxy running on the Raspberry Pi, along with wiringPi to access the Pi's GPIO pins and turn a relay on/off. The relay is then hooked up to my automatic garage door system. So, I have control of the door with Siri on my iPhone.

There are probably other ways to do the same thing, such as running a web server on the Pi and have that access the GPIO's etc but I basically cobbled this together for my own needs - and it works fine.

I am running the Pi as "root" for this whole setup as it just makes things easier for me and I'm using the "wheezy" distro.  
Follwing the instructions here: <http://www.idownloadblog.com/2011/12/09/how-to-install-siri-proxy-tutorial-video/> should get SiriProxy up and running, if you do follow these instructions then swap commands 11, 12 and 13 to 12, 13, 11. Command 7 by the way will take about 90 minutes to compile on the pi!

Then install wiringPi from [https://projects.drogon.net/raspberry-p ... d-install/](https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/)

Once these are installed its just a case of modifying the example ruby script included with siriproxy.  
Edit this file: /root/SiriProxy/plugins/siriproxy-example/lib/siriproxy-example.rb

Look for the lines:

    `  listen_for /test siri proxy/i do  
    say "Siriproxy is up and running!" #say something to the user!  
  
    request_completed #always complete your request! Otherwise the phone will "spin" at the user!  
  end`

And add this directly under them:

    `  listen_for /open the garage door/i do  
    say "Opening the garage door.."  
    request_completed  
    system("gpio mode 1 out")  
    system("gpio write 1 1")  
    system("sleep 0.5")  
    system("gpio write 1 0")  
  end  
  
  listen_for /close the garage door/i do  
    say "Closing the garage door.."  
    request_completed  
    system("gpio mode 1 out")  
    system("gpio write 1 1")  
    system("sleep 0.5")  
    system("gpio write 1 0")  
  end`

As you can see, the ruby script is basically calling "system" commands to access wiringPi. Setting a GPIO pin as an output then setting it high for half a second then low again.

You can have siri to call any command you can type in a terminal window, such as a passwordless SSH login to a remote pc to have it shut down or rebooted.

    `  listen_for /turn off my laptop/i do  
    response = ask "Are you sure you want me to shut down your laptop?"  
  
    if(response =~ /yes/i)  
      say "OK, I'll shut it down now.."  
      system("ssh root@192.168.1.74 shutdown -h now")  
    else  
      say "OK, I wont!"  
    end  
  
    request_completed  
  end`

You could have RasPI's in different rooms with different commands to follow, all from one siriproxy server. Note: each time you modify the example plugin you must run the "siriproxy bundle" command before restarting the server.

Anyway, here is a video of my setup.

<http://youtu.be/NUJ5z76Xv5o>

  


I did think if an even cheaper method to activate a relay remotely (I've done this to turn on a remote pc as an FTP server in the past)

Get an old Nokia 3210 - or any other old Nokia that let's you make custom ringtones along with its own pay as you go sim (free). Create a ringtone that consists of a single note for 1 second then silent for 30 seconds. Assign that tone to a contact number - your other phone. Set the phone to silent and only play that tone when you call the Nokia from your other phone.

Hook up 5v from the charger to a resistor and npn transistor, then hook up a wire from the phone speaker to a capacitor and the base of the transistor. Now attach a 5v relay to the transistor.

Now dial the Nokia's number from the other phone, the Nokia will play its 1 second tone that will be turned into a small DC current through the cap and into the transistor, which will turn the relay on for 1 second then off again.

As the Nokia never "picks up" the calls it will never cost anything to activate the relay over cellular. Just call it, then put the phone down after a couple of seconds.

> DarkTherapy wrote:I did think if an even cheaper method to activate a relay remotely (I've done this to turn on a remote pc as an FTP server in the past)  
  
Get an old Nokia 3210 - or any other old Nokia that let's you make custom ringtones along with its own pay as you go sim (free). Create a ringtone that consists of a single note for 1 second then silent for 30 seconds. Assign that tone to a contact number - your other phone. Set the phone to silent and only play that tone when you call the Nokia from your other phone.   
  
Hook up 5v from the charger to a resistor and npn transistor, then hook up a wire from the phone speaker to a capacitor and the base of the transistor. Now attach a 5v relay to the transistor.   
  
Now dial the Nokia's number from the other phone, the Nokia will play its 1 second tone that will be turned into a small DC current through the cap and into the transistor, which will turn the relay on for 1 second then off again.  
  
As the Nokia never "picks up" the calls it will never cost anything to activate the relay over cellular. Just call it, then put the phone down after a couple of seconds.

I hear Hamas has a few job openings that you may be qualified for...

But in all seriousness, this is pretty cool, and has got me thinking if there's any way to integrate this with my Insteon HA system. Since the controller is networked, a Pi might not even ben eded. Hmm.

Hi,

I've got the siriproxy up and running but changes I make to the siriproxy-example.rb do nothing! I've modified the line under 'listen_for /test siri proxy/i do'

from  
say "Siriproxy is up and running!" #say something to the user!

to  
say "Something different!" #say something to the user!

then run:  
siriproxy bundle

and restarted the server with:  
rvmsudo siriproxy server

but the command "Test Siri Proxy" still replies with "Siriproxy is up and running!"

What am I missing?

Thanks in advance

> Joey wrote:Hi,  
  
I've got the siriproxy up and running but changes I make to the siriproxy-example.rb do nothing! I've modified the line under 'listen_for /test siri proxy/i do'  
  
from  
say "Siriproxy is up and running!" #say something to the user!  
  
to  
say "Something different!" #say something to the user!  
  
then run:  
siriproxy bundle  
  
and restarted the server with:  
rvmsudo siriproxy server  
  
but the command "Test Siri Proxy" still replies with "Siriproxy is up and running!"  
  
What am I missing?  
  
Thanks in advance

For me I have to call "rake install" and I think that's the piece where it repackages that information up. Then from there you can skip straight to "rvmsudo siriproxy server".

It all works fines for me as per DT's instructions. Yes, I did need to 'siriproxy bundle', before restarting the server, but one thing I found was that I had to be in the SiriProxy directory in order for the server to restart, otherwise it threw up errors. This is slightly painful because you need to edit the .rb file and navigate to that beforehand. Well obviously I couldv'e used cd /blah/blah/blah/blah/blah/ to get there quicker.........

Texy

OK guys, I have been on this for the last two days and running out of ideas!!

It all seems to go fine until the last step of "rvmsudo siriproxy server" which has an error that gives me "no such file or directory - /root/.siriproxy/config.yml"

it seems the problems relates to root or pi user and where the installation, files and permissions are getting mixed up. The author of this post said that he did the installation under root user. Does this mean follow the whole instruction with login root using "su" or do I add a sudo to the commands and which ones need/should have sudo?

Or am is the problems something else? I am totally out of ideas. Help from the people that have got it working..

Thanks in advance for saving me pulling out more hairs

Dark Therapy

I just did a fresh install of wheezy and updated. THen I got to RVM install 1.9.3

1) It did not recognize RVM until I did "source /etc/profile.d/rvm.sh"  
Then after ahout 1 hour of waiting, It stopped due to error message  
"error running 'make', please read /usr/local/rvm/log/ruby-1.9.3-p327/male log There has been an error while running make. Halting installation  
chmod: cannot access "/usr/local/rvm/rubies/ruby-1.9.3-p327' No such file or directory..

I got the same error prior to doing a fresh install..

PS:   
While installing RVM, I noticed a warning, but it completed its install. The message was

" Installing to RVM to /usr/local/rvm  
/usr/local/rvm/src/rvm/scripts/functions/installer: line 147: __rvm_CD: command not found

Could it be due to that I am on Rev A of RPI and not the newer model??

I just noticed that the RVM installer said to signout before initiating RVM, so I am doing a second run of "rvm install 1.9.3"

Any ideas.

sorry as this is getting lengthy....like the 5th clean install try..yet I did the update and upgrade commands...

in the step:  
bash < <(curl -s [https://raw.github.com/wayneeseguin/rvm ... -installer](https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer)) process,  
there are notes to add user and running source /etc/profile.d/rvm.sh

and in the rvm install 1.9.3 there are notes to add things like git, curl, jruby...etc. all I did was hit q to continue.

Can someone clarify if I should have followed some of those instructions in the notes or just continue on?

Noob speaking but this is really interesting. I've been through all the posts here and not heard mention of Debian Wheezy, can I assume the same commands shown in the install video for Ubuntu will work with Debian?  
And is there C/C++ or Python source available for handling it?

Any help etc.

Cheers.  
Dave.

(great work btw)

> davef21370 wrote:Noob speaking but this is really interesting. I've been through all the posts here and not heard mention of Debian Wheezy, can I assume the same commands shown in the install video for Ubuntu will work with Debian?  
And is there C/C++ or Python source available for handling it?  
  
Any help etc.  
  
Cheers.  
Dave.  
  
(great work btw)

If you go back to the very first post, you'll notice the word "Wheezy". That is the distro it uses.

  


Hi DarkTherapy, Appreciate your patience.

I got it finally, for me on reboot, I could not get siriproxy without $source /etc/profile.d/rvm.sh is there are reason for this?

Also, I know you are running this on iPhone4S, I assumed that it works also for iPad3. Is this a correct assumption? Does it need to jailbroken? I am ios6.0 on the iPad3.

the reason I ask is that ask soon as I hit siri on my ipad3, it crashes my siri server.and in the error message it references "iphone" so wondering if this is only valid on iphone 4S, does it work on iphone5?

Also, since this is the second full attempt, I had a ca.pem from the 1st attempt installed on my ipad3, so there is now 2 ca.pem installed. Does it cause problems and how do I remove them if does cause problems.

Sorry for all this challenges to the group.

OH, I think the problem with other installs is because I was on BerryBoot install of wheezy which may have caused some of the problems.

I did a little research and it does not require jailbreak. And should work on Iphone 5. I just tried it on my friends iphone 5 and still the same crash upon opening up siri on iphone. here is the error

> root@raspberrypi:/home/pi/SiriProxy# siriproxy server  
Starting SiriProxy on port 443..  
SiriProxy up and running.  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1e67710 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1e67638>, @zip_stream=#<Zlib::Deflate:0x1e67620>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x16dd1f8 @manager=#<SiriProxy::PluginManager:0x1e671b8 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
/usr/local/rvm/gems/ruby-1.9.3-p327@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `encode': "\x8B" on UTF-8 (Encoding::InvalidByteSequenceError)  
from /usr/local/rvm/gems/ruby-1.9.3-p327@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `charset_convert'  
from /usr/local/rvm/gems/ruby-1.9.3-p327@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:442:in `string_to_binary'  
from /usr/local/rvm/gems/ruby-1.9.3-p327@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:48:in `to_binary'  
from /usr/local/rvm/gems/ruby-1.9.3-p327@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
from /usr/local/rvm/gems/ruby-1.9.3-p327@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
from /usr/local/rvm/gems/ruby-1.9.3-p327@SiriProxy/gems/CFPropertyList-2

hi, found potentially my issue on github

[https://github.com/jimmykane/The-Three- ... issues/389](https://github.com/jimmykane/The-Three-Little-Pigs-Siri-Proxy/issues/389)

> For now, this should be in siriproxy.gemspec:  
  
s.add_runtime_dependency('CFPropertyList', '2.1.2')  
  
I cannot submit code so cannot change it.

but when I go and edit siriproxy.gemspec to the above and I rerun server, I notice in the error, the reference to CFPropertyList-2.2.0 no matter what the edit. So it leads me to think that the siriproxy.gemspec edit is not getting to the server. Does the siriproxy.gemspec need to be compiled?? I tried siriproxy bundle after editing gemspec and prior to running server, but CFPropertylist -2.2.0

how do i make sure the revised gemspec is incorporated?

OK Guys, Got it!!

The issue was that maybe I am running the latest siriproxy which has an error as stated in my previous post. I was able to edit the file and correct the error, and afterwards I was able to do "rake install" to get the changes incorporated.!! but I repeated steps 12, 13 before rake install and 14 and on after step 11.

Well, thanks guys, hope this run around will help others in avoiding it. Thanks again to Dark Therapy for your patience and responses.

Goodnight. Earned after a rough weekend with this. Need it to tackle using it to use it to control my home automation!! Thanks guys

Basically

Nano into siriproxy.gemspec edit the line with CFPaneList to

s.add_runtime_dependency('CFPropertyList', '2.1.2')

Save and exit.

Now I repeated all the commands in the instruction starting with first removing the ~/.siriproxy with $ rm -rf /.siriproxy

Then steps 12,13,11 ..etc

Hope this helps

Hi All,

I've had some difficulty setting this up from a fresh Wheezy build despite following the steps exactly (it couldn't find config.yml when installing and running the siriproxy server as user Pi), so thought I'd summarise the extra steps taken that are a combination of Joefly and DarkTherapy's posts in an easy to follow process so that others don't have the same problems.

\- I created a fresh image from the latest 2012-12-16-wheezy-raspbian  
\- To enable root I typed "sudo passwd root", entered a new pass, and tested by typing su -  
\- I logged out and connected back in to ssh as root  
\- I followed these steps as shown in the link [http://www.idownloadblog.com/2011/12/09 ... ial-video/](http://www.idownloadblog.com/2011/12/09/how-to-install-siri-proxy-tutorial-video/)  
1, 2, 3, 4  
\- The output of step 4 asks you to add a user to rvm in groups and run a command, so I did the following  
\- edited /etc/group  
\- Added root to the end of the rvm line as follows  
rvm:x:1001:root  
\- Ran the command "source /etc/profile.d/rvm.sh"  
\- I didn't bother with steps 5 and 6 because /root (which is $HOME) had no .rvm folder.  
\- I then followed these steps  
7, 8, 9, 10, 12, 13  
\- I edited "/root/SiriProxy/siriproxy.gemspec" and changed the line with CFPaneList to (as per Joefly's post - running siriproxy update didn't work for me)  
s.add_runtime_dependency('CFPropertyList', '2.1.2')   
\- Followed steps  
11, 14, 15  
\- For step 16 I just ran "siriproxy server" and all now worked.

Hope this helps others!

...but doesn't Sky broadcast the control signals over the satellite 'airwaves' to control recordings, etc? My sky+ box isn't connected to any network yet, I am able to set recordings.  
Texy

> texy wrote:  
  
  
...but doesn't Sky broadcast the control signals over the satellite 'airwaves' to control recordings, etc? My sky+ box isn't connected to any network yet, I am able to set recordings.  
Texy

My sky box is connected to my router and I can use the sky+ app on my iPhone to change channels or fast forward/rewind, access my planner etc these are protocols over my network surely. I may fire up wireshark later and see if I can work it out.

I installed SiriProxy right after pptpd (on a clean install of Wheezy). I got the VPN working (traceroute confirms this). However when I try rvmsudo siriproxy server I get this error. I try running it as root, and it says that rvmsudo is not found. I'm not familiar with Ruby at all, so I apologize if this is a simple fix.

    `pi@raspberrypi ~/SiriProxy $ rvmsudo siriproxy server  
Warning: can not check `/etc/sudoers` for `secure_path`, falling back to call vi  
a `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_p  
ath=1 to avoid the warning./usr/bin/env: siriproxy: No such file or directory`

Thanks for your help.

>   
  
This is basically all the circuit is, replace the word arduino with raspberry pi lol

It appears that this link no longer works, do you have another link?

Thanks,

> wranglerdriver wrote:
>
>>   
  
This is basically all the circuit is, replace the word arduino with raspberry pi lol
> 
>   
  
It appears that this link no longer works, do you have another link?  
  
Thanks,

<http://i.stack.imgur.com/Oarz3.gif>

  


> peadard wrote:Hi Guys.  
Firstly thank you Darktheraphy for posting this.  
I have successfully managed to get Siriproxy running on my pi after a couple of issues.  
One that i have seen mentionned a couple of times was the "No such file or directory" when trying to run SiriProxy server. I found that this line helped "Note: on some machines, rvmsudo changes "`~`" to "`/root/`". This means that you may need to symlink your "`.siriproxy`" directory to "`/root/`" in order to get the application to work:   
  
sudo ln -s ~/.siriproxy /root/.siriproxy  
"  
This is found in the README.md in the SiriProxy folder so hopefully it helps some people.   
  
After I got Siriproxy up and running I started thinking about its applications. I have a Elk M1 gold in my house doubling as a home automation and security system. I was going to wire the Pi up to this but then I thought of using code to do it. With the help of the info and files from here (Thank you very much James Russo) <http://sourceforge.net/projects/elkm1control/> I now use Siri to activate almost anything I want to on my M1.  
So again a big thank you to DarkTheraphy for getting me on the right path.

That's great :0)

DarkTherapy*

Hi,

Thanks for posting this great project. I have now a running pi with siriproxy and a tellstick (<http://www.telldus.se/products/tellstick>). Can't even imagine all the possibilities with this combination!

I'm able to turn on and off my Christmas three lights now using Siri. Very useful 

Just ordered a "USB Infrared Toy v2", so soon maybe I can use Siri to control my TV as well!

Jørgen

> DarkTherapy wrote:
>
>> texy wrote:
>>
>>> Does anyone know what protocols the "Sky+" app uses to talk to a Sky+ HD box connected to my router? It would be awesome to have Siri control my Sky+   
  
My sky box is connected to my router and I can use the sky+ app on my iPhone to change channels or fast forward/rewind, access my planner etc these are protocols over my network surely. I may fire up wireshark later and see if I can work it out.

Do u mean like this ?  
<http://www.youtube.com/watch?v=oOOZ82N99d4>

I'm not home till Xmas eve but I achieved it by creating seperate applications (on mac),one for each command,sent via telnet.  
I gave up working out out how to send the commands directly via ruby,mainly due to my limited knowledge of ruby.

HI Dark therapy,

I got everything up and running and now just fine tuning. For ip, I have one for wired, and another for wifi.  
I also got raspberrypi.local using

> raspberrypi.local  
If you have trouble remembering the IP address of your Raspberry Pi when you want to access it over the network, install avahi with the command "sudo apt-get install avahi-daemon" and you'll be able to use raspberrypi.local instead of the IP address. If you're accessing the Raspberry Pi from a Windows machine, you may need to install Bonjour Services on it for this to work

when I change my ip address in dnsmasq.conf to that of "raspberrypi.local" it seems not not like it as it the dnsmasq will not restart.

Question: since i change back and forth between wired and wifi and various routers, I hope to reference raspberrypi.local to make it easier to connect under various connections. Is there are way to alter dnsmasq to this?

Thanks

> terrycarlin wrote:If you are installing this as root, you need to enter this in the command line.  
  
if you log off and log back on, that code should be included automagicly.

Thanks, that worked, however when im installing rvm, i get the following error:

"Error runing 'make', please read /usr/local/rvm/log/......  
There has been an error while running make. Halting the installation.

> wakummaci wrote:
>
>> terrycarlin wrote:If you are installing this as root, you need to enter this in the command line.  
  
if you log off and log back on, that code should be included automagicly.
> 
>   
  
Thanks, that worked, however when im installing rvm, i get the following error:  
  
"Error runing 'make', please read /usr/local/rvm/log/......  
There has been an error while running make. Halting the installation.

Can you post the log file?

  


I'm the only one having trouble running it with iphone 5?  
I've seen DarkTherapy work which is awesome! Thanks for sharing your knowledge

I've siriproxy up and running on my pi and my ubuntu laptop, but on both it seems like siri isn't communicating with the server, it just connect to apple and not my proxy.  
I've installed the ca.pem file but nothing, it might be my iphone or my server isn't running well?

Thanks.

> orxelm wrote:I'm the only one having trouble running it with iphone 5?  
I've seen DarkTherapy work which is awesome! Thanks for sharing your knowledge   
  
I've siriproxy up and running on my pi and my ubuntu laptop, but on both it seems like siri isn't communicating with the server, it just connect to apple and not my proxy.  
I've installed the ca.pem file but nothing, it might be my iphone or my server isn't running well?  
  
Thanks.

Did you set the DNS on your phones wifi setup to match the siriproxy ip?

> DarkTherapy wrote:
>
>> Can I run a bash script using the system command.  
  
Best wishes.
> 
>   
  
Yes you can, I am currently running a bash script to control my Sky+HD box - via Siri.

Thank you.

I can turn my lights on using a gem and then from the command line call "lightwaverf living socket on"

If I enter this directly into the plugin I get an error, so I thought I would try a bash script

#!/bin/sh   
lightwaverf living socket on

I have called this light.sh and then chmod +x the file.  
If I call this from the command line ./light.sh ---- It works.

If I enter it into the plugin:  
listen_for /power/i do  
say "Enabling the standing light..."  
request_completed  
system("./light.sh")  
end

I don't get any errors and it appears to accept the command but the bash script does not work.

Can anyone suggest what I am doing wrong?

Best wishes.

James.

> Foggy wrote:
>
>> DarkTherapy wrote:
>>
>>> Can I run a bash script using the system command.  
  
Best wishes.
>> 
>>   
  
Yes you can, I am currently running a bash script to control my Sky+HD box - via Siri.
> 
>   
  
Thank you.  
  
I can turn my lights on using a gem and then from the command line call "lightwaverf living socket on"  
  
If I enter this directly into the plugin I get an error, so I thought I would try a bash script  
  
#!/bin/sh   
lightwaverf living socket on  
  
I have called this light.sh and then chmod +x the file.  
If I call this from the command line ./light.sh ---- It works.  
  
If I enter it into the plugin:  
listen_for /power/i do  
say "Enabling the standing light..."  
request_completed  
system("./light.sh")  
end  
  
I don't get any errors and it appears to accept the command but the bash script does not work.  
  
Can anyone suggest what I am doing wrong?  
  
Best wishes.  
  
James.

Try:  
system("sh ./light.sh")

Other than that I can't see why it wouldn't launch? Maybe a chmod 777 the file?

Thank you.

system("sh ./light.sh")  
Just gave me  
[Info - Guzzoni] Received Object: SpeechRecognized  
[Info - Plugin Manager] Processing 'Power '  
[Info - Plugin Manager] Processing plugin #<SiriProxy::Plugin::Example:0x1eec580>  
[Info - Plugin Manager] Matches (?i-mx:power)  
[Info - Plugin Manager] Applicable states:   
[Info - Plugin Manager] Current state:   
[Info - Plugin Manager] Matches, executing block  
[Info - Plugin Manager] Say: Enabling the standing light...  
[Info - Plugin Manager] Sending Request Completed  
sh: 0: Can't open ./light.sh

Maybe a chmod 777 the file?  
changed to  
-rwxrwxrwx 1 root root 42 Jan 1 16:05 light.sh

Still no joy.

Have I got by bash script correct?  
it is just two lines  
#!/bin/sh   
lightwaverf living socket on

Do I need to add anything else?

Best wishes.

James.

> Foggy wrote:Thank you.  
  
system("sh ./light.sh")  
Just gave me  
[Info - Guzzoni] Received Object: SpeechRecognized  
[Info - Plugin Manager] Processing 'Power '  
[Info - Plugin Manager] Processing plugin #<SiriProxy::Plugin::Example:0x1eec580>  
[Info - Plugin Manager] Matches (?i-mx:power)  
[Info - Plugin Manager] Applicable states:   
[Info - Plugin Manager] Current state:   
[Info - Plugin Manager] Matches, executing block  
[Info - Plugin Manager] Say: Enabling the standing light...  
[Info - Plugin Manager] Sending Request Completed  
sh: 0: Can't open ./light.sh  
  
Maybe a chmod 777 the file?  
changed to  
-rwxrwxrwx 1 root root 42 Jan 1 16:05 light.sh  
  
Still no joy.  
  
Have I got by bash script correct?  
it is just two lines  
#!/bin/sh   
lightwaverf living socket on  
  
Do I need to add anything else?  
  
Best wishes.  
  
James.

Maybe it needs the full path to the bash script /root/SiriProxy/light.sh for example.

As soon as I try and put a path /root/SiriProxy/light.sh  
(I moved it there) and chmod 777 again.

I get these errors.

/usr/local/rvm/gems/ruby-1.9.3-p327@global/gems/bundler-1.2.3/lib/bundler/rubygems_integration.rb:147:in `block in replace_gem': lightwaverf is not part of the bundle. Add it to Gemfile. (Gem::LoadError)  
from /usr/local/bin/lightwaverf:22:in `<main>'

The only way I seem to get rid of the error is by specifying ./light.sh - but of course that does not work.

Best wishes.

Thank you, that was the problem   
But now i'm facing worse problem:

    `SiriProxy up and running.  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1062c00 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x10628d0>, @zip_stream=#<Zlib::Deflate:0x10628b8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x16cb0f0 @manager=#<SiriProxy::PluginManager:0x10625b8 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
/home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `encode': "\xA3" on UTF-8 (Encoding::InvalidByteSequenceError)  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `charset_convert'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:442:in `string_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:48:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:70:in `to_str'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:363:in `to_str'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:398:in `to_plist'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:150:in `inject_object_to_output_stream'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:90:in `process_compressed_data'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:58:in `receive_binary_data'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/em/protocols/linetext2.rb:94:in `receive_data'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
   from /home/pi/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
   from /home/pi/SiriProxy/bin/siriproxy:6:in `new'  
   from /home/pi/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
`

Any clue?

> orxelm wrote:  
  
Thank you, that was the problem   
But now i'm facing worse problem:  
  

> 
>     `SiriProxy up and running.  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1062c00 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x10628d0>, @zip_stream=#<Zlib::Deflate:0x10628b8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x16cb0f0 @manager=#<SiriProxy::PluginManager:0x10625b8 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
/home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `encode': "\xA3" on UTF-8 (Encoding::InvalidByteSequenceError)  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `charset_convert'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:442:in `string_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:48:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:70:in `to_str'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:363:in `to_str'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:398:in `to_plist'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:150:in `inject_object_to_output_stream'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:90:in `process_compressed_data'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:58:in `receive_binary_data'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/em/protocols/linetext2.rb:94:in `receive_data'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
   from /home/pi/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
   from /home/pi/SiriProxy/bin/siriproxy:6:in `new'  
   from /home/pi/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
`
>   
  
Any clue?

No idea! Does it work in Ubuntu? You mentioned it running in Ubuntu earlier.

> DarkTherapy wrote:
>
>> orxelm wrote:  
  
Thank you, that was the problem   
But now i'm facing worse problem:  
  

>> 
>>     `SiriProxy up and running.  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1062c00 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x10628d0>, @zip_stream=#<Zlib::Deflate:0x10628b8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x16cb0f0 @manager=#<SiriProxy::PluginManager:0x10625b8 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
/home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `encode': "\xA3" on UTF-8 (Encoding::InvalidByteSequenceError)  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `charset_convert'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:442:in `string_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:48:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:70:in `to_str'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:363:in `to_str'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:398:in `to_plist'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:150:in `inject_object_to_output_stream'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:90:in `process_compressed_data'  
   from /home/pi/SiriProxy/lib/siriproxy/connection.rb:58:in `receive_binary_data'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/em/protocols/linetext2.rb:94:in `receive_data'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
   from /home/pi/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
   from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
   from /home/pi/SiriProxy/bin/siriproxy:6:in `new'  
   from /home/pi/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
   from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
`
>>   
  
Any clue?
> 
>   
  
No idea! Does it work in Ubuntu? You mentioned it running in Ubuntu earlier.

The weirdest thing ever! I get the same error when running the proxy on Ubuntu 12.10

> orxelm wrote:  
  
Apparently i'm not the only one having this issue, here's the solution:  
<https://github.com/plamoni/SiriProxy/issues/389>  
  
Thanks man, you really helped 

No problem, that's a handy link you posted too.

Hello,

This is probably a late request (and a dumb question) but, being a programmer and not much of an electronics guy, can someone provide more with details about the relay piece? I've got SiriProxy set up on a VM as well as on a Model B Pi but I have no clue what to do regarding the relay: how to get one, how to wire/install it, etc.

I ordered a "SainSmart 8-Channel 5V Relay Module for Arduino DSP AVR PIC ARM" (<http://www.amazon.com/gp/product/B0057OC5WK>) but I'm not sure if this is the right equipment and how to use it.

Do I need an electronics expert to help me set it up?

Your help is appreciated.

-al

> alankernel wrote:Hello,  
  
This is probably a late request (and a dumb question) but, being a programmer and not much of an electronics guy, can someone provide more with details about the relay piece? I've got SiriProxy set up on a VM as well as on a Model B Pi but I have no clue what to do regarding the relay: how to get one, how to wire/install it, etc.  
  
I ordered a "SainSmart 8-Channel 5V Relay Module for Arduino DSP AVR PIC ARM" (<http://www.amazon.com/gp/product/B0057OC5WK>) but I'm not sure if this is the right equipment and how to use it.   
  
Do I need an electronics expert to help me set it up?  
  
Your help is appreciated.  
  
-al

That relay board will work fine. You'll notice it has a vcc pin - connect that to the RasPi's 5v pin. A gnd pin - connect that to the RasPi's gnd. Then the other 8 pins are the signal lines to activate each relay, these you connect to the GPIO, you'll need to look up a GPIO schematic to get the PIN numbers that you'll access in software.

There are single relay boards like the one you've bought that would work fine too. Basically the circuit is constantly connected to 5 volts and when the RasPi sends 3.3v through one if its GPIO pins the relay board sends 5v to its corresponding relay.

In fact, my first garage door opener prototype used the same board you've bought! I got the same board for arduino use but it's fine for the Pi too.

Here's a photo: [https://www.dropbox.com/s/j124p8gjmpauu ... .49.05.jpg](https://www.dropbox.com/s/j124p8gjmpauuvv/2012-12-06%2010.49.05.jpg)

Hi,

Amazing work ! My girlfriend begins to believe in the power of the Raspberry Pi because of you.

I successfully installed SiriProxy and Wiring Pi. If I say "Open the garage door" to Siri, the Rpi lights a LED (0,5 sec). I'm now waiting for a transistor and a relay, bought on ebay.ca, for the last part with a garage door.

Could you share the way you did to make the Rpi starts the server by itself. I understand it's a script that the Rpi will run when it starts (obviously)...but I've no idea how to do it nor where to learn to do it.

Thanks !

> RaspberryMarK wrote:Hi,  
  
Amazing work ! My girlfriend begins to believe in the power of the Raspberry Pi because of you.   
  
I successfully installed SiriProxy and Wiring Pi. If I say "Open the garage door" to Siri, the Rpi lights a LED (0,5 sec). I'm now waiting for a transistor and a relay, bought on ebay.ca, for the last part with a garage door.  
  
Could you share the way you did to make the Rpi starts the server by itself. I understand it's a script that the Rpi will run when it starts (obviously)...but I've no idea how to do it nor where to learn to do it.  
  
Thanks !

Well actually I personally haven't got mine setup to start on boot, I use a program called "screen" to keep the server running when I log out of the ssh session, there is plenty of documentation online regarding startup scripts. I prefer to start it manually in a screen session, then log out.

Thanks for your praise too.

  


> I have the siriproxy server up and running. I'm able to accept requests from both LAN and WAN (VPN was was easier to setup than i anticipated), I just received my relay board and just have one question.  
  
Where exactly do you connect the relay on the garage door circuit board?  
  
I have an older model genie system, and there isn't a secondary connection terminal and all of the wires are in prefabbed connectors, no screw down terminals. I don't mind cutting one of the wires in the name of home automation.

I have no idea without at least seeing the manual for the system. Usually you hear a relay click on inside the electronics, maybe you could tap into that if there is one.

My current project is to get this to control my central heating.

"Siri, set the thermostat to 20 degree's"

realtek, Setting the thermostat to 20 degree's"....

haha... can't wait!

As long as it doesn't say, "realtek, sorry I cannot do that"

I have the same question, but maybe less competent : what type of cable do I use to connect from the relay to the garage door circuit board and, according to the picture DarkTherapy kindly provided, there appear to be two cables coming out of the relay. Which pins/slots do they go from on the relay and where do they end up on the circuit board?  
I admit, I'm a complete noob in electronics/electricity.  
Thank you.

> I have the siriproxy server up and running. I'm able to accept requests from both LAN and WAN (VPN was was easier to setup than i anticipated), I just received my relay board and just have one question.  
  
Where exactly do you connect the relay on the garage door circuit board?  
  
I have an older model genie system, and there isn't a secondary connection terminal and all of the wires are in prefabbed connectors, no screw down terminals. I don't mind cutting one of the wires in the name of home automation.

You do not need to jailbreak your iPhone to access siriproxy over WAN (iPhone 5)

The way I have mine set up is as follows.

My router has custom firmware (dd-wrt will work but I used something else) with a VPN server built in. I enabled the VPN server and made the DNS server on the router the raspberrypi local ip. Took not even 5 min to setup and works like a charm. I leave VPN off unless I need to call upon siriproxy. (90% of the time I only use it at home anyway)

[quote]by realtek » Wed Jan 09, 2013 10:49 am  
I'm not sure if this has been mentioned on here as the thread is too long for me to read end to end but to get this working over the internet, it is possible if you jailbreak your phone. [/quote]

I figured out where to attach the relay. There are some screw terminals for the wall plate opener and for the safety beam. I found that If I bridge the wall plate terminals for 2 seconds the door opens. So I am placing the replay there.

As for connecting the relay. Mine is on a PCB and the diagram shows (when looking at the relay from the screw terminals) the middle is common and the right is unswitched and the left is the switch position. I will post a picture later.

[quote]I have the same question, but maybe less competent : what type of cable do I use to connect from the relay to the garage door circuit board and, according to the picture DarkTherapy kindly provided, there appear to be two cables coming out of the relay. Which pins/slots do they go from on the relay and where do they end up on the circuit board?  
I admit, I'm a complete noob in electronics/electricity. Thank you[/quote]

When I try executing siriproxy, I get this (but nothing is running on port 443. I am doing this on a fresh wheezy image. I have also tried this as root but I then get 'require' cannot load such file)

Starting SiriProxy on port 443..  
/home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:526:in `start_tcp_server': no acceptor (port is in use or requires root privileges) (RuntimeError)  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:526:in `start_server'  
from /home/pi/SiriProxy/lib/siriproxy.rb:19:in `block in initialize'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `call'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
from /home/pi/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
from ./siriproxy:6:in `new'  
from ./siriproxy:6:in `<main>'  
pi@raspberrypi:~/SiriProxy/bin$

Hi DarkTheorpy,

Yes just as I saw your post I was checking the origional instructions!

I was running it as pi and then just the last command as root which looks like where I went wrong.

I am going through the steps again as root.

Thanks!

Hi

I´m running as "pi" on a clean install "wheezy" and follow the steps @idownloadblog. I swaped commands 11, 12 and 13 to 12, 13, 11.

But when i type "rvmsudo siriproxy server" i get this error:

    `Warning: can not check `/etc/sudoers` for `secure_path`, falling back to call via `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_path=1 to avoid the warning.config.yml not found. Copy config.example.yml to config.yml, then modify it.  
`

And when i type "siriproxy server" i get this error:

> Starting SiriProxy on port 443..  
/home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:526:in `start_tcp_server': no acceptor (port is in use or requires root privileges) (RuntimeError)  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:526:in `start_server'  
from /home/pi/SiriProxy/lib/siriproxy.rb:19:in `block in initialize'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `call'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
from /home/pi/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
from /home/pi/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
from /home/pi/SiriProxy/bin/siriproxy:6:in `new'  
from /home/pi/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
from /home/pi/.rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  


Where is my mistake   
Thanks ... Rikka

ok thx

but now im loged in as pi and type "sudo -s", follow the steps until "rvm install 1.9.3"

    `root@raspberrypi:/home/pi# rvm install 1.9.3  
bash: rvm: command not found  
`

Can you help pls

> Rikka wrote:ok thx  
  
but now im loged in as pi and type "sudo -s", follow the steps until "rvm install 1.9.3"  
  

> 
>     `root@raspberrypi:/home/pi# rvm install 1.9.3  
bash: rvm: command not found  
`
>   
  
  
Can you help pls 

You may need to enter this after you get in to root.  
in the command line.  
This should be done automagicly if you just logged in as root or did a  
The - is very important.

ok thanks for your patience but now i´m at this point

    `root@raspberrypi:~/SiriProxy# rvmsudo siriproxy server  
Warning: `secure_path` found in `/etc/sudoers`, falling back to call via `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_path=1 to avoid the warning.Starting SiriProxy on port 443..  
SiriProxy up and running.  
`

and if if starting siri on my iPhone the server crashes

    `/usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine': Interrupt  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
        from /root/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
        from /root/SiriProxy/bin/siriproxy:6:in `new'  
        from /root/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
`

Thanks for your help

I got this warning. To avoid it, I entered the command that it included in it and re-ran it:  
export rvmsudo_secure_path=1

> Rikka wrote:ok thanks for your patience but now i´m at this point  

> 
>     `root@raspberrypi:~/SiriProxy# rvmsudo siriproxy server  
Warning: `secure_path` found in `/etc/sudoers`, falling back to call via `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_path=1 to avoid the warning.Starting SiriProxy on port 443..  
SiriProxy up and running.  
`
>   
  
and if if starting siri on my iPhone the server crashes  

> 
>     `/usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine': Interrupt  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
        from /root/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
        from /root/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
        from /root/SiriProxy/bin/siriproxy:6:in `new'  
        from /root/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
        from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
`
>   
  
Thanks for your help 

ok i think i found my problem ...

I have a iPhone 4s iOS 6.0.1 and i just read that on iOS 6 guzzoni is wrong and kryten is right. Can anyone confirm ??  
And i come from Germany and [here](http://knx-user-forum.de/244727-post173.html) i read that for Germany it is "de-de.kryten.a**le.com" is it right ??

So here "sudo nano /etc/dnsmasq.conf" i must add --> address=/de-de.kryten.a**le.com/(your_machine's_ip_address) right ??

@alankernel:  
must i run the command every time before starting the Proxy ??

Thanks ... Rikka

@Rikka  
I'll share with you a note-to-self that I kept. Note that, like DarkTherapy mentioned, I'm running everything as root..

    `To run SiriProxy after booting:  
1\. If IP changed:  
vi /etc/dnsmasq.conf  
   -re-edit the ip: address=/guzzoni.apple.com/<new ip>  
Issue command:  
/etc/init.d/dnsmasq restart  
  
2\. Issue the commands:  
root@raspberrypi:~/SiriProxy# export rvmsudo_secure_path=1  
root@raspberrypi:~/SiriProxy# [[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"  
root@raspberrypi:~/SiriProxy# siriproxy server`

> Rikka wrote:ok i think i found my problem ...  
  
I have a iPhone 4s iOS 6.0.1 and i just read that on iOS 6 guzzoni is wrong and kryten is right. Can anyone confirm ??  
And i come from Germany and [here](http://knx-user-forum.de/244727-post173.html) i read that for Germany it is "de-de.kryten.a**le.com" is it right ??   
  
So here "sudo nano /etc/dnsmasq.conf" i must add --> address=/de-de.kryten.a**le.com/(your_machine's_ip_address) right ??  
  
@alankernel:  
must i run the command every time before starting the Proxy ??  
  
Thanks ... Rikka 

@RugYG  
You mentioned that you'd post a picture of your setup. I was wondering if you have done it already and I missed it.  
Thank you

> You do not need to jailbreak your iPhone to access siriproxy over WAN (iPhone 5)   
  
The way I have mine set up is as follows.  
  
My router has custom firmware (dd-wrt will work but I used something else) with a VPN server built in. I enabled the VPN server and made the DNS server on the router the raspberrypi local ip. Took not even 5 min to setup and works like a charm. I leave VPN off unless I need to call upon siriproxy. (90% of the time I only use it at home anyway)  
  

>
>> by realtek » Wed Jan 09, 2013 10:49 am  
I'm not sure if this has been mentioned on here as the thread is too long for me to read end to end but to get this working over the internet, it is possible if you jailbreak your phone. 
> 
>   
  
I figured out where to attach the relay. There are some screw terminals for the wall plate opener and for the safety beam. I found that If I bridge the wall plate terminals for 2 seconds the door opens. So I am placing the replay there.   
  
As for connecting the relay. Mine is on a PCB and the diagram shows (when looking at the relay from the screw terminals) the middle is common and the right is unswitched and the left is the switch position. I will post a picture later.   
  

>
>> I have the same question, but maybe less competent : what type of cable do I use to connect from the relay to the garage door circuit board and, according to the picture DarkTherapy kindly provided, there appear to be two cables coming out of the relay. Which pins/slots do they go from on the relay and where do they end up on the circuit board?  
I admit, I'm a complete noob in electronics/electricity. Thank you

Alright i just finished wiring everything up. Sorry it took so long. I had to run wire from my office to my garage. I wanted to have the raspberryPi in my office so it can be hard wired in to the network and so i don't have to dedicate it to just this project.

The relay board is powered by a 5v USB wall plug and USB cord i had laying around. i cut the cord and just used the red and black wires, these are the wires refereed to as the main power and ground on the wiring diagram

Here is the wiring diagram for my setup:  
<https://www.dropbox.com/s/5oqr11vfbl5b3rg/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Wiring%20Diagram.jpg>

Relay board used:  
<https://www.dropbox.com/s/f4jxvw1vnkmi1i3/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Top.JPG>

<https://www.dropbox.com/s/243jjdxvky7lv2k/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Front.JPG>

Wall switch and where it connects:  
<https://www.dropbox.com/s/bp76j7hfyqa0cig/RaspberryPi__Siri%20Open%20Garage%20Door_Garage%20Door%20Wall%20Switch%20Front.JPG>

<https://www.dropbox.com/s/lzrwpwfqrxwj36t/RaspberryPi__Siri%20Open%20Garage%20Door_Garage%20Door%20Wall%20Switch%20Back.JPG>

<https://www.dropbox.com/s/5jmq4on4aew73ky/RaspberryPi__Siri%20Open%20Garage%20Door_Garage%20Door%20Safety%20Beam%20and%20Wall%20Switch%20Terminals.JPG>

Door sensor:  
<https://www.dropbox.com/s/ppcjdworgfh84tb/RaspberryPi__Siri%20Open%20Garage%20Door_Door%20Sensor.JPG>

How i installed the relay board in the garage door housing:  
<https://www.dropbox.com/s/1yhk2gcys31v4m1/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Installed.JPG>

  


I got everything working up until command 16 on the iDownloadBlog tutorial. When I type "rvmsudo siriproxy server" in the directory ~/SiriProxy, I get the following error:

Warning: can not check `/etc/sudoers` for `secure_path`, falling back to call via `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_path=1 to avoid the warning./usr/bin/env: siriproxy: No such file or directory

How do I fix this? I did everything right... I think.....

@zstryker  
Please refer to the earlier discussion we had about this topic where I provided a summary of things you need to do, one of which is mentioned in this warning, which is: export rvmsudo_secure_path=1  
Also, note that it's best to run all steps as root.

> zstryker wrote:I got everything working up until command 16 on the iDownloadBlog tutorial. When I type "rvmsudo siriproxy server" in the directory ~/SiriProxy, I get the following error:  
  
Warning: can not check `/etc/sudoers` for `secure_path`, falling back to call via `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_path=1 to avoid the warning./usr/bin/env: siriproxy: No such file or directory  
  
How do I fix this? I did everything right... I think.....

So, basically, I should re-run the setup, logged in as root, and then run "export rvmsudo_secure_path=1" before starting the server?

> alankernel wrote:@zstryker  
Please refer to the earlier discussion we had about this topic where I provided a summary of things you need to do, one of which is mentioned in this warning, which is: export rvmsudo_secure_path=1  
Also, note that it's best to run all steps as root.  
  

>
>> I got everything working up until command 16 on the iDownloadBlog tutorial. When I type "rvmsudo siriproxy server" in the directory ~/SiriProxy, I get the following error:  
  
Warning: can not check `/etc/sudoers` for `secure_path`, falling back to call via `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_path=1 to avoid the warning./usr/bin/env: siriproxy: No such file or directory  
  
How do I fix this? I did everything right... I think.....

Based on my experience, that should do, but I'll defer to DarkTherapy as he's the master in this domain.

> zstryker wrote:So, basically, I should re-run the setup, logged in as root, and then run "export rvmsudo_secure_path=1" before starting the server?  
  

>
>> alankernel wrote:@zstryker  
Please refer to the earlier discussion we had about this topic where I provided a summary of things you need to do, one of which is mentioned in this warning, which is: export rvmsudo_secure_path=1  
Also, note that it's best to run all steps as root.  
  

>>
>>> I got everything working up until command 16 on the iDownloadBlog tutorial. When I type "rvmsudo siriproxy server" in the directory ~/SiriProxy, I get the following error:  
  
Warning: can not check `/etc/sudoers` for `secure_path`, falling back to call via `/usr/bin/env`, this breaks rules from `/etc/sudoers`. export rvmsudo_secure_path=1 to avoid the warning./usr/bin/env: siriproxy: No such file or directory  
  
How do I fix this? I did everything right... I think.....

Found the post by jarrah31, with that I managed to get "Starting SiriProxy on port 443.. Siriproxy up and running!" But, when I connected with my brother's iPad 3 (I've got an ipad 2...), the server crashed, and showed a lot of code that I couldn't understand... I'm going to do a clean install, and then see if it'll work tomorrow. I think I've got a pretty good understanding of how to do it now.

One question- When following the instructions in jarrah31's post, I edited siriproxy.gemspec (sudo nano (siriproxy.gemspec directory)) and there was nothing there... Again, I think a clean install should help, as I had just installed siriproxy as the pi user, and that might have broken it... Can anyone verify that jarrah31's instructions work?

@RugYG  
Thanks or sharing the pictures of your setup. I'm still a bit confused though.  
In your wiring diagram:

Left side:   
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. Relay 1 signal for command to open door (Question: where does that connect on Pi?)

Right side:  
1\. Black wire goes to "Right Wall Switch Terminal" (Question: is this going into the right button of the garage door wall switch?)  
2\. Red wire goes to "Left Wall Switch Terminal" (Question: is this going into the left button of the garage door wall switch?)  
3\. To Main Power (Question: From where? Is this fed from a wall socket?)  
4\. To Raspberry Pi (Question: I wasn't aware that we needed to connect relay to Pi through a power wire)

> RugYG wrote:Alright i just finished wiring everything up. Sorry it took so long. I had to run wire from my office to my garage. I wanted to have the raspberryPi in my office so it can be hard wired in to the network and so i don't have to dedicate it to just this project.  
  
The relay board is powered by a 5v USB wall plug and USB cord i had laying around. i cut the cord and just used the red and black wires, these are the wires refereed to as the main power and ground on the wiring diagram  
  
Here is the wiring diagram for my setup:  
<https://www.dropbox.com/s/5oqr11vfbl5b3rg/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Wiring%20Diagram.jpg>  
  
Relay board used:  
<https://www.dropbox.com/s/f4jxvw1vnkmi1i3/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Top.JPG>  
  
<https://www.dropbox.com/s/243jjdxvky7lv2k/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Front.JPG>  
  
Wall switch and where it connects:  
<https://www.dropbox.com/s/bp76j7hfyqa0cig/RaspberryPi__Siri%20Open%20Garage%20Door_Garage%20Door%20Wall%20Switch%20Front.JPG>  
  
<https://www.dropbox.com/s/lzrwpwfqrxwj36t/RaspberryPi__Siri%20Open%20Garage%20Door_Garage%20Door%20Wall%20Switch%20Back.JPG>  
  
<https://www.dropbox.com/s/5jmq4on4aew73ky/RaspberryPi__Siri%20Open%20Garage%20Door_Garage%20Door%20Safety%20Beam%20and%20Wall%20Switch%20Terminals.JPG>  
  
Door sensor:  
<https://www.dropbox.com/s/ppcjdworgfh84tb/RaspberryPi__Siri%20Open%20Garage%20Door_Door%20Sensor.JPG>  
  
How i installed the relay board in the garage door housing:  
<https://www.dropbox.com/s/1yhk2gcys31v4m1/RaspberryPi__Siri%20Open%20Garage%20Door_Relay%20Board%20Installed.JPG>

@alankernel

Left Side  
The main power and ground for the relay board goes to a USB wall charger (I used one of these because they generally output 5v @ 1a. Also I have my raspberryPi in my office and not in my garage so less wire to run.)

I believe the provided code uses pin 1 which is the 3.3v output for the relay 1 signal. (Someone correct me if I'm wrong)  
I am working on some code to use pin 11 which is GPIO 17

Right Side  
You can go all the way to the button if you want. However to save wire, you can just connect to where the wall switch connects to your garage door opener. Basically all you are doing is completing the circuit to open the door (At least that is how my garage door opener model works)

The second relay isn't required. It's something I added to this project that i thought would be a cool addition.

The second relay is used to monitor the door sensor (The kind used with alarm systems to see if a window is open or closed)

I have this circuit as follows. Power from USB wall charger goes to the door sensor, then from the sensor to the relay 2 command, (The sensor is installed so when the door is closed the loop is complete) the relay then has the first terminal empty, power from the wall charger to the middle terminal and a line from the third terminal to a resistor then to the raspberryPi pin 12 which is GPIO pin 18 (any input to the raspberryPi must be 3.3v)

Once I finish the code, you will be able to ask "is the garage door closed?" or when you ask "Open the garage door" Siri can respond "The garage door is already open" if the door is already open.

The way everything is setup right now you can open and close the garage door with the same command.  
(Say "open the garage door" the door will open {if closed} and if you say "open the garage door" again it will close)

With the added sensor it's forcing you to use two commands and so that the garage door will only open when it is closed and vice versa. This is ideal for those who plan to use siriproxy over WAN (VPN)

RugYG

> by alankernel » Mon Jan 14, 2013 3:23 pm  
  
@RugYG  
Thanks or sharing the pictures of your setup. I'm still a bit confused though.  
In your wiring diagram:  
  
Left side:   
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. Relay 1 signal for command to open door (Question: where does that connect on Pi?)  
  
Right side:  
1\. Black wire goes to "Right Wall Switch Terminal" (Question: is this going into the right button of the garage door wall switch?)  
2\. Red wire goes to "Left Wall Switch Terminal" (Question: is this going into the left button of the garage door wall switch?)  
3\. To Main Power (Question: From where? Is this fed from a wall socket?)  
4\. To Raspberry Pi (Question: I wasn't aware that we needed to connect relay to Pi through a power wire)

@RugYG  
Thank you very much for explaining the details of your setup. My initial plan was not to use a sensor but after reading your description I'm more interested in doing it (and also definitely how to VPN in and use SIRI remotely).

For now, if I don't go for the sensor and just go with the simple setup, I wanted to validate with you that I would be ok if I do the following (Please note that I have a 5v/100mA wall charger for the Pi and I had a non-charged USB hub that I use to connect peripherals to the Pi, but I swapped it with another one that comes with a charger since I heard the non-charged one may suck some of the power from the Pi):

Left Side:  
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. IN 1 on Relay connects to Pin 1 on Pi, which will give signal for command to open door

Right Side:  
1\. Black wire connects from common (COM) on Relay to where the right wall switch connects to my garage door opener - in the garage door engine (I'm assuming I can pinpoint this by tracing where the right wall switch cable connects to)  
2\. Red wire connects from Normally Open (NO) on Relay to where the left wall switch connects to my garage door opener - in the garage door engine (same assumption)

Finally, since I'm not implementing the sensor (yet), I don't have to worry about the Relay 2 in or out connectivity.

Thank you again

> RugYG wrote:@alankernel  
  
Left Side  
The main power and ground for the relay board goes to a USB wall charger (I used one of these because they generally output 5v @ 1a. Also I have my raspberryPi in my office and not in my garage so less wire to run.)  
  
I believe the provided code uses pin 1 which is the 3.3v output for the relay 1 signal. (Someone correct me if I'm wrong)  
I am working on some code to use pin 11 which is GPIO 17  
  
Right Side  
You can go all the way to the button if you want. However to save wire, you can just connect to where the wall switch connects to your garage door opener. Basically all you are doing is completing the circuit to open the door (At least that is how my garage door opener model works)  
  
The second relay isn't required. It's something I added to this project that i thought would be a cool addition.   
  
The second relay is used to monitor the door sensor (The kind used with alarm systems to see if a window is open or closed)  
  
I have this circuit as follows. Power from USB wall charger goes to the door sensor, then from the sensor to the relay 2 command, (The sensor is installed so when the door is closed the loop is complete) the relay then has the first terminal empty, power from the wall charger to the middle terminal and a line from the third terminal to a resistor then to the raspberryPi pin 12 which is GPIO pin 18 (any input to the raspberryPi must be 3.3v)  
  
Once I finish the code, you will be able to ask "is the garage door closed?" or when you ask "Open the garage door" Siri can respond "The garage door is already open" if the door is already open.  
  
The way everything is setup right now you can open and close the garage door with the same command.  
(Say "open the garage door" the door will open {if closed} and if you say "open the garage door" again it will close)  
  
With the added sensor it's forcing you to use two commands and so that the garage door will only open when it is closed and vice versa. This is ideal for those who plan to use siriproxy over WAN (VPN)  
  
RugYG  
  

>
>> by alankernel » Mon Jan 14, 2013 3:23 pm  
  
@RugYG  
Thanks or sharing the pictures of your setup. I'm still a bit confused though.  
In your wiring diagram:  
  
Left side:   
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. Relay 1 signal for command to open door (Question: where does that connect on Pi?)  
  
Right side:  
1\. Black wire goes to "Right Wall Switch Terminal" (Question: is this going into the right button of the garage door wall switch?)  
2\. Red wire goes to "Left Wall Switch Terminal" (Question: is this going into the left button of the garage door wall switch?)  
3\. To Main Power (Question: From where? Is this fed from a wall socket?)  
4\. To Raspberry Pi (Question: I wasn't aware that we needed to connect relay to Pi through a power wire)

@alankernel

No problem, VPN is very handy but lets work on geting your Pi setup first then we can worry about that.

Double check your wall charger if you are using a usb splitter i wouldnt use anything under 500mA (1a would be best)

Left side looks good

Right side looks good. Only change would be to switch the COM and N.O. make the COM the red (Positive) wire {I just noticed that and will probably switch mine, it shouldnt matter because all you are doing is briding the gab between the two leads}

Correct about the second relay, you can ignore that part.

RugYG

> by alankernel » Mon Jan 14, 2013 11:04 pm   
  
@RugYG  
Thank you very much for explaining the details of your setup. My initial plan was not to use a sensor but after reading your description I'm more interested in doing it (and also definitely how to VPN in and use SIRI remotely).  
  
For now, if I don't go for the sensor and just go with the simple setup, I wanted to validate with you that I would be ok if I do the following (Please note that I have a 5v/100mA wall charger for the Pi and I had a non-charged USB hub that I use to connect peripherals to the Pi, but I swapped it with another one that comes with a charger since I heard the non-charged one may suck some of the power from the Pi):  
  
Left Side:  
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. IN 1 on Relay connects to Pin 1 on Pi, which will give signal for command to open door   
  
Right Side:  
1\. Black wire connects from common (COM) on Relay to where the right wall switch connects to my garage door opener - in the garage door engine (I'm assuming I can pinpoint this by tracing where the right wall switch cable connects to)  
2\. Red wire connects from Normally Open (NO) on Relay to where the left wall switch connects to my garage door opener - in the garage door engine (same assumption)  
  
Finally, since I'm not implementing the sensor (yet), I don't have to worry about the Relay 2 in or out connectivity.  
  
Thank you again

@RugYG  
Thanks! I will try this out and let you know.

> RugYG wrote:@alankernel  
  
No problem, VPN is very handy but lets work on geting your Pi setup first then we can worry about that.  
  
Double check your wall charger if you are using a usb splitter i wouldnt use anything under 500mA (1a would be best)  
  
Left side looks good  
  
Right side looks good. Only change would be to switch the COM and N.O. make the COM the red (Positive) wire {I just noticed that and will probably switch mine, it shouldnt matter because all you are doing is briding the gab between the two leads}   
  
Correct about the second relay, you can ignore that part.  
  
RugYG  
  

>
>> by alankernel » Mon Jan 14, 2013 11:04 pm   
  
@RugYG  
Thank you very much for explaining the details of your setup. My initial plan was not to use a sensor but after reading your description I'm more interested in doing it (and also definitely how to VPN in and use SIRI remotely).  
  
For now, if I don't go for the sensor and just go with the simple setup, I wanted to validate with you that I would be ok if I do the following (Please note that I have a 5v/100mA wall charger for the Pi and I had a non-charged USB hub that I use to connect peripherals to the Pi, but I swapped it with another one that comes with a charger since I heard the non-charged one may suck some of the power from the Pi):  
  
Left Side:  
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. IN 1 on Relay connects to Pin 1 on Pi, which will give signal for command to open door   
  
Right Side:  
1\. Black wire connects from common (COM) on Relay to where the right wall switch connects to my garage door opener - in the garage door engine (I'm assuming I can pinpoint this by tracing where the right wall switch cable connects to)  
2\. Red wire connects from Normally Open (NO) on Relay to where the left wall switch connects to my garage door opener - in the garage door engine (same assumption)  
  
Finally, since I'm not implementing the sensor (yet), I don't have to worry about the Relay 2 in or out connectivity.  
  
Thank you again

I got the server to start, but when I talk to siri using a 4S, I get the error:

    `Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x21f7608 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x21f7500>, @zip_stream=#<Zlib::Deflate:0x21f74e8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x289c5c0 @manager=#<SiriProxy::PluginManager:0x21f7110 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
/usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `encode': "\xFF" on UTF-8 (Encoding::InvalidByteSequenceError)  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `charset_convert'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:442:in `string_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:48:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:70:in `to_str'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:363:in `to_str'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:398:in `to_plist'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:150:in `inject_object_to_output_stream'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:90:in `process_compressed_data'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:58:in `receive_binary_data'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/em/protocols/linetext2.rb:94:in `receive_data'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
   from /root/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
   from /root/SiriProxy/bin/siriproxy:6:in `new'  
   from /root/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
zlib(finalizer): the stream was freed prematurely.`

Could someone point me toward a post that might help? I've already installed this a couple of times, and I'm desperate for it to work so I can use it to control stuff from siri...

> zstryker wrote:I got the server to start, but when I talk to siri using a 4S, I get the error:  
  

> 
>     `Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x21f7608 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x21f7500>, @zip_stream=#<Zlib::Deflate:0x21f74e8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x289c5c0 @manager=#<SiriProxy::PluginManager:0x21f7110 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
/usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `encode': "\xFF" on UTF-8 (Encoding::InvalidByteSequenceError)  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `charset_convert'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:442:in `string_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:48:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:70:in `to_str'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:363:in `to_str'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:398:in `to_plist'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:150:in `inject_object_to_output_stream'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:90:in `process_compressed_data'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:58:in `receive_binary_data'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/em/protocols/linetext2.rb:94:in `receive_data'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
   from /root/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
   from /root/SiriProxy/bin/siriproxy:6:in `new'  
   from /root/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
zlib(finalizer): the stream was freed prematurely.`
>   
  
Could someone point me toward a post that might help? I've already installed this a couple of times, and I'm desperate for it to work so I can use it to control stuff from siri...

<https://github.com/plamoni/SiriProxy/issues/389>

I tried changing the line on the file, but it didn't work, and I got the same error. There was another post, that said to move something into something, but I couldn't find the directory to move that thing into...

> DarkTherapy wrote:
>
>> zstryker wrote:I got the server to start, but when I talk to siri using a 4S, I get the error:  
  

>> 
>>     `Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x21f7608 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x21f7500>, @zip_stream=#<Zlib::Deflate:0x21f74e8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x289c5c0 @manager=#<SiriProxy::PluginManager:0x21f7110 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
/usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `encode': "\xFF" on UTF-8 (Encoding::InvalidByteSequenceError)  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:217:in `charset_convert'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:442:in `string_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:48:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `block in dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `map'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:550:in `dict_to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFTypes.rb:243:in `to_binary'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbBinaryCFPropertyList.rb:70:in `to_str'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:363:in `to_str'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/CFPropertyList-2.2.0/lib/rbCFPropertyList.rb:398:in `to_plist'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:150:in `inject_object_to_output_stream'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:90:in `process_compressed_data'  
   from /root/SiriProxy/lib/siriproxy/connection.rb:58:in `receive_binary_data'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/em/protocols/linetext2.rb:94:in `receive_data'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run_machine'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/gems/eventmachine-1.0.0/lib/eventmachine.rb:187:in `run'  
   from /root/SiriProxy/lib/siriproxy.rb:16:in `initialize'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `new'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:96:in `start_server'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:85:in `run_server'  
   from /root/SiriProxy/lib/siriproxy/command_line.rb:37:in `initialize'  
   from /root/SiriProxy/bin/siriproxy:6:in `new'  
   from /root/SiriProxy/bin/siriproxy:6:in `<top (required)>'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `load'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/siriproxy:19:in `<main>'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `eval'  
   from /usr/local/rvm/gems/ruby-1.9.3-p362@SiriProxy/bin/ruby_noexec_wrapper:14:in `<main>'  
zlib(finalizer): the stream was freed prematurely.`
>>   
  
Could someone point me toward a post that might help? I've already installed this a couple of times, and I'm desperate for it to work so I can use it to control stuff from siri...
> 
>   
  
<https://github.com/plamoni/SiriProxy/issues/389>

"I tried changing the line on the file, but it didn't work, and I got the same error. There was another post, that said to move something into something, but I couldn't find the directory to move that thing into..."

On my Pi is a dir: /usr/local/rvm/gems

Inside that is the @SiriProxy/gems directory.

I have a CFPropertyList-2.1.1 and mine works fine. If yours is different and not functioning, you can try:   
gem install CFPropertyList --version 2.1.1

I GOT IT!! IT WORKS!! Siri answers my every garage-door-command )  
@RugYG and @DarkTherapy  
Thank you much!  
Now, it's time to do more interesting stuff with this.. How about that VPN thing?

> RugYG wrote:@alankernel  
  
No problem, VPN is very handy but lets work on geting your Pi setup first then we can worry about that.  
  
Double check your wall charger if you are using a usb splitter i wouldnt use anything under 500mA (1a would be best)  
  
Left side looks good  
  
Right side looks good. Only change would be to switch the COM and N.O. make the COM the red (Positive) wire {I just noticed that and will probably switch mine, it shouldnt matter because all you are doing is briding the gab between the two leads}   
  
Correct about the second relay, you can ignore that part.  
  
RugYG  
  

>
>> by alankernel » Mon Jan 14, 2013 11:04 pm   
  
@RugYG  
Thank you very much for explaining the details of your setup. My initial plan was not to use a sensor but after reading your description I'm more interested in doing it (and also definitely how to VPN in and use SIRI remotely).  
  
For now, if I don't go for the sensor and just go with the simple setup, I wanted to validate with you that I would be ok if I do the following (Please note that I have a 5v/100mA wall charger for the Pi and I had a non-charged USB hub that I use to connect peripherals to the Pi, but I swapped it with another one that comes with a charger since I heard the non-charged one may suck some of the power from the Pi):  
  
Left Side:  
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. IN 1 on Relay connects to Pin 1 on Pi, which will give signal for command to open door   
  
Right Side:  
1\. Black wire connects from common (COM) on Relay to where the right wall switch connects to my garage door opener - in the garage door engine (I'm assuming I can pinpoint this by tracing where the right wall switch cable connects to)  
2\. Red wire connects from Normally Open (NO) on Relay to where the left wall switch connects to my garage door opener - in the garage door engine (same assumption)  
  
Finally, since I'm not implementing the sensor (yet), I don't have to worry about the Relay 2 in or out connectivity.  
  
Thank you again

I guess I celebrated too quickly.. 2 things:  
1 - when I connect the wires from the relay to the garage door opener, Siri is able to open and close the garage door but as soon as I use it, I notice that the light on the wall mounted switch goes out and its buttons don't work anymore. any idea why that may be?  
2 - Both the Pi and the relay fell down from the garage ceiling. One of the relays broke (I have 7 left) and the padding within one of the 2 USB ports on the Pi fell out...but - amazingly - they both still work. I guess this attests to the sturdiness of the Pi/relay or to my luck with that incident 

Your suggestion for 1- would be appreciated.

> I GOT IT!! IT WORKS!! Siri answers my every garage-door-command )  
@RugYG and @DarkTherapy  
Thank you much!  
Now, it's time to do more interesting stuff with this.. How about that VPN thing?   
  

>
>> @alankernel  
  
No problem, VPN is very handy but lets work on geting your Pi setup first then we can worry about that.  
  
Double check your wall charger if you are using a usb splitter i wouldnt use anything under 500mA (1a would be best)  
  
Left side looks good  
  
Right side looks good. Only change would be to switch the COM and N.O. make the COM the red (Positive) wire {I just noticed that and will probably switch mine, it shouldnt matter because all you are doing is briding the gab between the two leads}   
  
Correct about the second relay, you can ignore that part.  
  
RugYG  
  

>>
>>> by alankernel » Mon Jan 14, 2013 11:04 pm   
  
@RugYG  
Thank you very much for explaining the details of your setup. My initial plan was not to use a sensor but after reading your description I'm more interested in doing it (and also definitely how to VPN in and use SIRI remotely).  
  
For now, if I don't go for the sensor and just go with the simple setup, I wanted to validate with you that I would be ok if I do the following (Please note that I have a 5v/100mA wall charger for the Pi and I had a non-charged USB hub that I use to connect peripherals to the Pi, but I swapped it with another one that comes with a charger since I heard the non-charged one may suck some of the power from the Pi):  
  
Left Side:  
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. IN 1 on Relay connects to Pin 1 on Pi, which will give signal for command to open door   
  
Right Side:  
1\. Black wire connects from common (COM) on Relay to where the right wall switch connects to my garage door opener - in the garage door engine (I'm assuming I can pinpoint this by tracing where the right wall switch cable connects to)  
2\. Red wire connects from Normally Open (NO) on Relay to where the left wall switch connects to my garage door opener - in the garage door engine (same assumption)  
  
Finally, since I'm not implementing the sensor (yet), I don't have to worry about the Relay 2 in or out connectivity.  
  
Thank you again

I'm so close to getting everything working so that Siri can buzz me in to my apartment building. The hardware is fine: the intercom system connects two pins when you hold the "door" button to let someone in, so I'm using a relay to connect those two pins.

My problem is that I need to keep that relay closed for about 10 seconds so that I have time to get in. I used the following code:

listen_for /can you let me in right now/i do  
say "I'll buzz you in now..."  
request_completed  
system("gpio mode 1 out")  
system("gpio write 1 1")  
system("sleep 10")  
system("gpio write 1 0")  
end

But that sleep 10 bit crashes SiriProxy every time. The relay closes for 10 seconds and then opens again, but after that SiriProxy is out of commission until I restart. Siri never even responds with "I'll buzz you in now..." so I assume it is a buffer issue and it is actually waiting 10 seconds before giving the request completed command (like this guy had here: [http://stackoverflow.com/questions/3084 ... ay-in-ruby](http://stackoverflow.com/questions/3084232/how-to-produce-delay-in-ruby) ).

Someone else had a similar problem but I was lost in the answer: <https://github.com/plamoni/SiriProxy/issues/154>

Anyone have any ideas?

Try moving the "request completed" to after the relay is turned off.

Or you could put the GPIO commands in a separate bash script and have the siriproxy call it with: system("sh /SiriProxy/doorscript.sh")

Maybe that will work?

I've just Googled "ruby multithreading" and that looks like the answer, I'm going to mess with my Server to see of I can get multithreading working, running the relay code in its own thread so SiriProxy can continue in it's own.

> Or you could put the GPIO commands in a separate bash script and have the siriproxy call it with: system("sh /SiriProxy/doorscript.sh") 

If the application (siriproxy?) is waiting for the script to end, then it doesn't matter if it is in a bash script or not; it will still wait.

On the other hand you could use "&" and maybe "nohup" to let siriproxy set it off and forget it.

I think system("nohup bash /SiriProxy/doorscript.sh &") should work, but I can't test it at the moment. (And I can't test it with siriproxy anyway).

> rurwin wrote:
>
>> Or you could put the GPIO commands in a separate bash script and have the siriproxy call it with: system("sh /SiriProxy/doorscript.sh") 
> 
>   
  
If the application (siriproxy?) is waiting for the script to end, then it doesn't matter if it is in a bash script or not; it will still wait.  
  
On the other hand you could use "&" and maybe "nohup" to let siriproxy set it off and forget it.  
  
I think system("nohup bash /SiriProxy/doorscript.sh &") should work, but I can't test it at the moment. (And I can't test it with siriproxy anyway).

Thanks for that, I'll give it a go!

Thanks rurwin,

system("bash /SiriProxy/doorscript.sh &") worked perfectly. My doorscript.sh currently is pretty plain with just:

#! /bin/bash  
# basic door script  
gpio mode 1 out  
gpio write 1 1  
sleep 10  
gpio write 1 0

but I like that I can edit it on the fly.

Hi All

I recently wrote an articel on how to install and configure SiriProxy on PI (and Linux) and how to integrate with other systems using IP. the article also contains a link to a (guaranteed virus/spy where free) full configure Linux VM and PI SD image. All you need to do is change IP, one config file and install certificate on phone and you'll have a working SiriProxy

<http://www.hometoys.com/emagazine/2013/02/siri-home-automation-integration-from-start-to-finish-brpart-1--the-basics-using-a-linux-vm/2087>

Regards

Mark

Hi i am new to all of this but love the idea   
i also want to keep my raspberry pi inside and use it for other things. I was wondering a couple things.   
1\. I like the sensor idea.... but couldnt u just send a 5v signal through the door sensor and then the return wire feeds into one of the pins on the pi.... if it reads voltage you know the door is open or shut... is there any reason to do the relay???? would i still need a resistor????  
2\. can i send all this to the relay with a cat5 or 6 cable from my office. can it carry the 5v??? is it safe???  
well any help would be great   
oh btw this is the relay i got.... it was a few more dollars and i figure i could add to the system if i wanted to do something else.... also the reason for wanting to run cat 5 or 6 to the system.   
Well any help would be great....   
BTW would be great for a pictoral step by step with parts list to do the hardware part. i would but i wouldnt want to screw it up.   
Thanks for all the work you guys have put in

> @alankernel  
  
Left Side  
The main power and ground for the relay board goes to a USB wall charger (I used one of these because they generally output 5v @ 1a. Also I have my raspberryPi in my office and not in my garage so less wire to run.)  
  
I believe the provided code uses pin 1 which is the 3.3v output for the relay 1 signal. (Someone correct me if I'm wrong)  
I am working on some code to use pin 11 which is GPIO 17  
  
Right Side  
You can go all the way to the button if you want. However to save wire, you can just connect to where the wall switch connects to your garage door opener. Basically all you are doing is completing the circuit to open the door (At least that is how my garage door opener model works)  
  
The second relay isn't required. It's something I added to this project that i thought would be a cool addition.   
  
The second relay is used to monitor the door sensor (The kind used with alarm systems to see if a window is open or closed)  
  
I have this circuit as follows. Power from USB wall charger goes to the door sensor, then from the sensor to the relay 2 command, (The sensor is installed so when the door is closed the loop is complete) the relay then has the first terminal empty, power from the wall charger to the middle terminal and a line from the third terminal to a resistor then to the raspberryPi pin 12 which is GPIO pin 18 (any input to the raspberryPi must be 3.3v)  
  
Once I finish the code, you will be able to ask "is the garage door closed?" or when you ask "Open the garage door" Siri can respond "The garage door is already open" if the door is already open.  
  
The way everything is setup right now you can open and close the garage door with the same command.  
(Say "open the garage door" the door will open {if closed} and if you say "open the garage door" again it will close)  
  
With the added sensor it's forcing you to use two commands and so that the garage door will only open when it is closed and vice versa. This is ideal for those who plan to use siriproxy over WAN (VPN)  
  
RugYG  
  

>
>> by alankernel » Mon Jan 14, 2013 3:23 pm  
  
@RugYG  
Thanks or sharing the pictures of your setup. I'm still a bit confused though.  
In your wiring diagram:  
  
Left side:   
1\. Main power goes to Pi's 5v pin  
2\. Main ground goes to Pi's Gnd pin  
3\. Relay 1 signal for command to open door (Question: where does that connect on Pi?)  
  
Right side:  
1\. Black wire goes to "Right Wall Switch Terminal" (Question: is this going into the right button of the garage door wall switch?)  
2\. Red wire goes to "Left Wall Switch Terminal" (Question: is this going into the left button of the garage door wall switch?)  
3\. To Main Power (Question: From where? Is this fed from a wall socket?)  
4\. To Raspberry Pi (Question: I wasn't aware that we needed to connect relay to Pi through a power wire)

  


Hi,

thx for @ of this infos. First of all i´m german and a newbie ;-(

Siri is running on my ip as you can see below.... bit every time i say "test siri proxy" to siri its working and working and them siri say i´m sorry i can not help you.....

WHAT IS MY PROBLEM? please help me....

    `siri@raspberrypi:~$ cd SiriProxy  
siri@raspberrypi:~/SiriProxy$ rvmsudo siriproxy server  
[sudo] password for siri:   
Starting SiriProxy on 192.168.97.26:443..  
SiriProxy up and running.  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1614078 @signature=3, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x16392c0>, @zip_stream=#<Zlib::Deflate:0x16392a8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1c7e590 @manager=#<SiriProxy::PluginManager:0x1639008 @plugins=[...]>>]  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1c7e4a0 @signature=4, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1c7e3c8>, @zip_stream=#<Zlib::Deflate:0x1c7e3b0>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1c7dde0 @manager=#<SiriProxy::PluginManager:0x1c7e170 @plugins=[...]>>]  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1c7dd20 @signature=5, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1c7dc48>, @zip_stream=#<Zlib::Deflate:0x1c7dc30>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1c7d660 @manager=#<SiriProxy::PluginManager:0x1c7d9f0 @plugins=[...]>>]  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1c7d5a0 @signature=6, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1c7d4b0>, @zip_stream=#<Zlib::Deflate:0x1c7d498>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1c7cec8 @manager=#<SiriProxy::PluginManager:0x1c7d228 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
[Info - iPhone] Received Object: DestroyAssistant  
[Info - iPhone] Received Object: ClearContext  
[Info - iPhone] Received Object: SetRestrictions  
[Info - iPhone] Received Object: ClearContext  
[Info - iPhone] Received Object: StartSpeechRequest  
[Info - iPhone] Received Object: SetRequestOrigin  
[Info - User Location] lat: 49.531122072379475, long: 8.343780725466347  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: SpeechPacket  
[Info - iPhone] Received Object: FinishSpeech  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1db75e0 @signature=8, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1db73e8>, @zip_stream=#<Zlib::Deflate:0x1db73b8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1db6908 @manager=#<SiriProxy::PluginManager:0x1db6f80 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1de8bb8 @signature=10, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1de8ab0>, @zip_stream=#<Zlib::Deflate:0x1de8a98>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1e0b988 @manager=#<SiriProxy::PluginManager:0x1de87e0 @plugins=[...]>>]  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1e0b898 @signature=11, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1e0b778>, @zip_stream=#<Zlib::Deflate:0x1e0b760>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1e0a9e0 @manager=#<SiriProxy::PluginManager:0x1e0b1f0 @plugins=[...]>>]  
[Info - iPhone] Received Object: DestroyAssistant  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1e285a8 @signature=14, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1e284d0>, @zip_stream=#<Zlib::Deflate:0x1e284b8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x1c7f820 @manager=#<SiriProxy::PluginManager:0x1d415f0 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
[Info - iPhone] Received Object: DestroyAssistant  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0xf93a98 @signature=16, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0xf93600>, @zip_stream=#<Zlib::Deflate:0xf935e8>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0xf92bb0 @manager=#<SiriProxy::PluginManager:0xf93210 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
[Info - iPhone] Received Object: DestroyAssistant  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1120e48 @signature=18, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1120bf0>, @zip_stream=#<Zlib::Deflate:0x1120b48>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x111fd20 @manager=#<SiriProxy::PluginManager:0x1120668 @plugins=[...]>>]  
[Info - iPhone] Received Object: LoadAssistant  
[Info - iPhone] Received Object: DestroyAssistant  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x1208310 @signature=20, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x1208070>, @zip_stream=#<Zlib::Deflate:0x1208040>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x122bf68 @manager=#<SiriProxy::PluginManager:0x122ca18 @plugins=[...]>>]  
Create server for iPhone connection  
start conn #<SiriProxy::Connection::Iphone:0x122bdd0 @signature=21, @processed_headers=false, @output_buffer="", @input_buffer="", @unzipped_input="", @unzipped_output="", @unzip_stream=#<Zlib::Inflate:0x122bae8>, @zip_stream=#<Zlib::Deflate:0x122bad0>, @consumed_ace=false, @name="iPhone", @ssled=false>  
[Info - Plugin Manager] Plugins laoded: [#<SiriProxy::Plugin::Example:0x122a678 @manager=#<SiriProxy::PluginManager:0x122b5c0 @plugins=[...]>>]  
`
  


Hi,

I have got SiriProxy working but it is not picking up my new commands in "siriproxy-example.rb"

So I have this:

listen_for /turn light on/i do  
say "Switching Light on for you"  
request_completed  
os.system("sudo python /home/pi/Projects/LED_On.py")  
end

It keeps saying "I don't know what you mean by turn light on" ?

I have tried siriproxy bundle before I launch it too.. no luck

Thanks!

I had one or two similar teething problems. Try using simple 'single' word commands and build up from there! I used 'Quake' to launch Quake3 as an example!

____________________________________________  
Looking for where to start - try Kernel Panic - http://goo.gl/EEQ5J

The single most popular request I have received is how to wire up a relay and use SiriProxy to control one's garage door. I normally use a relay built in to my high end security panel which is out of reach for most people. So I bought a PiFace Digital IO board which has two relays, other outputs/inputs, diode protection, etc. The PiFace Digital IO board simply snaps on the Raspberry PI. I then created a SiriProxy PiFace plugin to control my garage door using Siri voice commands. Hopefully, this will make it much easier for everyone to get started. Feel free to modify the plugin for your specific configuration and application interests.

<http://www.youtube.com/watch?v=cpBG9m3LDqI>

Cheers!

http://www.youtube.com/user/TheElvisImprsntr

For those looking to use SiriProxy from outside their local WLAN, you can easily set up a VPN server on your router using open source firmware from [www.dd-wrt.com](http://www.dd-wrt.com). You can also use the firmware to set up a transparent DNS redirect which eliminates the need to manually adjust the DNS settings on your device.

VPN Server  
<https://www.youtube.com/watch?v=N97Xg2IovTA>

DNS Redirect  
<https://www.youtube.com/watch?v=vFSP4iYQPsM>

NOTE: Do not attempt to install dd-wrt on ISP issued equipment. Also use of dd-wrt firmware is for advanced users with networking knowledge/experience.

> Thanks for the instructions. I was able to get it going by following along. Is there code that could be used to check the status of the garage door via a magnetic switch tied to one of the gpio pins? That way a command could return the status of the garage door. It could also add security as it works currently, saying "open the garage door" while it is already open will close it. I know it is possible, but I don't know anything about programming so I don't know how to do it.

My PiFace plugin already checks the status of the door. Watch the video and look at the code.

> realtek wrote:Hi,  
  
I have got SiriProxy working but it is not picking up my new commands in "siriproxy-example.rb"  
  
So I have this:  
  
listen_for /turn light on/i do  
say "Switching Light on for you"  
request_completed  
os.system("sudo python /home/pi/Projects/LED_On.py")  
end  
  
It keeps saying "I don't know what you mean by turn light on" ?  
  
I have tried siriproxy bundle before I launch it too.. no luck  
  
Thanks!

@realtek,Please can you tell me if you managed to get that command working , cause i am having the same problem

> Pr4tik91 wrote:ok. i got things done fine till step 11 and then i think things just went downhill.  
  
when i command "siriproxy gencerts" it returns with "command not found"   
  
not sure what i am doing wrong.   
  
BTW i am using parallels on mac.

You need to source the RVM setup paths again. Either you did not set them up or you logged in at a console which may not source the login script you added the RVM paths.

First post in the forum, so please bear with me!

Hopefully someone will be able to help...

Followed all the instructions from sourceforge.net/p/siriproxyrpi/wiki/Home/ and installed SP from the SD image. Set up the DNS on the iPhone (4S, jailbroken) and copied the gencerts.

It seems SP is running on the Pi (I've pasted the terminal confirmation below). However, when I test the Siri on the iPhone, I get a "Sorry, I don't understand" message.

What could I be doing wrong?

Thanks a lot!

root@raspberrypi:~# siriproxy server  
[Info - Configuration] Loading plugins -- If any fail to load, run `siriproxy bundle` (not `bundle install`) to resolve.  
[Notice - Server] ======================= WARNING: Running as root =============================  
[Notice - Server] You should use -l or the config.yml to specify and non-root user to run under  
[Notice - Server] Running the server as root is dangerous.  
[Notice - Server] ==============================================================================  
[Info - Server] Starting SiriProxy on 0.0.0.0:443...  
[Info - Server] SiriProxy up and running.  
[Info - Plugin Manager] Plugins loaded: Example  
[Info - Plugin Manager] Plugins loaded: Example  
[Info - Plugin Manager] Plugins loaded: Example  
[Info - Plugin Manager] Plugins loaded: Example  
[Info - Plugin Manager] Plugins loaded: Example

I'll assume you are not using iOS7...

A small number of users have reported similar symptoms.

1\. Have you tired removing and generating new certificates? That has worked for some.

2\. Some users have made changes to some of siriproxy source files to solve their problem. <https://github.com/plamoni/SiriProxy/issues/564>
