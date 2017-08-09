# Pairing a BBC micro:bit with a Raspberry Pi using BlueZ

_Captured: 2017-08-08 at 17:32 from [bluetooth-mdw.blogspot.de](http://bluetooth-mdw.blogspot.de/2017/02/pairing-bbc-microbit-with-raspberry-pi.html?m=1)_

A Raspberry Pi 3 has Bluetooth low energy built in and a Raspberry Pi 2 can have a Bluetooth USB dongle plugged into it to give it Bluetooth capabilities. BlueZ, the Bluetooth stack for Linux needs then to be installed. Once done, you have a Bluetooth enabled Raspberry Pi.

But what about your BBC micro:bit? Well, the easiest way to use your Pi with your micro:bit is to install a hex file whose settings do not require it to be paired to another device before it can be used. PXT lets you pick whether or not pairing is required and if so, whether you want to use "passkey pairing", where you enter a 6 digit number displayed by the micro:bit or "just works" pairing, where all you need to do is initiate the pairing process, and the rest happens by magic.

If you opt to use passkey pairing, it's possible to have BlueZ pair your micro:bit with your raspberry Pi. After that, any communication with the micro:bit from the Pi will use that pairing information and where necessary, data will be encrypted.

Here's an example of me pairing my Raspberry Pi with my micro:bit using BlueZ from a Linux terminal session:
    
    
    pi@raspberrypi:~ $ **sudo hciconfig hci0 down** pi@raspberrypi:~ $ **sudo hciconfig hci0 up** pi@raspberrypi:~ $ **sudo bluetoothctl** [NEW] Controller B8:27:EB:C5:E9:31 raspberrypi [default] [NEW] Device D0:F5:DF:C0:AE:95 BBC micro:bit [NEW] Device 90:03:B7:C9:9C:D8 Flower power 9CD8 [bluetooth]# **scan on** Discovery started [CHG] Controller B8:27:EB:C5:E9:31 Discovering: yes [CHG] Device D0:F5:DF:C0:AE:95 RSSI: -61 [CHG] Device D0:F5:DF:C0:AE:95 Name: BBC micro:bit [vuzig] [CHG] Device D0:F5:DF:C0:AE:95 Alias: BBC micro:bit [vuzig] [CHG] Device 90:03:B7:C9:9C:D8 RSSI: -80 [bluetooth]# **paired-devices** Device D0:F5:DF:C0:AE:95 BBC micro:bit [vuzig] [bluetooth]# **remove D0:F5:DF:C0:AE:95** [DEL] Device D0:F5:DF:C0:AE:95 BBC micro:bit [vuzig] Device has been removed [bluetooth]# **agent KeyboardDisplay** Agent registered [NEW] Device D0:F5:DF:C0:AE:95 BBC micro:bit [vuzig] [CHG] Device 90:03:B7:C9:9C:D8 RSSI: -89 [bluetooth]# **pair D0:F5:DF:C0:AE:95** Attempting to pair with D0:F5:DF:C0:AE:95 [CHG] Device D0:F5:DF:C0:AE:95 Connected: yes Request passkey [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: 00001800-0000-1000-8000-00805f9b34fb [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: 00001801-0000-1000-8000-00805f9b34fb [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: 0000180a-0000-1000-8000-00805f9b34fb [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: e95d93af-251d-470a-a062-fa1922dfa9a8 [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: e95d93b0-251d-470a-a062-fa1922dfa9a8 [CHG] Device D0:F5:DF:C0:AE:95 Appearance: 0x0200 [agent] Enter passkey (number in 0-999999): **959145** [CHG] Device D0:F5:DF:C0:AE:95 Paired: yes Pairing successful [CHG] Device D0:F5:DF:C0:AE:95 Connected: no 

I've highlighted the text I entered in red. Initially, I brought the Bluetooth adapter's HCI (Host Controller Interface) down then up. This is a handy way to reset it and in my experience, this is sometimes necessary.

I then put my micro:bit into pairing mode.

Having done so, I launched "bluetoothctl", a utility that lets me enter various commands.

Once started, I ran "scan on" to start BlueZ scanning for other devices, and as you can see, it lists the Bluetooth devices that it finds, including a micro:bit.

I then ran "paired-devices" to see what devices my Pi was already paired with. It listed my micro:bit so to start with I removed that pairing. You should always do this if you've installed a new hex file on the micro:bit since this will have caused any previous pairing information to be lost from the micro:bit and the micro:bit and the device it is paired with must both have the same pairing information.

Then I specified "agent KeyboardDisplay". This tell the BlueZ to inform other devices that it is a device with both a keyboard and a display, during the pairing process. The point here is that during pairing, the two devices exchange information about each other's IO capabilities and this is used to determine what the best way to go about pairing might be. If neither device had a keyboard, for example, there would be no point trying to perform passkey pairing.

After that, I initiate pairing with the MAC address of my micro:bit as an argument. Pairing proceeds and the micro:bit display responds with an arrow on its display, pointing at button A. I pressed button A and was prompted on the Pi to enter the passkey displayed on the micro:bit.

And that's all there is to it. There's even less to do if you load a hex file configured for "just works" pairing.
