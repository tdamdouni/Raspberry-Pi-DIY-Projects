# Raspberry Pi SSL Certificates using Let’s Encrypt

_Captured: 2017-10-27 at 14:49 from [pimylifeup.com](https://pimylifeup.com/raspberry-pi-ssl-lets-encrypt/)_

![Raspberry Pi SSL with Lets Encrypt](https://cdn.pimylifeup.com/wp-content/uploads/2017/10/lets-encrypt-v1-mini-watermark.jpg)

This Raspberry Pi SSL certificate project will walk you through the steps to installing and setting up the Let's Encrypt Certbot client on the Pi. This Certbot client allows the user to grab a SSL certificate from Let's Encrypt by either utilizing your own web server or by running its own temporary server.

Let's Encrypt is the best way to easily obtain a [secure and certified SSL certificate](https://letsencrypt.org/) for your Raspberry Pi completely free. Before you get started with setting up SSL on your Raspberry Pi, make sure that you have a domain name already set up and pointed at your IP address as an IP Address cannot have a certified SSL Certificate.

![Pi Book Large](https://cdn.pimylifeup.com/wp-content/uploads/2017/04/pi-book-long.jpg)

> _If you are using Cloudflare as your DNS provider, then make sure you have it set to bypass Cloudflare as it hides your IP address meaning the Let's Encrypt tool will fail to verify your Raspberry Pi's IP address and generate it a SSL certificate._

##  Equipment List

Below are all the bits and pieces that I used for setting up Let's Encrypt SSL on my Raspberry Pi, you will need an internet connection to be able to complete this tutorial.

### Recommended:

### Optional:

## Installing and Running Lets Encrypt

**1.** If you are running **Raspbian Stretch or later** you can **skip down to step 5** of this tutorial as the package we be utilizing to setup SSL on our Raspberry Pi is available in the Raspbian Stretch repository.

However, if you are running Raspbian jessie you will have to follow the following four steps to install the SSL client Certbot on your Raspbian Jessie installation. That or you can [upgrade from Raspbian Jessie to Stretch](https://pimylifeup.com/update-raspbian/#jessie) by following our easy guide, and skipping to step 5.

Before we get installing the Let's Encrypt Certbot software on Raspbian Jessie we will first have to adjust our **sources.list** so that we can access the Jessie-Backports branch.

We need to add this as Certbot is not available on Raspbian Jessie by default, be warned though as the backports repository contain software that isn't as thoroughly tested.

Begin editing the sources.list file by using the following command in the terminal:
    
    
    sudo nano /etc/apt/sources.list

**2.** To the bottom of this file, add the following line, this line just tells Raspbian where to go searching for packages.
    
    
    deb http://ftp.debian.org/debian jessie-backports main
    

Once done we can save & exit by pressing **CTRL + X**, then pressing **Y** and then pressing **Enter**.

**3.** Now since our public keys for the new packages are not available by default we will have to grab them and add them to the package manager, we can grab both public keys we need by typing in the following four commands:
    
    
    gpg --keyserver pgpkeys.mit.edu --recv-key  8B48AD6246925553
    gpg -a --export 8B48AD6246925553 | sudo apt-key add -
    gpg --keyserver pgpkeys.mit.edu --recv-key  7638D0442B90D010
    gpg -a --export 7638D0442B90D010 | sudo apt-key add -
    

**4.** With the package now added to our sources list, we will need to run an update to grab the latest package list. We can do that with the following command:
    
    
    sudo apt-get update

**5.** Now that you are up to installing the let's encrypt software onto your Raspberry Pi you will either have to follow the instructions for Raspbian Jessie or Raspbian Stretch.

### Raspbian Stretch and Later

**Apache**
    
    
    sudo apt-get install python-certbot-apache

**Everything Else**
    
    
    sudo apt-get install certbot

### Raspbian Jessie

**Apache**
    
    
    sudo apt-get install python-certbot-apache -t jessie-backports

**Everything Else**
    
    
    sudo apt-get install certbot -t jessie-backports

**6.** With Certbot finally installed we can proceed with grabbing a SSL certificate for our Raspberry Pi from Let's Encrypt. There is a couple of ways of handling this.

If you are not using Apache you can skip this step. If you [are using Apache](https://pimylifeup.com/raspberry-pi-web-server/) then the easiest way of grabbing a certificate is by running the command shown below, this will automatically grab and install the certificate into Apache's configuration.

Before you do that, you will first have to make sure[ **port 80** and **port 443** are **port forwarded**](https://pimylifeup.com/raspberry-pi-port-forwarding/). Also, if you are using Cloudflare as your DNS provider you will need to temporarily bypass it as it hides your real IP address
    
    
    certbot --apache

**7.** If you are not running Apache there is two different ways we can go about grabbing a certificate from Let's Encrypt. Thanks to the certbot software, we can either grab the server using a standalone python server.

Alternatively, if you are running another web server such as NGINX we can also utilize that to grab the certificate as well. Though you will have to setup the certificate manually once it has been grabbed.

Go to step 8a if you are not running another webserver, otherwise go to step 8b.

**8a.** Utilizing the standalone built-in webserver is incredibly easy, though first you will have to make sure your port 80 is unblocked and forwarded. Make sure you replace example.com with the domain name you intend on utilizing.
    
    
    certbot certonly --standalone -d example.com -d www.example.com

**8b.** Using web root requires a bit more knowledge then using the built-in webserver. Make sure /var/www/example points to a working website directory that can be reached from the internet. Also make sure to replace example.com with the domain name you are using for your website.
    
    
    certbot certonly --webroot -w /var/www/example -d example.com -d www.example.com

**9.** After running these commands, you will be prompted to enter some details, such as your email address. This is required for Let's Encrypt to keep track of the certificates it provides and also allow them to contact you if any issues arrive with the certificate.

Once you have filled out the required information it will proceed to grab the certificate from Let's Encrypt.

If you run into any issues make sure you have a valid domain name pointing at your IP, make sure port 80 and port 443 are unblocked, and finally if you are using CloudFlare as your DNS provider, make sure that you have it currently set to bypass its servers.

The certificates that are grabbed by the certbot client will be stored in the following folder. Of course, swapping out example.com with your own domain name.
    
    
    /etc/letsencrypt/live/example.com/

You will find both the fullchain file (fullchain.pem) and the certificate's private key file (privkey.pem) within these folders. Make sure you don't allow others to access these files as they are what keep your SSL connection secure and identify it as a legitimate connection.

With the files now successfully grabbed you can proceed to set up any piece of software you need to use them. For instance, if you [wanted to setup NGINX](https://pimylifeup.com/raspberry-pi-nginx/) to utilize the SSL certificates then follow our Raspberry Pi SSL Nginx guide below.

##  Using your new SSL Certificate with NGINX

**1.** Begin by opening your NGINX configuration file. These are typically stored in /etc/nginx/ or /etc/nginx/sites-available/

Once you have found your configuration file, open it up using your favourite text editor, mine for instance is nano. Once you are within the file search for a text block like what is display below. Make sure you swap out our example.com with the domain name that you are using.
    
    
    server {
            listen 80 default_server;
            listen [::]:80 default_server;
    
            root /usr/share/nginx/html;
            index index.html index.htm;
    
            server_name example.com;
    
            location / {
                    try_files $uri $uri/ =404;
            }
    }

**2.** To this block of code, we will need to make some changes. Follow our steps and read our explanations on why we are making the change below.

**Find**
    
    
    listen [::]:80 default_server

**Add Below**
    
    
    listen 443 ssl;

This change basically tells NGINX to start listening on port 443. Port 443 is important as it is the port that handles HTTPS/SSL traffic, and will be the port web browsers try to connect over when using https://.

**Find**
    
    
    server_name example.com;

**Add Below**
    
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

This change tells NGINX where to find our certificate files. It will use these to setup the SSL/HTTPS connection.

The private key is what secures the actual connection only your server can read and see this file, and this file should be kept secure otherwise people could potentially intercept and decrypt your traffic.

The fullchain contains all the information needed to talk with the server over the HTTPS connection as well as the information needed to verify it is a legitimately signed SSL file.

**3.** With all those changes done, you should end up with something similar to what is displayed below. Of course make sure you replaced example.com with your own domain name.

Once you are satisfied that you have entered the new data correctly. You can save and quit out of the file and then restart NGINX so it loads in the new configuration.
    
    
    server {
            listen 80 default_server;
            listen [::]:80 default_server
    
            listen 443 ssl;
    
            root /usr/share/nginx/html;
            index index.html index.htm;
    
            server_name example.com;
    
            ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
            ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    
            location / {
                    try_files $uri $uri/ =404;
            }
    }

**4.** You should now have a fully operational HTTPS connection for your NGINX web server utilizing the certificate we generated with Let's Encrypt.

You should now hopefully have a fully validated SSL certificate that is provided to you from Let's Encrypt! You will find this tutorial pretty handy across a wide range of projects, especially the [server based Raspberry Pi projects](https://pimylifeup.com/category/projects/server/). Hopefully you have found this Raspberry Pi SSL tutorial helpful, if you have any issues or any feedback feel free to use the comments section below.
