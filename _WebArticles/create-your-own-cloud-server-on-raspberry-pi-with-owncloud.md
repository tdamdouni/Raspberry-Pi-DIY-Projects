# Create your own Cloud server on Raspberry Pi with OwnCloud

_Captured: 2017-08-08 at 17:51 from [www.stewright.me](https://www.stewright.me/2017/08/create-cloud-server-raspberry-pi-owncloud/)_

OwnCloud is an all-in-one solution for creating cloud storage, calendar and contacts servers. OwnCloud allows you to share files through an easy-to-use web interface, similar to OneDrive from Microsoft and Google Drive.

To make our OwnCloud installation even more robust, we're going to use a RAID volume for our storage. I'm going to assume you've followed my previous tutorial '[Create a RAID Volume on Raspberry Pi](https://www.stewright.me/2017/08/create-raid-volume-raspberry-pi/)' first, although this is not necessary.

## Why use a Raspberry Pi for OwnCloud?

Nowadays, home connections are quick enough thanks to fibre and advances and speed gains in ADSL. Raspberry Pi's are cheap, use little power and are quick enough to run the required web server needed for OwnCloud.

I'm using two USB Flash drives in an RAID-1 volume configuration ([see RAID tutorial](https://www.stewright.me/2017/08/create-raid-volume-raspberry-pi/)) and have my Raspbian OS booting from another USB Flash Drive ([see tutorial on booting from USB](https://www.stewright.me/2017/06/install-raspbian-usb-flash-drive-macos-linux/)) so there is a little bottlenecking on the USB bus, but for general usage, it's not a concern as the speed gains from running the OS from a USB and having 2 other devices is still quicker than a MicroSD card.

TL;DR it's a cheap way of creating cloud storage with your Raspberry Pi, and they're more than quick enough for the task.

## Step 1 - Installing the web server

We're going to need to install a web server in order to run OwnCloud. I'm going to install Nginx, PHP7 and MySQL server for this. First, we need to install some updates and upgrades to make sure we're good to go:
    
    
    sudo apt-get update -y && sudo apt-get upgrade -y

We need to add some new sources to APT in order to install PHP 7.1. First, we may need to install a couple of packages. Run the following command:
    
    
    sudo apt-get install apt-transport-https lsb-release ca-certificates

Now we need to modify our sources list in order to install Php 7 using APT. Download a security key in order to continue the installation:
    
    
    wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg

Now we need to create a file for our PHP source to reside. Create the file using nano:
    
    
    sudo /etc/apt/sources.list.d/php.list

Add the following to the file:
    
    
    deb https://packages.sury.org/php/ jessie main

Save and exit by pressing CTRL + C, saving when prompted. Finally, update Apt to register the new sources:
    
    
    sudo apt-get update

There are a few packages we're going to need. Run the following command to install the core files:
    
    
    sudo apt-get install nginx php7.0-fpm php7.0-curl php7.0-xml php7.0-json php7.0-zip php7.0-mb php7.0-mysql php7.0-mcrypt php7.0-gd

Now try visiting the IP address of your Raspberry Pi, you should see the default Nginx default page.

![](https://i2.wp.com/www.stewright.me/wp-content/uploads/2017/08/Screen-Shot-2017-08-06-at-19.40.04.png?w=1440&ssl=1)

## Step 3 - Install MySQL Database Server

The next step will see us install MySQL Database Server. To do this, run the following command:
    
    
    sudo apt-get install mysql-server mysql-client

An interactive prompt will start to create the initial configuration. You will see something like this:

![](https://i2.wp.com/www.stewright.me/wp-content/uploads/2017/08/Screen-Shot-2017-08-06-at-20.13.14.png?w=1336&ssl=1)

Provide a strong password for MySQL server and continue until the installation completes. Next, we need to login to our MySQL server and create a database and user for our OwnCloud installation. Login using the following command:
    
    
    mysql -uroot -p

You will be asked for your root password that you created during the installation. Once you're logged into your local MySQL server, run the following command to create your OwnCloud database:
    
    
    CREATE DATABASE owncloud;

Finally, we create a new user (change the 'a-secure-password' to suit, ensure you don't use your root password and that you make note of it, we'll need it later on):
    
    
    GRANT ALL PRIVILEGES ON owncloud.* TO 'owncloud'@'localhost' IDENTIFIED BY 'a-secure-password';

We're ready to start the installation of OwnCloud. Exit by typing 'quit'.

## Step 3 - Configure Nginx and PHP

First, we need to harden PHP to ensure it stays secure. Edit the configuration file for PHP using this command:
    
    
    sudo nano /etc/php/7.0/fpm/php.ini

Search for '; cgi.fix_pathinfo=1' by pressing CTRL + W, edit this line to look like this by removing the semicolon and space at the start and changing the value to 0:
    
    
    cgi.fix_pathinfo=0

Modify your default site using the following command:

sudo nano /etc/nginx/sites-available/default

Modify the file until it looks like this. The additions are marked in green:
    
    
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
    
        root /var/www/html;
    
        index index.php index.html index.htm;
    
        server_name _;
    
        location / {
            try_files $uri /index.php$is_args$args;
        }
    
        location ~ \.php(/|$) {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/run/php/php7.0-fpm.sock;
            fastcgi_read_timeout 300
        }
    
        location ~ /\.ht {
            deny all;
        }
    }

Save by pressing CTRL + X, saving the changes when prompted. Let's test the configuration using the following command:
    
    
    sudo nginx -t

You should see confirmation of successful configuration. Let's test PHP by creating a new file:
    
    
    sudo nano /var/www/html/index.php

Enter the following into the nano editor:
    
    
    <?php phpinfo();
    
    

Save by pressing CTRL + X once more, saving when asked to. Visit the IP address of your Raspberry Pi once more, you should see the PHP info page:

![](https://i0.wp.com/www.stewright.me/wp-content/uploads/2017/08/Screen-Shot-2017-08-06-at-21.02.57.png?w=1440&ssl=1)

We now need to extend the maximum execution time of PHP-FPM to 300 in order to provide Nginx and PHP enough time to go through the installation process. Edit the FPM configuration with the following command:
    
    
    sudo nano /etc/php/7.0/fpm/pool.d/www.conf

Search for 'request_terminate_timeout' and ensure the line reads like this:
    
    
    request_terminate_timeout = 300

Save using CTRL + X and save when prompted. We're ready to go ahead and install OwnCloud.

## Step 4 - Install OwnCloud

Remove any test or sample files, ensuring we have most definitely changed to the above directory or run the risk of damaging the OS:
    
    
    sudo rm /var/www/html/*

We need to download the setup script:
    
    
    sudo wget https://download.owncloud.com/download/community/setup-owncloud.php

Next, we need to change the owner of the '/var/www/html' folder to 'www-data':
    
    
    sudo chown -R www-data:www-data /var/www/html

Now in the browser, navigate to your Raspberry Pi in the browser, adding '/setup-owncloud.php' to the end. My URL looks like this, change yours to the correct IP:
    
    
    http://192.168.1.118/setup-owncloud.php

You should see the following screen:

![](https://i2.wp.com/www.stewright.me/wp-content/uploads/2017/08/Screen-Shot-2017-08-06-at-21.12.50.png?w=1440&ssl=1)

Follow the installation until you reach the end and the installation has completed. You should now see the following screen which means the installation was completely successful.

![](https://i2.wp.com/www.stewright.me/wp-content/uploads/2017/08/Screen-Shot-2017-08-06-at-21.24.26.png?w=1440&ssl=1)

To begin, provide yourself with an admin username and password. The next stage is very important for configuring the storage. If you followed my previous tutorial on [creating a RAID volume on Raspberry Pi](https://www.stewright.me/2017/08/create-raid-volume-raspberry-pi/), we need to create our data directory. Assuming you did, and your mount point is '/mnt/raid0/', we need to create a directory for our OwnCloud data and set the owner to www-data:
    
    
    sudo mkdir /mnt/raid0/owncloud && sudo chown -R www-data:www-data /mnt/raid0/owncloud/ && sudo chmod -R 755 /mnt/raid0/owncloud/

After this, we enter the following path into the 'data folder' section of the setup page in your browser where you added a username and password earlier:
    
    
    /mnt/raid0/owncloud/

Enter your MySQL details as following:

  * Username: owncloud
  * Password: your chosen password
  * Database: owncloud
  * Server: localhost

Press 'Finish Setup' to complete the installation. That's it. We're good to go. You should now see the login screen when visiting the IP address:

![](https://i0.wp.com/www.stewright.me/wp-content/uploads/2017/08/Screen-Shot-2017-08-06-at-22.15.19.png?w=1440&ssl=1)

## Conclusion

We've hardened our platform by creating a RAID volume, and gone through the steps to install PHP, Nginx and MySQL. We've installed OwnCloud and created a very affordable and robust cloud platform. Please feel free to feedback below or ask any questions.
