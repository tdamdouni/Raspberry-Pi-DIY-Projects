Even this code isn’t perfect. You will probably notice that the LEDs appear to turn off slower than they turn on. They’re actually transitioning through the steps at the same speed each way, but the changes in the higher-end of the brightness are much less perceptible than those in the lower end.

Also, you might notice red/green kicking in first. This is a problem that this method introduces that’s less pronounced when you use global brightness.

You can import set_clear_on_exit and use set_clear_on_exit(False) to prevent Blinkt! being cleared when your code exits.

But ideally you need to run a script continuously to display a solid colour, this is because the APA102 LEDs on Blinkt! can very easy interpret environmental noise as signal and display something random.

To do that, you would write something like this:

```python
import time
from blinkt import set_pixel, set_brightness, show, clear

set_brightness(0.1)
clear()

FPS = 15

# set all pixels to RED
while True:
    for i in range(8):
        set_pixel(i, 255, 0, 0)

    show()
    time.sleep(1.0 / FPS)
```