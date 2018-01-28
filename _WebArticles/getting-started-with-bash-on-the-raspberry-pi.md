# Getting Started With Bash On The Raspberry Pi

_Captured: 2017-10-05 at 08:56 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/bash/getting-started-with-bash)_

## So, what is Bash?

Bash is the name of the programming language and "shell" that powers the text interface of your Raspberry Pi. Every time you type a command into the terminal, you're speaking Bash. The humble shell dates back to 1989, and before computers had graphical interfaces it was the only way you could interact with them. It's necessarily very powerful and flexible.

A shell is a command processor which lets you manipulate your computer by typing in commands. Commands are typed after the "prompt" which is a brief snippet of text informing you who and where you are on the system:

![Bash Prompt](https://learn.pimoroni.com/static/repos/learn/bash/bash-prompt.jpg)

> _While the Bash shell is a flexible programming language in its own right, most of its power comes from the collection of applications known as the "GNU Core Utilities". Each of these has a specific role and they can pass messages between each other via Bash._

The "GNU Core Utilities" make up most of what you see and interact with when using the terminal, Bash can't do much without them. You can run these applications on their own, or use Bash to glue them together in elaborate ways and accomplish complex tasks.

For example, you might use `ls` to list the contents of a directory, `mkdir` to make a directory, or `cd` to change the current directory. None of these are bash functions and Bash can't do these things by itself. They are executable files which live in a special locations on your computer, like `/bin` or `/usr/bin` ( where bin stands for "binary" and not trash! ), so that Bash knows to run them when you call them by name.

If you wanted to do something more complicated, you might run `ps x | grep python` to search all running processes for instances of Python. The `|` is a pipe, we'll learn more about it later!

## You know what Bash is, what now?

Knowledge is power! Knowing that you've already been using a programming language you might not have heard of should encourage you to explore it more. This series of tutorials will, hopefully, arm you with the knowledge you'll need.

First, [go and read abut the GNU Core Utilities](https://en.wikipedia.org/wiki/GNU_Core_Utilities). Just knowing the names of various utilities and what they do is helpful- they are all individually very powerful and very useful. The real magic happens when you start to glue them together with Bash; you'll gain a whole new level of control over your Pi and will start to defeat mundane computing tasks with ease!

Many applications exist solely to make Bash better at general purpose scripting and problem solving, try running `sleep 1` for example! Sleep is not the sort of command you're likely to type straight in, but when placed in a Bash script it can be very useful. The same applies to `false` and `true`, you can type these right into your command line.

Bash doesn't deal with trueness or falseness as you might understand it, everything in Bash returns an "exit status." On success the exit status is always 0, and on failure it should be >0\. Because of this, `true` actually exits with a status of 0 and `false` exits with a status of 1, you can see this for yourself:
    
    
    pi@raspberrypi ~ $ true 2>&1; echo $?
    0
    pi@raspberrypi ~ $ false 2>&1; echo $?
    1
    

![Bash True and False](https://learn.pimoroni.com/static/repos/learn/bash/bash-true-false.jpg)

## Hello Bash!

Now you've waded through my waffle, let's start to write some Bash. First off, you'll need a command line at the ready to type everything into. To fire up the command line you need to run the "terminal" application on your Pi, it looks like a black rectangle in the top menu bar. Alternatively you can find it in Menu -> Accessories -> Terminal.

We'll begin with Hello World, the simplest of simple scripts.

First we'll need a file to put our script in, we'll use `nano`, a text editor, to create it like so:
    
    
    nano hello.sh
    

Now type this into it:
    
    
    #!/bin/bash
    echo Hello World
    

And press `crtl+x`, then press `y` to save changes and hit `enter` to confirm the filename.

### Breaking it down...

The funny looking line that comes first, `#!/bin/bash`, is called a hashbang or shebang. Its purpose it to tell Bash exactly how the contents of the script should be interpreted, in this case we're asking that Bash run the script with `/bin/bash` because we're running a Bash script. You could just as easily write in Python and use `!#/usr/bin/python`, but today we're writing in Bash!

The next line is our script is a short and simple one `echo Hello World`. You can type it right into your command line if you want! It's simply passing the words "Hello World" into the `echo` command. Echo is a simple but very useful command that just echoes out whatever you send to it. Technically it echoes stuff out to a place called "stdout" ( Standard Output ), but Bash will normally display things sent here right on your screen so we wont worry about the nitty gritty details just yet.

### Running your new Bash script...

Once it's created you should make it executable, you can use another Bash command to do that but you'll type this one right into your command line:
    
    
    chmod +x hello.sh
    

`chmod` is a very useful utility, you can use it to change the permissions of a file or directory.

Finally, you can run your script. To run an executable file in the current directory you must use:
    
    
    ./hello.sh
    

![Bash Hello World](https://learn.pimoroni.com/static/repos/learn/bash/bash-hello-world.jpg)

> _In Bash the single dot is a shortcut for the current directory, also useful is the double dot .. which is a shortcut for the directory above the current directory._

##  Wrapping Up

Now you should have a basic understanding of what Bash is- a shell and programming language that ties together a whole bunch of useful applications to make a usable computer system. It's like the text equivalent of a desktop GUI. You should have created, set permissions upon and run a Bash "Hello World" script and used some commands you might not have come across.

In the next Bash article we'll be taking a look at some of the core utilities you might find useful on the Raspberry Pi

Need something for this project? You can use the links below to add products to your [Pimoroni Shop](http://shop.pimoroni.com/) basket for easy checkout.

Want to checkout or change something? Click here to [view your cart](http://shop.pimoroni.com/cart).

## Phil Howard

Phil is Pimoroni's software guru, instantly recognisable by his somewhat pirate-themed moustache growing attempts. Usually found buried neck deep in Python libraries, he's also been known to escape on occasion and turn out crazy new products. If you need a helping hand, he's a prolific Twitter user and rampages around the forums like a T-Rex. Ask him if you need help with Pimoroni's software libraries, or Propeller HAT.
