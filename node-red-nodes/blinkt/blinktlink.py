#!/usr/bin/env python

import time
import sys
from threading import Thread, Event
from Queue import Queue, Empty

class NonBlockingStreamReader:

    def __init__(self, stream):
        '''
        stream: the stream to read from.
                Usually a process' stdout or stderr.
        '''

        self._s = stream
        self._q = Queue()
        self._stop_event = Event()

        def _populateQueue(stream, queue, stop_event):
            '''
            Collect lines from 'stream' and put them in 'queue'.
            '''
            while not stop_event.is_set():
                line = stream.readline()
                if line:
                    queue.put(line)

        self._t = Thread(target = _populateQueue,
                args = (self._s, self._q, self._stop_event))
        self._t.daemon = True
        self._t.start() #start collecting lines from the stream

    def readline(self, timeout = None):
        try:
            return self._q.get(block = timeout is not None, timeout = timeout)
        except Empty:
            return None

    def stop(self):
        self._stop_event.set()


def millis():
    return int(round(time.time() * 1000))

def emit(message):
    sys.stdout.write(message + "\n")
    sys.stdout.flush()

def error(message):
    emit("ERROR: " + message)

def fatal(message):
    emit("FATAL: " + message)
    sys.exit(1)


try:
    import blinkt
except ImportError:
    fatal("Unable to import explorerhat python library")

error("Starting up...")
blinkt.clear()
blinkt.show()

running = True

stdin = NonBlockingStreamReader(sys.stdin)

def handle_command(cmd):
    if cmd is not None:
        cmd = cmd.strip()

        if cmd.startswith("all") and ":" in cmd:
            cmd, data = cmd.split(":")
            r, g, b = [int(x) for x in data.split(",")]

            for index in range(8):
                blinkt.set_pixel(index, r, g, b)

            blinkt.show()
            return

        # Expects a message formatted like: pixel.x.y:r,g,b
        if cmd.startswith("pixel.") and ":" in cmd:
            cmd, data = cmd.split(":")
            cmd, index = cmd.split(".")
            pixels = [int(x) for x in data.split(",")]
            index = int(index)

            while len(pixels) > 0:
                blinkt.set_pixel(index, pixels.pop(0), pixels.pop(0), pixels.pop(0))
                index += 1
                index %= 8

            blinkt.show()
            return

        if cmd.startswith("clear"):
            blinkt.clear()
            blinkt.show()

        if cmd.startswith("stop"):
            stdin.stop()
            running = False


while running:
    cmd = stdin.readline(0.1)
    handle_command(cmd)
    time.sleep(0.001)

