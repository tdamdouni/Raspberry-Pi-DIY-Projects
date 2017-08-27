# No coding required: Node-RED on a Raspberry Pi

_Captured: 2017-08-26 at 16:16 from [opensource.com](https://opensource.com/article/17/7/nodered-raspberrypi-hardware?utm_campaign=intrel)_

![No coding required: Node-RED on a Raspberry Pi](https://opensource.com/sites/default/files/styles/image-full-size/public/lead-images/hardware_hammer_sign.jpg?itok=ezZ2QpJj)

Node-RED is a programming tool that lets you quickly connect hardware devices using a browser-based editor. It comes with a wide range of nodes that can be used to build flows in a drag-and-drop manner, significantly reducing your development time. [Node-RED](https://nodered.org/) is installed with Raspian Jessie for Raspberry Pi, and there is also an option to download Node-RED separately.

To show you how it works, we'll build a simple tool using Node-RED to communicate with a cellular modem connected to a Raspberry Pi. With cellular modems, you can send/receive data from your Raspberry Pi over a cellular network. You can use one of the 3G/4G USB dongles commonly available through cellular network providers, or you can connect a development board with a 3G or 4G wireless modem.

Whether you're connecting with a USB dongle or a development board, the connection interface to the Raspberry Pi is through a USB port. In this tutorial, I'm connecting a [SIM900](http://m2msupport.net/m2msupport/simcom-sim900-gprs-2g-module/) development board to Raspberry Pi through a USB-to-serial converter cable.

![Connecting SIM900 to Raspberry Pi through a USB-to-serial converter cable](https://opensource.com/sites/default/files/u128651/node_red1.png)

> _Connecting SIM900 to Raspberry Pi through a USB-to-serial converter cable_

The first step is to check that the SIM900 development board is connected to the Raspberry Pi.

![Checking that the SIM900 development board is connected](https://opensource.com/sites/default/files/u128651/node_red2a.png)

> _Checking that the SIM900 development board is connected_

The USB-to-serial adapter shows up here as one of the USB devices connected to the Raspberry Pi.

Next, check the USB port number the SIM900 board is connected to.

![Checking the SIM900 board's USB port number](https://opensource.com/sites/default/files/u128651/node_red3a.png)

> _Checking the SIM900 board's USB port number_

In the last line above, you can see that the SIM900 board (connected through the USB-to-serial converter) is connected to **ttyUSB0** on the Raspberry Pi. Now we're ready to start using Node-RED.

Launch Node-RED on the Raspberry Pi.

![​​​​Launching Node-RED in Raspberry Pi](https://opensource.com/sites/default/files/u128651/node_red4a.png)

> _​​​​Launching Node-RED in Raspberry Pi_

Download this [sample flow](http://m2msupport.net/m2msupport/wp-content/themes/admired/Node-RED/modem_commands) and import it into Node-RED. Note that the flow file is a JSON representation of the graphical UI.

The imported flow should look like this in Node-RED:

![The imported flow in Node-RED](https://opensource.com/sites/default/files/u128651/node_red5.png)

> _The imported flow in Node-RED_

Injection nodes set up [AT commands](http://m2msupport.net/m2msupport/software-and-at-commands-for-m2m-modules/) required to query the modem. The **Add Newline** function node appends **\r\n** to the AT commands passed from the injection nodes. Output from **Add Newline** is then wired to the **Serial Out** node, which writes data to the serial port. The AT command response from the modem is read through the **Serial In** node, which outputs the response to the **Debug **window. Make sure the serial port number and port speed are configured in both the **Serial In** and **Serial Out** nodes.

Node-RED is an easy-to-use programming tool that can be used to quickly integrate and test hardware devices. As you can see from this tutorial, connecting and testing a cellular mode with Raspberry Pi using Node-RED required no coding at all.

For more information about Node-RED and other ways it can be used, visit [the project's website](https://nodered.org/).
