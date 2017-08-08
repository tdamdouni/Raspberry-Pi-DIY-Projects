# How to Write and Run a C Program on the Raspberry Pi

_Captured: 2016-11-07 at 10:27 from [www.circuitbasics.com](http://www.circuitbasics.com/how-to-write-and-run-a-c-program-on-the-raspberry-pi/)_

In this brief tutorial, I'll discuss what a C program is, what C programming is used for, and finally, how to write and run a C program on the Raspberry Pi.

## What is a C Program?

The C programming language is one of the most widely used programming languages of all time. It is computationally faster and more powerful than Python. C is a middle level programming language because of its low level of abstraction to assembly language. High level languages provide the programmer with _constructs_, or commands that make it easy to do certain tasks like printing to the computer monitor, or logic functions like and, or, and not. Low level programming languages only give you access to the machine's basic instruction set. C does have some of these useful constructs, but not as many as higher level languages like Python.

The advantage of C is that it produces code that is almost as fast computationally as assembly code, it gives you access to powerful low level machine functions, and it has a syntax that is easier to read than assembly code. For example, compare this assembly code for our "hello world" program to the C code for the same program below:

Code written in C will need to be compiled before it can be run on a computer. Compiling is the process of converting human readable code into machine readable code that can be understood by the computer's CPU.

C is so widely used that it can be compiled for almost any system with minimal changes to the source code. The C language is available on a wide range of computer platforms including personal computers, embedded microcontrollers, and supercomputers.

## What can a C program do?

C was initially used to develop operating systems, so it may not surprise to you that the Linux kernel is written in C. C can do pretty much anything you would want to do in computer programming. Some example applications include:

  * Operating systems
  * Large programs
  * Databases
  * Desktop utilities
  * Language compilers
  * Text/photo editors
  * Network drivers

## How to create and run a program in C

The intent of this article is to give a high level view of the main programming languages used on the Raspberry Pi. If you're looking for in depth information on C programming, a great book is the de facto standard, _[The C Programming Language_ by Brian Kernighan and Dennis Ritchie](http://buy.geni.us/Proxy.ashx?TSID=13213&GR_URL=http%3A%2F%2Fwww.amazon.com%2Fgp%2Fproduct%2F0131103628%2Fref%3Das_li_qf_sp_asin_il_tl%3Fie%3DUTF8%26camp%3D1789%26creative%3D9325%26creativeASIN%3D0131103628%26linkCode%3Das2%26tag%3Dcircbasi-20%26linkId%3DNIJRMUE6AS6WZW4V). It's a useful text for anyone currently using C, or anyone that wants to learn it.

The coding process in C consists of four steps:

  1. Writing the code
  2. Compiling the program
  3. Making the program executable
  4. Executing the program

To start, open the nano text editor with a new file by entering sudo nano hello-world.c at the command prompt. When you create the initial uncompiled text file where you will save the C code, it must have a ".c" extension. Now, enter this code into nano:

After entering the code, enter Ctrl-X to save and exit nano.

The next step is to compile the source file hello-world.c. This will make a new file which we can name anything we want, for example myfirstcprogram. At the command prompt, enter gcc hello-world.c -o myfirstcprogram. The -o myfirstcprogram part tells the compiler to take the source file (hello-world.c) and output another file (myfirstcprogram) that we can make executable.

Now, we need to change the file permissions of myfirstcprogram to make it executable. At the command prompt, enter chmod +x myfirstcprogram. The program can now be run by entering ./myfirstcprogram.

Hope this helps you get a basic idea on how to get started programming in C on the Raspberry Pi. If you have any questions, please leave a comment below, and if you know anyone who could enjoy this information, please share it! You can also keep updated on our regularly published tutorials by subscribing via email - just enter an email address in the subscribe field below.
