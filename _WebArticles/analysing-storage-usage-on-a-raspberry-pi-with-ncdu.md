# Analysing Storage Usage on a Raspberry Pi with Ncdu

_Captured: 2017-11-03 at 20:31 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2017/10/analysing-storage-usage-on-a-raspberry-pi-with-ncdu/?utm_content=buffera4881&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)_

![Analysing Data](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2017/10/data_magnifying_glass-1078x516.jpg)

Sometimes you need to find out what is using the space on your SD card. Raspbian includes a useful tool called Ncdu which can provide a breakdown of the space used by folders from the command line.

The [official Ncdu site](https://dev.yorhel.nl/ncdu) states :

> Ncdu is a disk usage analyzer with an ncurses interface. It is designed to find space hogs on a remote server where you don't have an entire graphical setup available, but it is a useful tool even on regular desktop systems. Ncdu aims to be fast, simple and easy to use, and should be able to run in any minimal POSIX-like environment with ncurses installed.

Ncdu is installed by default on Raspbian but can be installed using the following commands if required :
    
    
    sudo apt-get update
    sudo apt-get install -y ncdu

Running the utility is as easy as typing ncdu in on the command line or in a terminal window :
    
    
    ncdu

This will provide a breakdown of all the folders in the current working directory.

So you can either browse to the directory you are interested in and then run ncdu or you can specify the path at the same time :

For example :
    
    
    ncdu /home/pi

or :
    
    
    ncdu /

It will take longer to analyse more directories so you should target a specific path to limit the amount of file structure it needs to process.

You can use the arrow keys to move through the list of directories and ENTER to drop down into the next level.

Pressing ? should bring up some help but when I tested I needed to do SHIFT-? :

The keys include :

  * ? - Show help + keys + about screen
  * up, down j, k - Cycle through the items
  * right, enter, l - Open selected directory
  * left, <, h - Go to parent directory
  * n - Order by filename (press again for descending order)
  * s - Order by filesize (press again for descending order)
  * C - Order by number of items (press again for descending order)
  * a - Toggle between showing disk usage and showing apparent size.
  * d - Delete the selected file or directory.
  * t - Toggle dirs before files when sorting.
  * g - Toggle between showing percentage, graph, both, or none. Percentage is relative to the size of the current directory, graph is relative to the largest item in the current directory.
  * c - Toggle display of child item counts.e - Show/hide 'hidden' or 'excluded' files and directories. Please note that even though you can't see the hidden files and directories, they are still there and they are still included in the directory sizes. If you suspect that the totals shown at the bottom of the screen are not correct, make sure you haven't enabled this option.
  * i - Show information about the current selected item.
  * r - Refresh/recalculate the current directory.
  * b - Spawn shell in current directory.

The symbols that may be seen next to items are explained on the "Format" tab :

In conclusion this is a really useful command line tool to be aware of and I'm sure it will be useful to Pi users whatever projects they are working on.
