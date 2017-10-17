# Intall Node.js v4 on your Raspberry Pi

The latest version of Node.js has full support for ARM processors, so it is this lean and simple to install:
If you had nodejs already installed
```
sudo apt-get remove nodejs
Download Node.js source 
```

Raspberry Pi Model A, B, B+ and Compute Module
```
wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv6l.tar.gz 
 tar -xvf node-v4.0.0-linux-armv6l.tar.gz 
 cd node-v4.0.0-linux-armv6l
```

Raspberry Pi 2 Model B
```
wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv7l.tar.gz
 tar -xvf node-v4.0.0-linux-armv7l.tar.gz 
 cd node-v4.0.0-linux-armv7l
```
Copy to /usr/local
```
sudo cp -R * /usr/local/
```

Probably you will have to refresh your ENV variables so simple run: `bash`

And now feel free to check your current running version and write some code!
```
node -v
```