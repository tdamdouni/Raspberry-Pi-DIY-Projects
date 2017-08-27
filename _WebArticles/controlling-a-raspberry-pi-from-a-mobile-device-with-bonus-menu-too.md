# Controlling a Raspberry Pi from a Mobile Device with Bonus Menu Too

_Captured: 2017-08-27 at 14:02 from [thisdavej.com](http://thisdavej.com/controlling-a-raspberry-pi-from-a-mobile-device-with-bonus-menu-too/)_

![rmain main](http://thisdavej.com/wp-content/uploads/2016/12/rmain-main.png)

In my [Beginner's Guide to Installing Node.js on a Raspberry Pi](http://thisdavej.com/beginners-guide-to-installing-node-js-on-a-raspberry-pi/), I equipped you with the knowledge needed to build an awesome Raspberry Pi system that could also run in a headless mode. We're able to avoid a dedicated monitor, keyboard, and mouse, and this opens a whole new world of possibilities!

This brings us to today's scenario: you've deployed your headless Raspberry Pi in the living room and connected it to your speaker system, soaking in the full stereo sound of your favorite music using [pianobar](https://github.com/PromyLOPh/pianobar), the console-based Pandora player. It's eventually time for bed and you're tired. Should you yank the power cord on your Raspberry Pi and call it a night? Probably not - you might risk corrupting the microSD card. Should you walk upstairs and re-open your laptop so you can SSH into the Pi and safety shut it down? That's a lot of work! Wouldn't it be fantastic if you could connect to your Pi from the mobile phone sitting next to you and issue that `shutdown -h now` command? Controlling your Pi from a mobile device could be very useful in other contexts too beyond listening to music such as IoT applications, computer vision systems, Magic Mirrors, etc.

In this guide, I will teach you how to control your Raspberry Pi from a mobile device. As a bonus, we will create a menu application to make it easier to issue commands since typing complicated command-line syntax on a small screen can prove to be challenging! Let's jump right in!

### Article Contents

### Install SSH client on your mobile phone

Install an SSH client on my mobile phone? Are you serious? Yes, I'm serious. Until recently, I had no idea that SSH clients existed for mobile devices--other than perhaps as a novelty. I've used the venerable [Putty SSH client](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) for Windows, and the OpenSSH client on Linux and OpenBSD. I figured SSH clients must exist for mobile devices, but I never had a context to investigate. Sure enough, SSH clients do exist and I am downright amazed at their usefulness. After all, I wouldn't be taking the time to write this article for you otherwise.

Let's install an SSH client on our mobile device now.

If you are using an Android phone like me, go to the Google Play Store, and [search for SSH clients](https://play.google.com/store/search?q=ssh%20clients&hl=en). I chose the [JuiceSSH client](https://play.google.com/store/apps/details?id=com.sonelli.juicessh&hl=en) and have been happy with it.

For iPhone users, find an SSH client that looks awesome and give it a try. The [Serverauditor SSH client](https://itunes.apple.com/us/app/serverauditor-ssh-shell-console/id549039908?mt=8) looks promising; however, I don't have an iPhone so I could not test it out. Let me know in the comments if you have an SSH client for iOS that you love.

### Verify SSH mobile client works

Let's verify that our SSH mobile client works. First, make sure that you have wi-fi enabled on your mobile device since there is obviously no way to connect to a Raspberry Pi on your local LAN if your mobile device is using a cell connection only, and doesn't have wi-fi enabled.

Next, fire up your Raspberry Pi. If you have used other methods to connect to it through SSH such as an SSH desktop client, try that first and verify that you can establish communication.

#### Option 1 - Activate SSH server using graphical interface

If you can't connect, you may need to enable the SSH server on your Pi as follows:

Launch the `Raspberry Pi Configuration` which is in the Menu under `Preferences`.

![RasPi configuration GUI](http://thisdavej.com/wp-content/uploads/2016/06/rc_gui.png)

Next, click on the `Interfaces` tab (as shown below), ensure that SSH is set to `Enable`, and click `OK`.

![raspi-interfaces](http://thisdavej.com/wp-content/uploads/2016/12/raspi-interfaces.png)

#### Option 2 - Activate SSH server through the command-line

As an alternative approach, if you want to be a command-line hero, issue the following commands from the terminal instead:

Check if SSH server is running:

Enable the ssh server to start on boot and start it now if it's not running:

### Take mobile SSH client for an initial test drive

After the SSH server is up and running (and potentially tested with a desktop SSH client), go ahead and connect to it with the SSH client running on your mobile device. Unless you are hosting highly classified data on your Pi, you may want to go ahead and save the SSH credentials for the `pi` user in the connection settings, if your SSH mobile client allows for this. I have saved connections for multiple Pi systems in my JuiceSSH client, and this makes it very convenient to launch SSH sessions without typing the passwords on constrained on-screen keyboards each and every time!

You should be seeing a command prompt for your Raspberry Pi. Your world has opened up; just think about the possibilities this could provide!

Go ahead and type some commands and see how it works. For example:

As shown in this screenshot below from my SSH session using the JuiceSSH client, there is a popup keyboard available for typing special characters (CTRL, ALT, TAB, etc.) so you have all the capabilities of a standard keyboard. For JuiceSSH, you must touch the screen in the terminal area first, before the special character popup keyboard appears.

![juice ssh](http://thisdavej.com/wp-content/uploads/2016/12/juicessh.png)

### Create menu application for added awesomeness

We're now able to remote into our Pi from our mobile device, and we're feeling on top of the world. But wait, there's more. As a bonus, let's create a menu application to make it easier to invoke commands since, as stated earlier, typing complicated command-line syntax on a small screen can prove to be challenging! Here we go!

Our ultimate goal is to create a menu that looks like this:

![rmenu](http://thisdavej.com/wp-content/uploads/2016/12/rmenu.png)

This will enable us to issue commands through a nice menu-based system efficiently and expediently. I will be providing you with the source code to implement the five menu items shown in the screenshot above. You may ultimately implement different menu commands to suit your specific needs. I'm guessing you will at least want to keep the last two commands which are universally applicable since most of us will have a need from time to time to reboot and shut down our Pi systems from our mobile devices. Remember we wanted a way to shut down our Raspberry Pi remotely instead of yanking the power cord and potentially corrupting our microSD card? Let's get on with it and create the menu application!

#### Create bin directory to make our menu command accessible from any directory

First of all, we will create a directory for our scripts so our scripts can be accessible from any directory on our system without providing a full path name to our script.  
Go ahead and launch a terminal session. This will bring you to a command prompt in your home directory (`/home/pi`).

Next, create a directory called `bin`:

We will need to edit our `.bashrc` file to include this `bin` directory in our `PATH` variable. This will ensure that any scripts located in our newly created `bin` directory can be invoked from any directory on our system without needing to include the full path to the script. Let's first launch a text editor so we can edit the `.bashrc` file:

Add the following line to the bottom of this file:

Save your changes and close the leafpad editor.

To ensure our changes to the `.bashrc` file are processed right away, invoke this command:

Perfect! We are now positioned to create our menu command.

#### Create menu command

We'll use leafpad once again to create and edit our new command. We'll call our command `rmenu` (remote menu):

Create the `rmenu` file. You might find it easier to launch this tutorial page using the Web browser on your Raspberry Pi so you can copy and paste the script contents with ease. The latest Pi browser is based on Chromium, after all, and works excellently! I've also created a [Github Gist](https://gist.github.com/thisdavej/582fde9133baa1123f49c32d2955a4f6) containing the `rmenu` source code.

Add the following contents to the `rmenu` file:

Create a second file in the same directory called `menu1.sh` to store the actual menu code. (This allows us to create multiple menus down the road.)

Add the following contents:

There's a lot going on in these scripts, and we'll explain its functionality as we progress. At its core, the `rmenu` script displays a user-friendly menu.

As one last step to ensure our new `rmenu` command is ready to use, set the user execute bit:

Go ahead and launch the `rmenu` command now. I'm launching mine from a desktop SSH client (Putty) to start, but you can launch from your mobile device, if desired. Also, it does not matter which directory you launch the `rmenu` command from since the `~/bin` directory is part of your `PATH` now.

You should see a menu appear on your screen as shown here:

![rmenu](http://thisdavej.com/wp-content/uploads/2016/12/rmenu1.png)

As a side note (explained in the usage area of the script source code above), you could also create a menu with different contents by creating a file called `menu2.sh` in the same directory as the `rmenu` script. You could then launch this second menu instead of the default menu (`menu1.sh`) like this:

That's some bonus information that might come in handy sometime! Let's get back to our current context.

Let's navigate through the menu together to learn how it works. Our mouse does not work in this context and thus we must rely on our keyboard only.

Press the `down` arrow key to select `Calendar` and then press the `Enter` key to select that option. Bam! You should see a calendar like this:

![rmenu](http://thisdavej.com/wp-content/uploads/2016/12/rmenu2.png)

To "press" the `Ok` button, hit the `Enter` key. This will return you to the main menu.

Next, use the `down` arrow key to navigate down to the `Reboot Pi` option. Hit the `Enter` key to select this option. You should see the following screen:

![rmenu](http://thisdavej.com/wp-content/uploads/2016/12/rmenu3.png)

Use your `left` and `right` arrow keys to select between the "Yes" and "No" options. Hit the `Enter` key to make your selection. You could also press the `Escape` key to return to the main menu.

Back on the main menu, you can hit the `Escape` key to exit the menu, or use your `Tab` key or right arrow key to navigate to the `Cancel` button, and then hit the `Enter` key.

Here's a summary of the keys used for menu navigation:

  * up/down arrow keys: move through the menu items
  * `Enter` key: select a menu item
  * left/right arrow keys (or `Tab` key): Select between different options such as the "Yes" and "No" options

#### Ensure menu command only appears when launched from your mobile device

Our `rmenu` command includes some special sauce that can be used to only display the menu when certain remote hosts connect through SSH. That's explore that functionality now:

For starters, we need to know the host name of our mobile device which is probably not obvious. Go ahead and launch an SSH session into your Pi from your mobile device. From another screen, such as a remote desktop session into your Pi (where the screen is bigger and easier to read), invoke the following command:

This will give you an "arp table" showing the names of the hosts that have recently connected to your Pi. Lo and behold, you should see your mobile device name listed there!

Next, create a file called `rmenu_hosts` in the same directory as your `rmenu` script:

Add your mobile device host name in this file. Here's an example file I created (with dummy host names) which also demonstrates that you can use "#" to comment out host names that should be ignored when the `rmenu` script proccesses the `rmenu_hosts` configuration file:

Save the file. Let's give it a test and confirm that `rmenu` will only conditionally display the menu if certain host connect. Keep in mind that the menu will always be displayed if connections are made from a non-SSH connection such as in a VNC or Remote Desktop session. Invoke the following command from your mobile phone (the "-c" shows the menu "conditionally"):

Sure enough, you should see the menu appear! If you launch an SSH connection through another host such as your laptop and issue the same command, the menu should not appear since only the host name of your mobile device is listed in the `rmenu_hosts` file.

Go ahead and hit the `Escape` key to exit the menu, and type the following to disconnect the SSH session on your mobile device:

#### Update `.profile` so `rmenu` is launched with each SSH connection

After everything is working to your satisfaction, the final step is to add the `rmenu` command to the `.profile` file in your home directory so it is launched every time a user connects through SSH and logs in as the `pi` user. Here's how we do it:

Add the following line at the bottom of this file:

Save the file and close leafpad.

To confirm this works, connect to your Pi from the SSH client running on your mobile device. The menu should appear, and you are in control of your Pi!

We are now equipped and ready to control our Raspbery Pi systems from mobile devices! As a bonus, we also created a menu application to make it even easier to control the Pi, and shut down our Pi safely rather than yanking the power cord and potentially corrupting our microSD card. Feel free to modify the script and add your own menu commands!

Join us next time as we put this menu to use and create a Pandora music player for our Raspberry Pi that includes a handy Web interface we can use from our mobile device!

[Follow @thisDaveJ](https://twitter.com/thisDaveJ) (Dave Johnson) on Twitter to stay up to date with the latest tutorials and tech articles.

#### Additional articles

[Beginner's Guide to Installing Node.js on a Raspberry Pi](http://thisdavej.com/beginners-guide-to-installing-node-js-on-a-raspberry-pi/)  
[Connecting a Raspberry Pi Using an Ethernet Crossover Cable and Internet Connection Sharing](http://thisdavej.com/connecting-a-raspberry-pi-using-an-ethernet-crossover-cable-and-internet-connection-sharing/)  
[Upgrading to more recent versions of Node.js on the Raspberry Pi](http://thisdavej.com/upgrading-to-more-recent-versions-of-node-js-on-the-raspberry-pi/)  
[While I napped, we got a new apt - Debian apt command cheat sheet](http://thisdavej.com/while-i-napped-we-got-a-new-apt-debian-apt-command-cheat-sheet/)
