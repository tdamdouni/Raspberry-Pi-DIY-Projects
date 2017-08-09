# Getting Started With Raspberry Pi 3 and Node.js

_Captured: 2017-08-08 at 17:33 from [docs.resin.io](https://docs.resin.io/raspberrypi3/nodejs/getting-started/)_

## Introduction 

In this guide we will build a simple Node.js web server project on a Raspberry Pi 3. Along the way you will learn the basics of resin.io. We will walk through getting a Raspberry Pi 3 online and deploying some Node.js code to it.

We will also look into using the built in web terminal to run test commands and debug issues. Once you have a handle on the resin.io deployment workflow, we will introduce you to resin sync and our CLI which will allow you to increase your development speed on resin.io.

## What You Will Need 

![](https://docs.resin.io/img/raspberrypi/raspberrypi.jpg)

  * A [Raspberry Pi 3 model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/). See our [supported devices list](https://docs.resin.io/hardware/devices/) for other boards.
  * A 4GB or larger microSD card. The [speed class](https://en.wikipedia.org/wiki/Secure_Digital#Speed_class_rating) of the card also matters - class 10 card or above is the way to go.
  * **[Optional]** An ethernet cable
  * A micro USB cable.
  * **[Optional]** A [2A USB micro power supply](https://www.raspberrypi.org/products/universal-power-supply/).
  * A [resin.io account](https://dashboard.resin.io/signup).

## Getting Help 

Before we get started building something cool, lets just point out some places to get help. If at anytime while using resin.io you find yourself stuck, confused or alone remember that there is a team of helpful and friendly support engineers just one click away.

The best place to chat with us is in the [resin.io forums](https://forums.resin.io). Post your questions to the [Troubleshooting section](https://forums.resin.io/c/troubleshooting), where our engineers can help address any issues you may be having with resin.io.

We also love to meet users in our community chat at [gitter.im](https://gitter.im/resin-io/chat).

Read more about our approach to support at resin.io/support(<https://resin.io/support>).

To help us understand all the moving parts in resin.io, lets first define a few terms that will be used later in the guide.

  * **Application:**

> This is a group of devices or "fleet" that will all run the same application code. When you provision a device, it will automatically be associated to the application. You can add as many devices to an application as you like, its also possible to migrate devices to other applications.

  * **resin remote:**

> A remote [git repository](https://www.sbf5.com/~cduan/technical/git/git-1.shtml) that is associated to your application. Any code pushed to the `master` branch of this repo will be built and deployed as a container on all devices in the application. This git repo uses SSH keys to secure it, so don't forget to set up your SSH key.

  * **Container:**

> A [Docker container](https://docs.docker.com/engine/understanding-docker/#how-does-a-container-work) that essentially is a bundle of your application code and all its dependencies. It runs as an isolated process in userspace on the resinOS host.

## Let's Jump In 

If you don't already have a resin.io account head over to our [signup page](https://dashboard.resin.io/signup), during the sign up process you will be asked to set up an SSH key so you can securely push code.

### Adding an SSH Key 

SSH keys use the power of [public-key cryptography](http://en.wikipedia.org/wiki/Public-key_cryptography) to secure your connection when sending your code to us. In order to secure your [git](http://git-scm.com/) connection, you need to add your **public** [SSH Key](http://en.wikipedia.org/wiki/Secure_Shell) (you should never share your _private_ key with anyone.)

![](https://docs.resin.io/img/common/sign_up_flow/enter_ssh_key_cropped.png)

Simply paste your **public** key into the box provided on the UI and click `save`. Alternatively you can import your key from [Github](http://github.com/), just click on the Octocat icon.

#### Don't have a SSH key? 

If you don't have an ssh key or have never used one, we recommend you take a look at [Github](http://github.com/)'s [excellent documentation](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) on the subject and how to generate a key pair for your OS.

Once generated, SSH keys are easy to use. In fact you generally don't have to think about it at all. Once you're set up just `git push` your code to resin.io and it's taken care of automatically and securely.

#### Import SSH key From GitHub 

For convenience we provide the ability to import your public SSH key from [GitHub](http://github.com/) \- just click on the Octocat icon in the bottom right-hand corner ([we use](http://resin.io/blog/email-github-public-ssh-key/) GitHub's [public APIs](https://developer.github.com/v3/) to retrieve this data.)

You will then have to enter your github username into the prompt:

![](https://docs.resin.io/img/common/sign_up_flow/enter_github_username_cropped.png)

If you don't have a ssh key setup yet, but want to explore resin.io, just click `skip`. Note that you will not be able to push code to your Raspberry Pi 3 until you have a ssh key saved. This can be done at anytime from the `[Preferences`](https://dashboard.resin.io/preferences?tab=sshkeys) page on the dashboard.

## Creating an Application 

To create an application simply type in a name, select the Raspberry Pi 3 type from the drop down list and click the create button. You should now be taken to the dashboard of your newly created application:

![](https://docs.resin.io/img/common/main_dashboard/select_fleet_type.png)

This dashboard may not look like much right now, but this is where you will command and manage a whole fleet of Raspberry Pi 3s.

## Adding Your First Device 

This is the application dashboard where all of the devices connected to your application will be shown, along with their statuses and logs.

![](https://docs.resin.io/img/common/app/app_dashboard_empty.png)

Click the `Download resinOS` button to get the resin.io operating system (resinOS) image for your application. A list of available versions is available via the dropdown. In general, the most recent version is recommend.

**Warning:** Versions ending in .dev are for development purposes only, and should not be used in production. More details on the differences between dev and prod images can be found [here](https://docs.resin.io/understanding/understanding-devices/2.0.0/).

**Note:** The `.img` may seem large, but your browser will download a compressed version and decompress it on the fly using [http compression](https://en.wikipedia.org/wiki/HTTP_compression), so the download will be much, much faster than you expect!

Before your resinOS download begins, a prompt will appear asking you to specify how your device will connect to the internet. Currently there are two connectivity options:

  * Ethernet cable, this option requires _NO_ configuration as is the default.
  * Wifi, in which case you must specify the [network name or`SSID`](https://en.wikipedia.org/wiki/Service_set_\(802.11_network\)#Service_set_identification_.28SSID.29) and `passphrase` for the network your device will connect to.

Once you have selected your connectivity option, click the `Download Device OS` button to get the resin.io operating system image configured for your application and network.

![](https://docs.resin.io/img/common/network/network_selection_wifi_cropped.png)

When the download completes you should have a `.img` file with a name like `resin-myFleet-1.1.1-1.7.0-dc6c40fe05aa.img` where "myFleet" is the name you gave your application on the dashboard.

### Create a Bootable SD card 

Now we have to flash the downloaded `.img` file onto our SD card. We recommend using [Etcher](https://etcher.io/), a simple, cross platform SD card writer and validator. Head over to the [Etcher homepage](https://etcher.io/) and get install it, it only takes a few seconds :)

You can of course use any other SD card writing software you like, some options are:

  * [win32diskimager](http://sourceforge.net/projects/win32diskimager/) for Windows.
  * [piFiller](http://ivanx.com/raspberrypi/) for osx.
  * [dd or "Disk Destroyer"](http://man7.org/linux/man-pages/man1/dd.1.html) for Linux.

**Note:** Before you flash resinOS to your SD card you may need to formatted it as [FAT32](http://en.wikipedia.org/wiki/Fat32#FAT32). [WikiHow](http://www.wikihow.com/Main-Page) has great [instructions](http://www.wikihow.com/Format-an-SD-Card) on how to do this.

For simplicity this tutorial will assume you are using [Etcher](https://etcher.io/). Once you have Etcher installed, start it up. You may be asked to allow Etcher administrative privileges. This is just so Etcher can access your SD card.

To create a bootable resinOS SD card follow these 3 easy steps:

  1. Click "Select image" button and find your applications resinOS `.img` file.
  2. If you haven't already done so, insert your SD card into your computer. Etcher will automatically detect it. If you have more than one SD card inserted, you will need to select the appropriate one.
  3. Click the "Flash!" button.
![](https://docs.resin.io/img/common/etcher/etcher.gif)

Etcher will now prepare a bootable SD card and validate that it was flashed correctly. Right! time for a spot of tea as flashing the SD card can take roughly 3 or more minutes depending on the quality of your SD card.

Etcher will give you a little ping! when it's done, and safely eject the SD card for you.

**Note:** You can burn several SD cards with the same `.img` file and all the devices will boot and provision into your application's fleet. You can also disable the auto-ejecting or write validation steps from the Etcher settings panel.

## Setting Up Your Device 

Insert the SD card into the Raspberry Pi 3 and connect the ethernet cable if necessary. Now power up the Raspberry Pi 3 by inserting the micro USB cable.

![insert SD](https://docs.resin.io/img/gifs/insert-sd.gif)

It will take a minute or two for the Raspberry Pi 3 to appear on your [resin.io dashboard](https://dashboard.resin.io/). While you wait the resinOS is expanding the partitions on your SD card to use all available space, installing a custom linux environment and establishing a secure connection with our servers.

You should now be ready to deploy some code!

##### Help! My device won't show up. 

If your device still hasn't shown up on your dashboard after 10 minutes, something is definitely wrong. First check that you entered the wifi credentials correctly and ensure that your network meets these [basic requirements](https://docs.resin.io/deployment/network/). It may also be worth checking the [LED error notifications](https://docs.resin.io/troubleshooting/error)

If you still can't get your device online, come on over and chat to us on our [support channel](https://docs.resin.io/support/).

## Deploying Code 

Now that we have a device or two connected to a resin.io application, lets deploy some code and actually start building something.

A nice first project to get your feet wet is a simple [Express.js](http://expressjs.com/) web server which will serve a static page on port `:80`. All the project source code can be found [here on github](https://github.com/resin-io-projects/simple-server-node).

To clone the project, run the following command in a terminal or your preferred git client:
    
    
    $ git clone https://github.com/resin-io-projects/simple-server-node.git
    

Once the repo is cloned, change directory into the newly created `simple-server-node` directory and add the resin git remote endpoint by running the command `git remote add` shown in the top-right corner of your application page:
    
    
    $ cd simple-server-node
    $ git remote add resin <USERNAME>@git.resin.io:<USERNAME>/<APPNAME>.git
    

So now we have set up a reference in our local git repository (the one on our development computer) to the resin.io application remote repository. So when we push new changes to this remote repository it will get compiled and built on our servers and deployed to every device in the application fleet.

Now to deploy this code to all device(s) in the application just run the command:
    
    
    $ git push resin master
    

If you want to completely replace the source code of the application with a new source tree, you may need to force the push by running `git push resin master --force`, due to how git works.

You'll know your code has been successfully compiled and built when our friendly unicorn mascot appears in your terminal:

![](https://docs.resin.io/img/common/pushing/success_unicorn_simple_nodejs.png)

This means your code is safely built and stored on our image registry. It should only take about 2 minutes to build your code and subsequent builds will be quicker because of build caching.

Your application will now be downloaded and executed by all the devices you have connected in your application fleet. You may have to wait about 6 minutes for the first push... So time for more tea, but don't worry, all subsequent pushes are much, much faster due to [Docker layer sharing](https://docs.docker.com/engine/userguide/storagedriver/imagesandcontainers/). You can see the progress of the device code updates on the device dashboard:

![](https://docs.resin.io/img/common/device/device_dashboard_during_update_generic.png)

You should now have a node.js web server running on your device and see some logs on your dashboard. If you go to the `Actions` page for your device, you can enable a public URL, this URL is accessible from anywhere in the world.

![](https://docs.resin.io/img/common/enable-public-URLs.png)

If you follow the URL, you will be served a page saying "Hello, World!". Alternatively you can point your browser to your devices IP address.

You should now have a basic idea of how to deploy a node.js application on resin.io. If you feel like you have a handle on docker and Node.js projects, then skip over the next section and go straight to "[Using the web terminal"](https://docs.resin.io/raspberrypi3/nodejs/getting-started/).

#### Let's dive into the code 

So in the root directory of our project we see a number of files, the most important ones to focus on are:-

  * `Dockerfile.template` : This is basically a recipe file on how to build and run our application container.
  * `package.json` : This is a [JSON](http://www.json.org/) file that describes how our node.js project is built, what dependencies it has and it's entry point. Read more about it on the [npm docs](https://docs.npmjs.com/files/package.json).
  * `server.js` : This is the entry point to our application code and is where all the fun happens!

The most important part of a resin.io project repo is usually the `Dockerfile` or `Dockerfile.template`. The `.template` version allows you to define template variables like `%%RESIN_MACHINE_NAME%%` which enables you to push the same repository to multiple different architecture fleets.

If we look at our `Dockerfile.template`, the first thing we see is:
    
    
    FROM resin/%%RESIN_MACHINE_NAME%%-node:slim
    

This line has quite a bit packed into it. The first thing that happens is that the `%%RESIN_MACHINE_NAME%%` place holder gets stripped and replaced with the resin device name. For example if your application type is a Raspberry Pi 3, the line will be replaced with:
    
    
    FROM resin/raspberrypi3-node:slim
    

Which tells the resin builder that this is the docker image we want as our base. Checkout the full [list of official resin device names](https://docs.resin.io/devicetypes/) and the [matching dockerhub base images](https://hub.docker.com/u/resin/).

We also have a `:slim` tag associated to the base image which denotes that we want the stripped down version only contains the minimal packages needed to run node, so no `[node-gyp`](https://github.com/nodejs/node-gyp) and other build-essentials. If you need to build some native modules, say node-i2c, you should switch to `:latest` tag. We also have a number of pinned version tags, which should be used for production devices. Checkout the full [list of -node tags](https://hub.docker.com/r/resin/raspberrypi3-node/tags/), if you want to target a specify node.js version or a fixed date build.

Next up we have 3 line which were commented out:
    
    
    RUN apt-get update && apt-get install -yq \
       alsa-utils libasound2-dev && \
       apt-get clean && rm -rf /var/lib/apt/lists/*
    

This is just a demonstration of how you can use `apt-get` to install dependencies in your container. In this case we would install some useful linux sound utilities.

The next two directives are pretty straight forward and key parts of using docker.
    
    
    # Defines our working directory in container
    WORKDIR /usr/src/app
    
    # Copies the package.json first for better cache on later pushes
    COPY package.json package.json
    

As the comments say, `WORKDIR` set our working directory for any `RUN`, `COPY` or `CMD` commands following it. So the next line would effectively `COPY` our `package.json` in the root of our directory to `usr/src/app/package.json`. Check out the [Docker reference](https://docs.docker.com/engine/reference/builder/) pages for more info on these commands.

We can now build all our node.js modules and dependencies, this is done using the `RUN` command. We also build with the `\--production` flag and clear the cache in the same step in order to keep the final image size smaller.
    
    
    # This install npm dependencies on the resin.io build server,
    # making sure to clean up the artifacts it creates in order to reduce the image size.
    RUN JOBS=MAX npm install --production --unsafe-perm && npm cache clean && rm -rf /tmp/*
    
    # This will copy all files in our root to the working  directory in the container
    COPY . ./
    
    # Enable systemd init system in container
    ENV INITSYSTEM on
    
    # server.js will run when container starts up on the device
    CMD ["npm", "start"]
    

After the `npm install` we copy the rest of our source code into the working directory, we do this after so that later builds can benefit from build caching. So we will only trigger a full npm install if we change something in `package.json`.

The last 2 commands are runtime directives. The `ENV INITSYSTEM on` is used to enable the [systemd](https://en.wikipedia.org/wiki/Systemd) init within the container. This is useful for a number of reasons, like keeping the container open after application crash and handling `/dev` updates as new USB devices are plugged in. If you don't want an init system, just set it to `off` or remove the line for the `Dockerfile`.

The last command, `CMD` is perhaps one of the most important. This command defines what will run at container start on your Raspberry Pi 3, in our example we have told npm to start a process. It should be noted that you can only have **one** `CMD` per `Dockerfile`.

In our `package.json` the parts to focus on are our "scripts" and "dependencies":
    
    
    {
      "name": "simple-server-node",
      "version": "1.0.0",
      "description": "A simple Expressjs Web server on resin.io",
      "main": "server.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "node server.js"
      },
      "dependencies": {
        "express": "*"
      }
    }
    

The "dependencies" section allows us to define node modules and their versions we want to use in our application. For a production application we recommend pinning the versions.

The "scripts" allow us to point to the `server.js` as our starting point for the whole application, so we get our awesome "Hello, World!" server when the container starts up :)

## Using the Web Terminal 

Often while developing and deploying code, it helps to run a few test commands or check some log files. For this resin has a handy built in web terminal which you can use from the comfort of your dashboard, or command line (check the later section on CLI and resin sync for this).

To fire up a terminal session on your device you need to two things:

  1. An online device.
  2. A running container.

Number `.1` is usually pretty easy, but number `.2` catches people pretty often. Since if the main process of the docker container crashes or ends, the container effectively stops and there is nothing for the web terminal to SSH into `:(` . For this reason we normally recommend using the systemd init system during development as this will ensure your container is always up and running, even if your application code crashes.

![](https://docs.resin.io/img/common/webterminal/terminal-raspberrypi3.png)

To start a session, just navigate to the `>_ Terminal` page for the device and hit the "Start the terminal session" button. It will take a few seconds to establish a connection and then you are good to go.

## Using Resin Sync to Develop Fast 

Okay, so now we know how to provision a device and push code. There is just one glaring problem...

> Do I really have to go through the whole `git add`, `git commit`, `git push` dance every time I forget a semicolon?

Luckily, our nifty little command line tool `resin sync` is here to save the day. It allows you to quickly sync source code and file changes across to one of the devices in your fleet, so you can rapidly iterate code on this test device before releasing it to the whole fleet.

#### Setting up resin sync. 

Resin sync is bundled in with our handy resin CLI. The CLI allows you to basically do all your resin.io management from the comfort of the command line. Read the [CLI reference](https://docs.resin.io/tools/cli/) more info on all the cool things it can do.

To install resin CLI and sync you need at least `[node.js 4.0.0`](https://nodejs.org/en/) on your development machine, then run:
    
    
    $ npm install --global --production resin-cli
    

You may need to run the install with admin privileges depending on how you have installed node.js.

Once the CLI is installed globally, login with your resin account:
    
    
    $ resin login
    

You should then be presented with 3 options to login. The recommended method is `Web authorisation` which will open a dialog in your web browser and ask you to authorise the use of the CLI.
    
    
    resin:simple-server-node shaun$ resin login
    ______          _         _
    | ___ \        (_)       (_)
    | |_/ /___  ___ _ _ __    _  ___
    |    // _ \/ __| | '_ \  | |/ _ \
    | |\ \  __/\__ \ | | | |_| | (_) |
    \_| \_\___||___/_|_| |_(_)_|\___/
    
    Logging in to resin.io
    ? How would you like to login? (Use arrow keys)
    ❯ Web authorisation (recommended)
      Credentials
      Authentication token
      I don't have a Resin account!
    

#### Setting up Node.js cross-compilation 

Cross-compilation is not needed when using `resin sync` and Node.js as it is an interpreted language. Interpreted languages are programming languages in which programs may be run from source code form, they do not need to be compiled.

#### Using resin sync 

You are now ready to start using `resin sync`, so open a terminal in the directory which we were using earlier in this guide. Make a trivial change to your source code and then run:
    
    
    $ resin sync --source . --destination /usr/src/app
    

It should prompt you to select a device, then it will sync all the files in the root of your directory to `/usr/src/app` on your selected device and finally it will restart the container. You should see something similar to:
    
    
    resin:simple-server-node shaun$ resin sync --source . --destination /usr/src/app
    Getting information for device: 5dc2c87ea2caf79bc4e25ae638c6d5a35a75cecf22e8f914331dcb2f588f4b
    Application container stopped.
    Synced /usr/src/app on 5dc2c87.
    Application container started.
    
    resin sync completed successfully!
    

Your new code changes should be up an running in under 30 seconds, **Great success!!**

##### Some Notes and Caveats on Resin Sync 

  * Resin sync directly syncs all the files in the root of your directory to the selected destination directory on your device. If you are using a compiled language you will need to set up cross-compiling on your local development machine and include a `.resin-sync.yml` file that tells `resin sync` how to compile your code and sync the resulting executable.

  * It is not possible(~easy) to install dependencies using resin sync. So if you need to do an `apt-get` or add something to either your `Dockerfile`, `package.json` or `requirements.txt`, then you will need to go through the standard `git push resin master` build pipeline.

  * If you know the device UUID you can just run: `resin sync <uuid>`. This is useful for using resin sync programmatically, in say a [gulp](http://gulpjs.com/) workflow, as it does not require interactive action to confirm the destination device.

  * If no `\--destination / -d` option is set, an interactive dialog will ask you to provide a destination directory. You can skip this by hitting 'enter' and `resin sync` will use the `/usr/src/app` device directory as the default sync destination.

  * After every `resin sync` the updated settings are saved in `.resin-sync.yml` in your projects's local directory and will be used in later invocations. You can also change any option by editing '.resin-sync.yml' directly.

  * A caveat, if you are using a DSA key, some newer openSSH clients do not allow them by default. So you may have to add the following option to `~/.ssh/config` : `PubkeyAcceptedKeyTypes=+ssh-dss`

  * Resin sync is currently permitted to device owners only. The owner of a device is the user who provisioned it, so you will not be able to use resin sync on devices of shared applications that you did not provision.

One of the many useful features of [resin-cli](https://docs.resin.io/tools/cli/) is `resin ssh`, this command allows you to quickly SSH into a device's running container and run test commands or pull out some logs.

Provided you are already logged in on the CLI and you have a device online, you can use `resin ssh <uuid>` to access the container. Here is an example:
    
    
    resin:simple-server-node shaun$ resin ssh 5dc2c87
    Connecting with: 5dc2c87
    root@raspberrypi3-5dc2c8:/# uname -a
    Linux Raspberry Pi 3-5dc2c8 3.10.93 #1 SMP PREEMPT Wed Apr 20 10:25:12 CEST 2016 armv7l GNU/Linux
    

## Example Projects to Build From 

There are even more hidden treasures in the resin.io platform and tools, but we will get into those a bit later. For now why not fork one or two of our example projects and build something grand.

### Basic GPIO Control in Node.js 

This sample project will get you started blinking LEDs on the Raspberry Pi 3 using only javascript. For this project you will need some additional hardware, namely a basic LED, a breadboard and a 220 ohm resistor.

### Audio stock ticker in Node.js 

The audio stock ticker will verbally announce a list of your favourite stocks every couple of minutes or hours, depending on how you configure it. For this project you will need some head phones or speakers to connect to the Raspberry Pi 3's audio jack.

### Servo motor control in Node.js 

A simple application to issue commands to a servo motor using pi-blaster.

Send SMSes with Twilio and convert them to speech on your Raspberry Pi. For this project you will need some head phones or speakers to connect to the 's audio jack.

### I2C proximity sensor 

This is a simple node.js project that uses [i2c-bus](https://www.npmjs.com/package/i2c-bus) to get data from a [VLNC4000 proximity & light sensor](https://www.adafruit.com/products/466). It is made to be generic and act as base for any i2c sensor integration. It should work on any of the resin.io supported devices, you just need to make sure i2c is enabled in the kernel and know the i2c bus number for you device.

### RPI camera module example in Node.js 

**Enjoy Resinifying All the Things!**

![](https://docs.resin.io/img/common/resinify.jpg)
