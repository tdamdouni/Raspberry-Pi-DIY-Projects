# http://forums.pimoroni.com/t/use-a-media-keyboard-with-your-phat-beat-can-it-be-done/5176/18

import os
import socket
import re
import sys

VLC_HOST = "127.0.0.1"
VLC_PORT = 9294

class VLC():

    def __init__(self, host="127.0.0.1", port=9294):
        self.host = host
        self.port = port
        self.current_stream = None
        self.current_state = None
        self.connecting = False
        self.socket = None

    def send(self, command):
        if self.connecting:
            return False

        print("Sending command: {}".format(command))
        command_string = command + "\n"

        if sys.version_info[0] >= 3:
            command_string = command_string.encode("utf-8")

        try:
            self.socket.send(command_string)

        except socket.error:
            print("Failed to send command to VLC") 
            if self.connect():
                self.send(command)

    def recv(self, length):
        value = self.socket.recv(8192)

        if sys.version_info[0] >= 3:
            value = value.decode("utf-8")

        return value

    def communicate(self, command, response_length=8192):
        self.send(command)
        return self.recv(response_length)

    def get_current_stream(self):
        self.send("status")
        status = self.recv(8192)

        result = re.search("input:\ (.*)\ ", status)
        state = re.search("state\ (.*)\ ", status)

        if state is not None:
            self.current_state = state.group(1)

        if result is not None:
            self.current_stream = result.group(1)
        else:
            self.current_stream = None

        return self.current_stream

    def connect(self):
        if self.connecting:
            return

        self.connecting = True

        if self.socket is not None:
            self.socket.close()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for attempt in range(10):
            try:
                print("Attempting to connect to VLC on {host}:{port}".format(host=self.host, port=self.port))
                self.socket.connect((self.host, self.port))
                print("Connection successful!")
                self.connecting = False
                return True

            except socket.error:
                time.sleep(1)

        print("Connection failed!")
        self.connecting = False
        return False

vlc = VLC(host=VLC_HOST, port=VLC_PORT)

if vlc.connect():

    import usb.core
    import usb.util
    import time

    USB_VENDOR  = 0x20a0
    USB_PRODUCT = 0x0001

    USB_IF      = 0 # Interface
    USB_TIMEOUT = 5 # Timeout in MS

    BTN_FASTFWD = 181
    BTN_REWIND = 182
    BTN_PLAYPAUSE = 205
    BTN_VOLUP = 233
    BTN_VOLDN = 234
    BTN_ONOFF = 1

    dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)
    endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(USB_IF) is True:
  dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF)

while True:
    control = None
    try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        #print(control)
    except:
        pass

    if control != None:
        if BTN_FASTFWD in control:
           vlc.communicate("next") #  Next track

        if BTN_REWIND in control:
            vlc.communicate("prev") # Prev track

        if BTN_PLAYPAUSE in control:
            vlc.communicate("pause") # Pause/Play

        if BTN_VOLUP in control:
            vlc.communicate("volup") # Turn the volume up one step

        if BTN_VOLDN in control:
            vlc.communicate("voldown") # Turn the volume down one step

        if BTN_ONOFF in control:
            os.system("sudo shutdown now -P")

    time.sleep(0.02)