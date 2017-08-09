# Writing your own CAN-Bus app in C for Raspberry Pi 2

_Captured: 2017-05-11 at 22:48 from [skpang.co.uk](http://skpang.co.uk/blog/archives/1199)_

This blog will show you how to write a basic CAN-Bus program in C for the Raspberry Pi 2 board.

Before you start make sure the [drivers are installed](http://skpang.co.uk/blog/archives/1165) and working correctly first.

Download the source code and example files by typing the following in the command prompt:
    
    
    wget http://skpang.co.uk/dl/cantest.tar

Unpack the tar file and change into directory by:
    
    
    tar xf cantest.tar 
    
    
    cd linux-can-utils

The example file is called cantest.c to edit this file, type the following in the command prompt:
    
    
    nano cantest.c

Line 77 is the CAN message to be sent out.
    
    
    unsigned char buff[] = "7DF#0201050000000000";

7DF is the message ID and 0201050000000000 is the data. Change the data to suit.

Press CTRL-X to exit.

To compile the program type:
    
    
    make

Check there are no errors. To run the program type:
    
    
    ./cantest
