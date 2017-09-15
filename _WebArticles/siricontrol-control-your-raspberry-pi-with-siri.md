# SiriControl: control your Raspberry Pi with Siri

_Captured: 2017-09-03 at 12:50 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/siricontrol-control-raspberry-pi-siri/)_

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/08/SiriControl.jpg)

Siri is an intelligent personal assistant, integrated with Apple devices, and [SiriControl](http://magpi.cc/2t3Bh4v) lets you use Siri with a Raspberry Pi.

From setting reminders to hailing taxis, Siri can do many things to make life easier. However, wouldn't it be awesome if you could control anything with Siri?

SiriControl is a Python framework which provides a simple way of using Siri voice commands to add fantastic voice control to any project. The possibilities for SiriControl are endless, and as no extra hardware is required: you can get started right away.

### STEP-01: How it works

Siri can create Notes by using the command word 'note'. The new Note is then synced with the linked Gmail account. SiriControl fetches the new Note from the Gmail account, and executes the appropriate function from the dynamically loaded modules created by the user. This ingenious hack enables you to add fantastic voice control capabilities to any project, with minimal setup required.

### STEP-02: Configure Gmail

A Gmail account is required for SiriControl. For security reasons, we suggest creating a new Gmail account specifically for SiriControl, as you will have to enter your credentials in a Python script.

Access for less secure apps needs to be enabled for your new account as Google identifies the connection between the Python script and mail servers as less secure. [Click here for more info](http://magpi.cc/2u3gprx).

![SiriControl Less Secure Apps](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/08/SiriControl-Less-Secure-Apps.jpg)

> _IMAP must also be enabled. This is found in the Gmail account settings, as shown in the image (on next page). This is the protocol SiriControl uses to fetch new Notes._

![SiriControl Gmail](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/08/SiriControl_GMAIL.jpg)

> _STEP-03: Prepare your iOS device_

The Notes need to be synced with your Gmail account so that SiriControl can fetch the voice commands that you say, through Siri. So navigate to Settings > Notes > Accounts > Add Account on your iOS device, and add your new Gmail account.

After turning on Notes, ensure that the default account for creating Notes is the new account. Now, if you say to Siri, "Note this is awesome," it should appear under the Notes section, under your Gmail account.

![SiriControl iOS](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/08/Setup-iOS.jpg)

> _STEP-04: Set up SiriControl_

Finally, you will need to clone the SiriControl repository using:

`sudo apt-get update`

`sudo apt-get install git-core`

`git clone https://github.com/theraspberryguy/SiriControl-System`

Edit siricontrol.py and enter your Gmail account credentials. This should be self-explanatory once the script is opened up.  
Next, run siricontrol.py and say to Siri: "Note meaning of life."

You should get the answer. That's it! You have finished the SiriControl setup. Now, let's add your own voice commands.

### STEP-05: Create your own modules

SiriControl uses a modular approach for adding your own commands. Each voice command, along with its action, is separated into different modules, found in the modules folder.

Every module must have the following:

  * moduleName - this is the name of the module, which can be anything you want.
  * commandWords - this array will contain the words which need to be spoken in order to call the execute() function.
  * execute(command) - this function is called when all the words in the commandWords array are spoken. The command parameter is the complete command spoken by the user.

Take a look at the life.py module, which comes with SiriControl, to gain a better understanding of how it works. Also, keep in mind that all modules you create must be stored in the modules directory for SiriControl to load when it starts up. The template Module.py is also included with SiriControl, which can be used as a reference.

### STEP-06: Next steps

Now you know how to create your own voice commands, what next? Well, whether it's as simple as turning on an LED or controlling your TV using infrared signals - with the power of Siri behind it, the possibilities are endless! You could integrate SiriControl into any project. Due to the nature of the hack, you can control your Raspberry Pi from anywhere in the world, as long as you have an internet connection. This opens up many possibilities, including home automation and IoT. Anything is possible.
