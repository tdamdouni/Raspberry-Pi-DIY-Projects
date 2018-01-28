# Add Push Notifications to MotionEye OS

_Captured: 2017-11-19 at 15:33 from [www.raspberrycoulis.co.uk](https://www.raspberrycoulis.co.uk/coding/add-push-notifications-motioneye-os/)_

![Add push notifications to MotionEye OS](https://i1.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/08/cover_image-opt.jpg?w=1600&ssl=1)

MotionEye OS is perfect for using your Raspberry Pi as a CCTV home security system. If you want to know if it detects movement when you're out as part of a home security system, then read on…

## MotionEye OS

For those of you unfamiliar with MotionEye OS, it is a dedicated operating system for CCTV systems created by [Calin Crisan](https://github.com/ccrisan) and distributed free via [GitHub](https://github.com/ccrisan/motioneyeos). It is very quick to set up and is perfect for your Raspberry Pi due to its lower resource requirement. Those of you who read **The MagPi Magazine** may recognise this guide as it was [featured in their Raspberry Pi 3 launch edition in March 2016](https://www.raspberrycoulis.co.uk/hints-tips/i-am-in-magpi-magazine/), after I originally wrote this for [Pi Supply's Maker Zone!](https://www.pi-supply.com/make/adding-push-notifications-motioneyeos-formerly-motionpie/?ref=2&v=79cba1185463) If you want to download the PDF version of the brochure, then you can [check it out here.](https://raspberrypi.org/magpi-issues/MagPi43.pdf)

One benefit of MotionEye OS is its ability to detect motion and capture images and movies of what triggered it. You can even access a live stream of your camera online, even when you're not home, which is handy if you want to check in every now and then. If you're not home, being notified of any movement is very useful and MotionEye OS has a nifty option for custom notifications.

This guide will assume you have already set up and configured MotionEye OS and requires a Pushover licence, which costs $4.99 / £3.99. For help, check out the [MotionEye OS wiki here](https://github.com/ccrisan/motioneyeos/wiki/Installation).

## What You'll Need

  * Raspberry Pi Camera Module (pick from either the older 5MP or the newer 8MP versions):

## Steps

### 1\. Create an Application in Pushover

Pushover has a great, easy to use API and before we start we need to register an application with them. To do this, go click on **"Register Application"** under the **"Your Applications"** heading on their website. Give your app a name - something like **RaspiMotion** - and then make sure the type is **"Application"**. Give your app a quick description (i.e. "Push notifications sent by my Raspberry Pi") and, if feeling creative, upload a custom icon which will show in your Pushover client app whenever a notification is sent.

![Create an app in Pushover](https://i1.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/08/create_an_app.jpg?w=1150&ssl=1)

> _Create an app in Pushover_

### 2\. Get you API Token and User Key

Once you have created your application, you should have access to an **API Token/Key**. This is a combination of numbers and letters - **please keep this a secret!** You'll also need your user key, which is shown once you log in to Pushover's website.

Okay, now you have an app and your API and user keys. You'll now need to download (or recreate if you so wish) a simple Python script to tell your Raspberry Pi to work its magic once the script is called upon by MotionEye OS.

### 3\. Create your Python script

MotionEye OS is not like Raspbian. You cannot use certain commands as you would normally (such as _git clone_), so we'll have to create our Python script manually (or you can drag and drop using WinSCP if preferred). We also do not need to use _sudo _as we're already logged in as root by default. Our script needs to live in the _data_ folder, so let's go there and create _pushover.py_ using Nano:

Then once here, you'll need to copy and paste or type in my code, whilst also including your **API Token** and **User Key** where required.

My code can be found over at my [GitHub repository](https://github.com/raspberrycoulis/pushover), but you can also use the following here:

### 4\. Make your script executable

As with the majority of scripts used on a Raspberry Pi, we need to make sure it can be executed otherwise it is nothing more than a fancy collection of text! You can do this either from the command line, or from within [WinSCP](https://winscp.net/eng/download.php). From the command line, make sure you are in the _data_ folder and then type:

Or using WinSCP, select the _pushover.py_ file in the data folder then press **F9**. In the window that appears, change the permissions to **0755 **and then click "OK" to confirm.

### 5\. Configure MotionEye OS to use your script

Now that we have our script, we need to tell MotionEye OS to use it when it detects motion. To do this, log in and then go to the **"Motion Notifications"** menu and then turn on **"Run A Command"**. You then need to specify which command to run, which will be the Python script you just created. This will be _"/data/pushover.py"_. Click **"Apply"** once done to confirm the changes.

![Motion Notifications](https://i2.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/08/motion_notifications-opt.jpg?w=714&ssl=1)

> _Motion Notifications_

### 6\. Test it out!

Hopefully by now, you have created your Python script, made it executable, told MotionEye OS to use your script when it detects motion and have the Pushover app installed on your smartphone or tablet. We now need to test that it works! Wave your hand in front of your Raspberry Pi Camera (or you can do a dance if you are feeling energetic!) and then shortly afterwards, you should receive a notification via Pushover warning you that motion has been detected!

![Motion Detected!](https://i1.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/08/pushover-opt.png?w=2028&ssl=1)

> _Motion Detected!_

Feel free to experiment with the script to customise the message displayed and sound played in Pushover. Their [API documentation is really simple](https://pushover.net/api) to follow, so be brave and have a play!
