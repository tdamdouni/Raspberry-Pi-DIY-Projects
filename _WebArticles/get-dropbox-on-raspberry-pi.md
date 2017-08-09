# Get Dropbox on Raspberry Pi

_Captured: 2017-05-06 at 16:28 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/dropbox-raspberry-pi/)_

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2016/09/dropboxmain.png)

Dropbox's relationship with Linux has always been slightly weird, and as Raspbian is a version of Linux, that too means it's not so straightforward to get the file-syncing behaviour of Dropbox to work. There are definitely ways around this, though, and with a little bit of hacking and tweaking, we can get automatic uploads (and downloads!) of items to Dropbox. This method was created by [Alex Eames of RasPi.TV](http://raspi.tv/2013/how-to-use-dropbox-with-raspberry-pi) and is perfect for many types of Raspberry Pi project, especially those where you're taking pictures and want to view them remotely or free up some space on the Raspberry Pi after they've been taken.

_The full article can be found in [The MagPi 48](https://www.raspberrypi.org/magpi/issues/48) and was written by [Rob Zwetsloot](https://twitter.com/RobThez/)_

**STEP-01** Get a Dropbox account

If you don't already have one, sign up for a Dropbox account at dropbox.com. It offers a couple of GB for free, but you can pay a small amount a month for a whopping 1TB of space. There are some other cloud services around, such as Google Drive, but they have even less Linux support than Dropbox. As with most cloud storage services, you can view, download, and upload files from the browser. So if you want to download anything to the Raspberry Pi, it can be quick and easy to go through there.

**STEP-02** Get Dropbox uploader

Now we need to grab Dropbox Uploader on the Raspberry Pi. Boot into Raspbian if you're not already using it, and either open a Terminal or SSH into the Raspberry Pi if you prefer. From there, you'll need to download the install files with:

Once that's downloaded, you'll need to move to the folder (cd Dropbox-Uploader) to begin installing. You can start this off with:

It will ask for your API key, which is our cue to move onto to the next step.

**STEP-03** Find your API key

You need to head to the [developers' section of Dropbox](https://www.dropbox.com/developers/apps) so you can create a new app and get a unique API key to use on the Raspberry Pi. Click on Create App to start.

As we're working towards a personal use application, the first option we'll chose is Dropbox API rather than business. The next two options don't really matter: if you want to access full Dropbox, you can, but it may be better for privacy and security reasons if you're just able to use a specific folder on your Dropbox. Finally, name it whatever you want and click Create App.

**STEP-04** Enter your API key

On the settings page for the app you created, there will be an 'App key' field. Note it down or simply copy and paste it in into the Terminal if you're still on your Raspberry Pi. It will then ask for the 'App secret', which is right below the key in your settings page. Click on 'show' and then enter that. It will then ask you to confirm what type of permission you gave it (full or just a folder) and then it will drop a link to put in the browser to confirm everything. Press ENTER to finish the setup and if everything has gone correctly, it will flash up a message to let you know!

![Enter your keys and secrets](https://www.raspberrypi.org/magpi/wp-content/uploads/2016/09/dropbox3.png)

> _Enter your keys and secrets_

**STEP-05** Add a progress bar

Without a progress bar, you won't always know if everything is working. Luckily, you can add one to this project: open up the installed file we just used  
(nano dropbox_uploader.sh) and look for the line that says SHOW_PROGRESSBAR under Default values.

If this line ends with =0, then change the 0 to a 1 and save the file. There are also some other options under Default values (such as the ability to skip existing files), so have a quick look and see if there's anything else you feel confident to change.

**STEP-06** Start uploading!

Now everything should be working and you can start uploading. Everything revolves around the dropbox_uploader file, so stay in the folder or make sure to have your code point towards the folder in the future. The code to upload is something like:

You can use this code in Python 3 by creating an OS call, using something like:

Time to get uploading and experimenting!
