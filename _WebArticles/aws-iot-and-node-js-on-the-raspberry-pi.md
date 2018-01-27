# AWS IoT and Node.js on the Raspberry Pi

_Captured: 2017-12-05 at 19:03 from [dzone.com](https://dzone.com/articles/aws-iot-and-nodejs-on-the-raspberry-pi?edition=342102&utm_source=Zone%20Newsletter&utm_medium=email&utm_campaign=iot%202017-12-05)_

There are many approaches for installing Node.js on a Raspberry Pi (Google and you'll find lots of guides), presumably because, for a while, there didn't seem to be any official binaries in the official apt repos, so people were building and sharing their own.

I installed a version from somewhere (can't actually remember where, as it was a while back) and it doesn't support ES6 class syntax used by some of the dependent libraries in the AWS IoT SDK:
    
    
    /home/pi/aws-iot-nodejs-pi-lights/node_modules/aws-iot-device-sdk/node_modules/mqtt/node_modules/websocket-stream/server.js:6
    
    
        at Object.<anonymous> (/home/pi/aws-iot-nodejs-pi-lights/node_modules/aws-iot-device-sdk/node_modules/mqtt/node_modules/websocket-stream/index.js:2:14)

The version I currently have installed is:

Since I'm not sure where this version came from originally, (and apt-get upgrade is not finding any updates), I uninstalled:

Then I followed the steps in the AWS IoT SDK guide [here](http://docs.aws.amazon.com/iot/latest/developerguide/iot-device-sdk-node.html) to install using the version provided from Adafruit's repo (official Node.js binaries for ARM are also available from nodejs.org [here](https://nodejs.org/en/download/)).

With the version provided from Adafruit, this gives me v0.12.6 but unfortunately, this still gives the same error with the ES6 class keyword.

Next, let's try the ARM version from nodejs.org. There's step by step instructions showing how to download the TAR and extract and copy to /usr/local/

Now we have:

And now trying to run my AWS IoT Node.js-based app is a success!
