# Create a Web Server in Node without any Code

_Captured: 2017-08-27 at 14:02 from [thisdavej.com](http://thisdavej.com/create-a-web-server-in-node-without-any-code/)_

Welcome back! In a previous tutorial ([Beginners Guide to Installing Node.js on a Raspberry Pi](http://thisdavej.com/beginners-guide-to-installing-node-js-on-a-raspberry-pi/)), we installed Node.js on a Raspberry Pi. We are now ready to continue our LTM (Learning through Making) tutorial series and build a simple web server without any code. While this tutorial is geared toward the RasPi, the instructions can be easily mapped over to other platforms such as Windows, Linux, and OS X. Let's get started!

After powering on the headless Node.js RasPi that you built in the [previous tutorial](http://thisdavej.com/beginners-guide-to-installing-node-js-on-a-raspberry-pi/), log in from a Windows system by launching a Windows _Remote Desktop Connection_. (Hit the Windows key on your keyboard and type _Remote Desktop Connection _to get started.) This method of remote connection works since we installed xrdp as part of the last tutorial. Of course, you can connect the RasPi directly to a monitor/keyboard/mouse or use other remote options such as an X Server.

Next, launch a terminal window so we can install a special Node package to get this web server up and running in no time. We installed Node in our [previous tutorial](http://thisdavej.com/beginners-guide-to-installing-node-js-on-a-raspberry-pi-2) and we consequently have another command available to us called `npm` (Node Package Manager) which interacts with the official Node npm package repository containing hundreds of thousands of Node packages.

At the shell prompt, type the following:

This will install the npm package called [http-server](https://www.npmjs.com/package/http-server) globally so it is available as a command anywhere on the RasPi rather than just in the current directory. The http-server package was created by the amazing [IndexZero](https://www.npmjs.com/~indexzero) (aka Charlie Robbins) who as authored a number of npm packages. Here's a screenshot that describes this package aptly:

![http-server logo](http://thisdavej.com/wp-content/uploads/2016/02/http-server.png)

We're preparing to serve up static files like they were turtles strapped to rockets!

When we opened the terminal window, it dropped us into our home directory on the RasPi. We're now going to change the directory to the _Public_ directory since this will be a convenient place to store and serve up our web files.

Let's go ahead and create a simple HTML file to serve. We'll launch Leafpad, a user friendly RasPi text editor, to get the job done:

We put the "&" at the end of the command so that Leafpad will be launched as a separate task and return us to the shell prompt. Also, we could have used other text editors such as nano, but Leafpad provides a simple, graphical interface which is very intuitive.

Enter the following HTML code in the Leafpad window (or enter your own HTML):

Save your file and close out Leafpad.

Can you feel the excitement? We're going to be launching a web server soon and serving up this file on our network.

Back at the terminal, let's issue a `ls` (list directory contents) command to verify that the index.html file we just created is there (your shell prompt will include the word "Public" in it rather than just "$" as shown in the example below):

Very good - the index.html file is present in the directory. Let's start serving up this file with our web server by issuing the following command:

Upon launching, you will see something like this:

![http-server serving](http://thisdavej.com/wp-content/uploads/2016/02/http-server-serving.png)

How cool is that? One simple command and we are up and running with a web server.

Let's try it out from a browser. Go ahead and launch the web browser included with Raspbian and type in the following URL in the address bar:

It works! This Node http-server package is pure genius. Super simple to use.

![RasPi web browser](http://thisdavej.com/wp-content/uploads/2016/02/webbrowser.png)

We should now be able to go to another machine on our network and invoke the web server on the RasPi. If you are using the default Raspberry Pi hostname (and did not change it through raspi-config), your server name will be "raspberrypi". Enter the following in your browser address bar:

If this does not work, you may need to install Samba as described in my article [here](http://thisdavej.com/solution-for-cant-ping-raspberry-pi-hostname-on-the-network/) or use the IP address of the RasPi to view the web server files from another machine on your network.

You can also serve up the entire directory of files. Let's see this in action.

First create another file called `hello.txt` in the Public directory:

Enter something simple in this file such as "hello world", save it, and close Leafpad.

Next, rename the index.html file so that the web server will no longer find a default document to serve and will serve a listing of the entire directory instead:

Ok, go ahead and launch the Web browser again. You will see something like this:

![Web browser with directory listing](http://thisdavej.com/wp-content/uploads/2016/02/webbrowser2.png)

We're serving up the whole directory! This is typically a security faux pas in the real world, but it can be a great way to serve up an entire directory of files (potentially including subdirectories, etc.) to other machines on your home network.

The http-server package contains several other options as described [here](https://www.npmjs.com/package/http-server). As one last example, we can serve up port 80 instead of the default port 8080.

First, use Ctrl-C in the terminal to stop the web server.

Next, we need to issue this command with elevated privileges using sudo so that we are able to "bind" the web server to port 80.

We can now visit our web server by going to `http://raspberrypi` rather than `http://raspberrypi:8080`

We have a bona fide web server running here serving URLs that look legit too.

How might this simple Node web server be useful? Here are some examples:

  * Serving up files for sharing with other machines on your network.
  * Teaching yourself or others you love about HTML with a real web server to stage and serve up the files
  * Providing a web portal for IoT projects you are hosting on your RasPi.

That's it for now. There will be more fun tutorials on the way!

[Follow](https://twitter.com/thisDaveJ) Dave Johnson on Twitter to stay up to date on the latest tutorials and tech articles.
