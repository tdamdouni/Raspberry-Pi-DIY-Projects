# Running node.js on a Raspberry Pi Zero

_Captured: 2017-08-13 at 09:23 from [eddielee.me](http://eddielee.me/running-node-js-on-a-raspberry-pi-zero/)_

_This post assumes your Raspberry Pi is already setup and you can SSH into it. If not, have a Google and come back. I'll wait._

The Raspberry Pi Zero (and the original Raspberry Pi) use an ARMv6 CPU. Unfortunately `apt-get install nodejs` installs a version of node built for ARMv7, so we'll have to install it manually.

![](http://eddielee.me/content/images/2017/03/IMG_6828.jpg)

## Download

  * Download the version of node you want, in this case I'm downloading v7.7.2 for ARMv6. Other versions can be found [here](https://nodejs.org/dist/).

`wget https://nodejs.org/dist/v7.7.2/node-v7.7.2-linux-armv6l.tar.gz`

  * Extract the files once the download has completed.

`tar -xzf node-v7.7.2-linux-armv6l.tar.gz`

## Install

  * Copy the files into /user/local

`sudo cp -R node-v7.7.2-linux-armv6l/* /usr/local/`

## Add to path

To use the `node` and `npm` commands you need to add the location we installed node (/user/local/bin) to your path.

  * Open "~/.profile" for editing (I'm using nano)

`nano ~/.profile`

  * Add `PATH=$PATH:/usr/local/bin` at the end then press `ctrl + x` to exit. Type `yes` to save.

## Clean up

We should now remove the downloaded files to keep the file system clean.

  * Remove the tarball

`rm ~/node-v7.7.2-linux-armv6l.tar.gz`

  * Remove the extracted files

`rm -r ~/node-v7.7.2-linux-armv6l`

## Test

  * Check that node is working with `node -v` which will return the installed version, in my case v7.7.2.
  * Check that npm is working with `npm -v` which will return the installed version, in my case v4.1.2.
