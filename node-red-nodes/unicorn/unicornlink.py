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

def notice(message):
    emit("NOTICE: " + message)

try:
    import unicornhat
except ImportError:
    fatal("Unable to import unicornhat python library")

notice("Starting up...")
unicornhat.clear()
unicornhat.show()

running = True

stdin = NonBlockingStreamReader(sys.stdin)

width, height = unicornhat.get_shape()

def handle_command(cmd):
    global width, height

    if cmd is not None:
        cmd = cmd.strip()

        if cmd.startswith("all") and ":" in cmd:
            cmd, data = cmd.split(":")
            r, g, b = [int(x) for x in data.split(",")]

            for x in range(width):
                for y in range(height):
                    unicornhat.set_pixel(x, y, r, g, b)

            unicornhat.show()
            return

        # Expects a message formatted like: pixel.x.y:r,g,b
        if cmd.startswith("pixel.") and ":" in cmd:
            cmd, data = cmd.split(":")
            cmd = cmd.split(".")

            if len(cmd) == 3:
                cmd, x, y = cmd
            else:
                cmd, x = cmd
                y = 0

            pixels = [int(p) for p in data.split(",")]
            x, y = int(x), int(y)

            while len(pixels) > 0:
                unicornhat.set_pixel(x, y, pixels.pop(0), pixels.pop(0), pixels.pop(0))
                x += 1
                if x > 7:
                    x = 0
                    y += 1
                if y > 7:
                    y = 0

            unicornhat.show()
            return

        if cmd == "hat":
            unicornhat.set_layout(unicornhat.HAT)
            width, height = unicornhat.get_shape()
            return

        if cmd == "phat":
            unicornhat.set_layout(unicornhat.PHAT)
            width, height = unicornhat.get_shape()
            return

        if cmd == "clear":
            unicornhat.clear()
            unicornhat.show()

        if cmd == "stop":
            stdin.stop()
            running = False


while running:
    cmd = stdin.readline(0.1)
    handle_command(cmd)
    time.sleep(0.001)

