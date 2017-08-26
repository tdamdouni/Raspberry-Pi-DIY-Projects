#!/usr/bin/env python
#To install pivumeter
#git clone http://github.com/pimoroni/pivumeter -b devel --depth=1
#cd pivumeter
#./setup.sh
#cd python_server/library
#sudo python setup.py install

import pivumeter
import signal
import scrollphathd
import threading
import time

try:
    import queue
except ImportError:
    import Queue as queue

class OutputScrollPhatHD(pivumeter.OutputDevice):
    def __init__(self):
        super(OutputScrollPhatHD, self).__init__()

        self.running = False
        self.busy = False
        scrollphathd.set_brightness(0.5)
        self.messages = queue.Queue()

        self._thread = threading.Thread(target=self.run_messages)
        self._thread.daemon = True
        self._thread.start()

    def run_messages(self):
        self.running = True
        while self.running:
            try:
                message = self.messages.get(False)
                self.busy = True
                scrollphathd.clear()
                length = scrollphathd.write_string(message)
                scrollphathd.set_pixel(length + 17, 0, 0)
                scrollphathd.show()
                time.sleep(1)
                for x in range(length):
                    if not self.running: break
                    scrollphathd.scroll(1)
                    scrollphathd.show()
                    time.sleep(0.05)
             
                scrollphathd.clear()
                self.messages.task_done()
                self.busy = False
            except queue.Empty:
                pass
            time.sleep(1)

    def setup(self):
        pass

    def display_fft(self, bins):
        if self.busy: return
        self.busy = True
        scrollphathd.set_graph(bins, low=0, high=65535, brightness=0.5, x=0, y=0)
        scrollphathd.show() 
        self.busy = False

    def display_vu(self, left, right):
        pass

    def cleanup(self):
        self.running = False
        self._thread.join()

print("""
This advanced proof of concept will let you type messages into the console.
They will display in place of the VU meter.
Type a message and hit enter for it to scroll across the display.
Press Ctrl+C then hit Enter to exit.
""")

output_device = OutputScrollPhatHD()

pivumeter.run(output_device)

try:
    while pivumeter.running:
        output_device.messages.put(raw_input("\n\nYour message: "))
        time.sleep(1)
except KeyboardInterrupt:
    pass

