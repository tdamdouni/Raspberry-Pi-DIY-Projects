# Getting a Python script to run in the background (as a service) on boot

_Captured: 2017-08-26 at 10:11 from [blog.scphillips.com](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)_

For some of my projects I write a simple service in Python and need it to start running in the background when the Raspberry Pi boots. Different Linux distributions use different ways of starting and stopping services (some now use [Upstart](http://en.wikipedia.org/wiki/Upstart), some [systemd](http://en.wikipedia.org/wiki/Systemd)). I am using the "Wheezy" Debian distribution on my Raspberry Pi, and in this case the proper way to do this is using an "init script". These are stored in the /etc/init.d folder. In there you can find scripts that for instance, start the networking system or a print server. Debian Wheezy uses the old Sys V init system which means that these scripts are run according to symbolic links in the /etc/rc.x directories. The [Debian documentation](http://www.debuntu.org/how-to-managing-services-with-update-rc-d/) explains this.

Anyway, the following init script makes getting a Python script (or e.g. a Perl script) to run when the Raspberry Pi boots fairly painless. Services are supposed to run as "daemons" which is quite complicated in Python and involves forking the process twice and [other](http://stackoverflow.com/questions/1603109/how-to-make-a-python-script-run-like-a-service-or-daemon-in-linux) [nasty bits](http://code.activestate.com/recipes/278731/). Instead we can make use of the handy start-stop-daemon command to run our script in the background and basically deals with everything we need.
    
    
    [ 1](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 2](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 3](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 4](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 5](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 6](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 7](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 8](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [ 9](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [10](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [11](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [12](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [13](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [14](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [15](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [16](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [17](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [18](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [19](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [20](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [21](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [22](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [23](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [24](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [25](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [26](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [27](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [28](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [29](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [30](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [31](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [32](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [33](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [34](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [35](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [36](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [37](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [38](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [39](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [40](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [41](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [42](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [43](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [44](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [45](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [46](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [47](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [48](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [49](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [50](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [51](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [52](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [53](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [54](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [55](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [56](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [57](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [58](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [59](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [60](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [61](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    [62](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)
    
    
    #!/bin/sh
    
    ### BEGIN INIT INFO
    # Provides:          myservice
    # Required-Start:    $remote_fs $syslog
    # Required-Stop:     $remote_fs $syslog
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: Put a short description of the service here
    # Description:       Put a long description of the service here
    ### END INIT INFO
    
    # Change the next 3 lines to suit where you install your script and what you want to call it
    DIR=/usr/local/bin/myservice
    DAEMON=$DIR/myservice.py
    DAEMON_NAME=myservice
    
    # Add any command line options for your daemon here
    DAEMON_OPTS=""
    
    # This next line determines what user the script runs as.
    # Root generally not recommended but necessary if you are using the Raspberry Pi GPIO from Python.
    DAEMON_USER=root
    
    # The process ID of the script when it runs is stored here:
    PIDFILE=/var/run/$DAEMON_NAME.pid
    
    . /lib/lsb/init-functions
    
    do_start () {
        log_daemon_msg "Starting system $DAEMON_NAME daemon"
        start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --chuid $DAEMON_USER --startas $DAEMON -- $DAEMON_OPTS
        log_end_msg $?
    }
    do_stop () {
        log_daemon_msg "Stopping system $DAEMON_NAME daemon"
        start-stop-daemon --stop --pidfile $PIDFILE --retry 10
        log_end_msg $?
    }
    
    case "$1" in
    
        start|stop)
            do_${1}
            ;;
    
        restart|reload|force-reload)
            do_stop
            do_start
            ;;
    
        status)
            status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
            ;;
    
        *)
            echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status}"
            exit 1
            ;;
    
    esac
    exit 0
    

## Changing the init script

Lines 14 and 15 define where to find the Python script. In this case I have said that there is a folder /usr/local/bin/myservice and that the script is called myservice.py inside there. This is so that any additional Python files or other bits that your Python script needs can also be tidily put into that one place (not really how you're supposed to do it, but is easy).

Line 16 defines what we call the service. You should call this script by the same name.

Line 23 sets what user to run the script as. Using root is generally not a good idea but might be necessary if you need to access the GPIO pins (which I do). You might want to change this to the "pi" user for instance.

Line 28 loads a some useful functions from a standard file. We later use the logging functions for instance. We then define functions do_start and do_stop that will be used to start and stop the script.

start-stop-daemon needs to be able to identify the process belonging to a service so that (1) it can see it is there and does not start it again, and (2) it can find it and kill it when requested. In the case of a Python script then process name is "python" so this is not a very useful identifier as there may well be other Python processes running and things would get confusing. Instead we get start-stop-daemon to store the PID (the or process ID) using the --pidfile $PIDFILE --make-pidfile arguments. When told to start the process it looks for the file $PIDFILE which is defined in line 26 to be /var/run/myservice.pid (which on a Raspberry Pi is actually found at /run/myservice.pid thanks to a symbolic link.

Other than that, we use the --background flag of start-stop-daemon to run our script in the background, --chuid to set the user that the script runs as (with --user to look for scripts run by that user when we are trying to determine if it is already running) and --startas to define what we want to run. The options to start-stop-daemon end with the double-hyphen and then we add on $DAEMON_OPTS in case there are any parameters to pass to the daemon itself.

When stopping the daemon the --retry 10 means that first of all a TERM signal is sent to the process and then 10 seconds later it will check if the process is still there and if it is send a KILL signal (which definitely does the job).

## Using the init script

To actually use this script, put your Python script where you want and make sure it is executable (e.g. chmod 755 myservice.py) and also starts with the line that tells the computer to use the Python interpreter (e.g. #!/usr/bin/env python). Edit the init script accordingly. Copy the init script into /etc/init.d using e.g. sudo cp myservice.sh /etc/init.d. Make sure the script is executable (chmod again) and make sure that it has UNIX line-endings (dos2unix).

To make the Raspberry Pi use your init script at the right time, one more step is required: running the command sudo update-rc.d myservice.sh defaults. This command adds in symbolic links to the /etc/rc?.d directories so that the init script is run at the default times. you can see these links if you do ls -l /etc/rc?.d/*myservice.sh

At this point you should be able to start your Python script using the command sudo /etc/init.d/myservice.sh start, check its status with the /etc/init.d/myservice.sh status argument and stop it with sudo /etc/init.d/myservice.sh stop.
