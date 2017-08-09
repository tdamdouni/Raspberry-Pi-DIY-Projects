# Python Can

_Captured: 2017-05-11 at 22:06 from [www.janssuuh.nl](http://www.janssuuh.nl/de/2016/03/18/python-can/)_

In the post about installing PiCan I described how you could use the tooling for CAN message receiving / sending.  
However these are rather hard to understand .C scripts, which I had some trouble with to customize.

For this reason I chose to install the Hard byte-Python Can software on my Raspberry Pi. Python is a fairly easy programming language, and has no need to compile the code. Also Python is being used as default programming language for Kodi plug-ins. Both of these components are very useful to serve as interface between my Audi / Rns-e and my Raspberry Pi.

To install the Pycan library, you can run the following command;

[PIP install python-can]

In the AudiRns FULL Beta plugin I have processed all of the default settings.

Do you want to set the correct settings (for example to use when the example plugins), then open;  
[Nano/etc/can.conf]  
and put the following content to the file;  
can.rc['interface'] = 'socketcan_ctypes'  
can.rc['channel'] = 'can0'
