_http://forums.pimoroni.com/t/unpredictable-blinkt-results-w-1-process-controlling-leds/4948/7_

My usual approach to this pattern/problem is to have a single thread responsible for running show() periodically, in your case the simplest approach might be to remove show() from both threads and, instead, place it in a while True loop in the main thread with an appropriate time.sleep(1.0/30) where 30 is your desired Blinkt! update rate in updates per second leaving you with:

```
from time import sleep
from threading import Thread
from blinkt import set_pixel, show

FPS = 30

def red():
while True:
    for l in range(0,4,1):
            set_pixel(l, 1, 0, 0)
            sleep(.25)
    for l in range(3,-1,-1):
            set_pixel(l, 0, 0, 0)
            sleep(.25)
def blue():
while True:
    for l in range(4,8,1):
            set_pixel(l, 0, 0, 1)
            sleep(.25)
    for l in range(7,3,-1):
            set_pixel(l, 0, 0, 0)
            sleep(.25)

if __name__ == '__main__':
    Thread(target = red).start()
    Thread(target = blue).start()
    while True:
        show()
        time.sleep(1.0/FPS)
```

In this case your pixel colour changes will not be synced to updates, resulting in some imprecise timing, but since anything timed with time.sleep() is not especially precise in the first place that's kind of academic.

(Note: time.sleep() is imprecise because you're not taking into account the amount of time it takes for the rest of the code to run, which can be variable depending on the Pi you happen to be running it on)
