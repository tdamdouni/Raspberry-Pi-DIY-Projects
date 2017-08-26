#!/usr/bin/env python

import atexit
import re
import socket
import subprocess
import time
import signal
from sys import exit, version_info

import phatbeat

class VLC():

    def __init__(self, host="127.0.0.1", port=9294):
        self.host = host
        self.port = port
        self.pid = None
        self.current_stream = None
        self.current_state = None
        self.running = False

    def shutdown(self):
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        import subprocess
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print output

    def kill(self):
        if self.pid is not None and self.running:
            print('Killing VLC process with PID: ' + str(self.pid))
            subprocess.call(['/bin/kill','-9', str(self.pid)])

    def send(self, command):
        print("Sending command: " + command)
        command += "\n"

        if version_info[0] >= 3:
            command = command.encode("utf-8")

        try:
            self.socket.send(command)

        except socket.error:
            print("Failed to send command to VLC")

    def recv(self, length):
        value = self.socket.recv(8192)

        if version_info[0] >= 3:
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
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for attempt in range(10):
            try:
                print("Attempting to connect to VLC")
                self.socket.connect((self.host, self.port))
                print("Connection successful!")
                return True

            except socket.error:
                time.sleep(1)

    def start(self):
        if self.pid is None:
            try:
                return_value = subprocess.check_output(['pidof', 'vlc'])

                if version_info[0] >= 3:
                    self.pid = int(return_value.decode('utf-8').split(' ')[0])
                else:
                    self.pid = int(return_value.decode('utf-8').split(' ')[0])

                print('Found VLC with PID: ' + str(self.pid))

                if self.connect():
                    return True

            except subprocess.CalledProcessError:
                pass

            try:
                return_value = subprocess.check_output(['./vlc.sh'])
                pids = return_value.decode('utf-8').split('\n')[0]
                self.pid = int(pids.split(' ')[0])
                self.started_vlc_instance = True
                print('VLC started with PID: ' + str(self.pid))

            except subprocess.CalledProcessError:
                print('You must have VLC installed to use Dot3k Radio')
                print('Try: sudo apt-get install vlc')
                return False

        if not self.connect():
            print("Unable to connect to VLC")
            return False

        self.running = True

        return True

if __name__ == "__main__":
    vlc = VLC()

    if vlc.start():
        @phatbeat.on(phatbeat.BTN_VOLDN)
        def pb_volume_down(pin):
            print(vlc.communicate("voldown"))

        @phatbeat.on(phatbeat.BTN_VOLUP)
        def pb_volume_up(pin):
            print(vlc.communicate("volup"))

        @phatbeat.on(phatbeat.BTN_PLAYPAUSE)
        def pb_play_pause(pin):
            print(vlc.communicate("pause"))

        @phatbeat.on(phatbeat.BTN_FASTFWD)
        def pb_fast_forward(pin):
            print(vlc.communicate("next"))

        @phatbeat.on(phatbeat.BTN_REWIND)
        def pb_rewind(pin):
            print(vlc.communicate("prev"))
        
        @phatbeat.on(phatbeat.BTN_ONOFF)
        def pb_onoff(pin):
            print(vlc.communicate("pause"))
            print(vlc.kill())
            print("Bye Bye ...")
            vlc.shutdown()
            exit()
        
        signal.pause()
    else:
        exit()
