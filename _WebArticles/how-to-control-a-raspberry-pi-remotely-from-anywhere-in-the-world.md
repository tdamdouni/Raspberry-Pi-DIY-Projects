# How to Control a Raspberry Pi Remotely From Anywhere In the World

_Captured: 2017-07-30 at 16:04 from [lifehacker.com](http://lifehacker.com/how-to-control-a-raspberry-pi-remotely-from-anywhere-in-1792892937/amp)_

![](https://i.kinja-img.com/gawker-media/image/upload/s--xu4wTt1B--/c_scale,fl_progressive,q_80,w_800/ng1xhuw0kityksytqfjb.png)

> _Illustration by Sam Woolley._

Ever wished you could access your Raspberry Pi when you're on the road? Perhaps you've set up a home security camera, you're running a private Minecraft server, or you're using your Pi for some crazy hacked together internet appliance of your own making. Whatever your reasons, it's easy than you think to access that Raspberry Pi remotely. Here's how.

To access a Raspberry Pi (or any home computer for that matter) from outside your home network, you'd usually need to jump through a lot of hoops, get an IP address, and tweak a few settings on your home router. If you just need to control a few simple things on your Raspberry Pi, that's overkill. We're going to outline two methods that skip all of that.

The first thing you need to do is get your [Raspberry Pi set up and connected to your home network](http://lifehacker.com/the-always-up-to-date-guide-to-setting-up-your-raspberr-1781419054). Since you're exposing your Raspberry Pi to the internet, be sure you[ change your default password](https://www.raspberrypi.org/documentation/linux/usage/users.md) during the set up process. Once that's done, come back here to set up everything else.

### Remote Log Into Your Raspberry Pi's Full Operating System Using VNC Connect

![null](https://i.kinja-img.com/gawker-media/image/upload/s--uvqpxEo9--/xugumrkku9zlkbjfz8aq.jpg)![null](https://i.kinja-img.com/gawker-media/image/upload/s--dozfiK_R--/xugumrkku9zlkbjfz8aq.gif)

VNC has long been the best way to access any[ computer remotely on the same network](http://lifehacker.com/how-to-control-your-raspberry-pi-from-any-computer-usin-1788592777). Recently, [VNC Connect came out to make it easy to access](http://lifehacker.com/you-can-now-easily-connect-to-your-raspberry-pi-from-an-1792438276) your Raspberry Pi from _anywhere _using a cloud connection. Once it's set up, you can access your Raspberry Pi's graphic interface from any other computer or smartphone using the [VNC Viewer app](https://www.realvnc.com/download/viewer/raspberrypi/).

VNC Connect comes packed in for free with the most recent versions of the Raspberry Pi operating system, [PIXEL](http://lifehacker.com/the-new-raspberry-pi-os-is-here-and-it-looks-great-1787194540). If you already have that, you can skip this part. If not, you can install it and turn it on by opening up Terminal on your Raspberry Pi and typing in a few commands:

  1. Type in `sudo apt-get update` and press Enter.
  2. Type in `sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer` and press Enter.
  3. Once that's complete, type in `sudo raspi-config` and press Enter. Scroll down to VNC and set it to Enabled.

Once that's finished downloading, you can set up VNC Connect:

  1. Head to the [RealVNC Raspberry Pi sign up page](https://www.realvnc.com/raspberrypi/#sign-up) and enter your email address in the sign up box.
  2. Follow the on-screen instructions to finish setting up your account with a password.
  3. Back on your Raspberry Pi, click the VNC icon in the top-right corner of the screen to open VNC. Then click the status menu and select Licensing.
  4. Enter the email address and password you created in step one.
  5. When prompted, select "Direct and cloud connectivity." Your Raspberry Pi is now accessible online.
  6. Download the [VNC Viewer application](https://www.realvnc.com/download/viewer/) on the computer you want to control the Raspberry Pi _from_, like the laptop or smartphone you'll have when you travel. 
  7. Open the VNC Viewer application and enter the credentials you created in step one.
  8. Your Raspberry Pi will pop up as an option automatically. Select it to open up the connection. When prompted, enter your Raspberry Pi's username and password (by default this is the username `pi` and password `raspberry`). Within a few second it'll connect.

You're now able to log into your Raspberry Pi's graphic desktop from anywhere as long as your Raspberry Pi has internet access. This means you can take control of any security software, check on the status of any projects you've set up, or [play Minecraft on your private server](http://lifehacker.com/learn-all-kind-of-coding-skills-using-a-raspberry-pi-an-1784535192).

### Access the Command Line with Dataplicity

If you don't need to access the full graphic interface, then you'll want to check out [Dataplicity](https://www.dataplicity.com). Dataplicity makes it incredibly easy to access your Raspberry Pi's command line from any browser. You'll need access to a web browser and your Raspberry Pi for this.

  1. Head to [Dataplicity ](https://www.dataplicity.com)and create an account by entering your email address.
  2. Click Add New Device.
  3. Dataplicity will display a line of code as seen in the image above. Copy that line of code and enter it into the command line of your Raspberry Pi. You can do this on your Raspberry Pi by selecting opening the Terminal application or by accessing it [remotely on your home network over SSH](http://lifehacker.com/how-to-control-your-raspberry-pi-from-any-computer-usin-1788592777) using a tool like [Adafruit's Pi Finder](https://github.com/adafruit/Adafruit-Pi-Finder). After a few seconds, Dataplicity will download and install software on your Raspberry Pi that links it directly with your account.
  4. Once that's complete, head to the [Dataplicity device page](https://www.dataplicity.com/devices/). Here, you'll see your Raspberry Pi. Click on it to open up a Terminal window.
  5. Right now, you can reboot and rename your Raspberry Pi, and that's about it. If you just need to remotely reboot it sometimes, leave it as is. If you need to do more than that, like install software or edit files, you can sign in as a superuser. To do so, in the Dataplicity command line, type in, `su pi` and press Enter. Then, enter your Raspberry Pi's password and press Enter. Now you have total control over your Raspberry Pi. 

That's it, you have complete access to your Raspberry Pi from anywhere in the world with an internet connection. Obviously your Raspberry Pi needs to remain powered on, but otherwise you can access it from any browser. You can do a _ton_ of thing with this little feature out of the box, including: hosting a [small web site](https://docs.dataplicity.com/docs/host-a-website-from-your-pi), [sharing files](https://docs.dataplicity.com/docs/share-files-from-your-pi), and [even streaming video](https://docs.dataplicity.com/docs/stream-live-video-from-your-pi).
