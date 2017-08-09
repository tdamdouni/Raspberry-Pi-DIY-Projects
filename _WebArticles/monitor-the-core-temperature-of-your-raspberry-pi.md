# Monitor the core temperature of your Raspberry Pi.

_Captured: 2017-08-05 at 17:39 from [medium.com](https://medium.com/@kevalpatel2106/monitor-the-core-temperature-of-your-raspberry-pi-3ddfdf82989f?source=userActivityShare-c79006fee040-1501947534)_

![](https://cdn-images-1.medium.com/max/2000/1*l2nLQ7PGOfrUu0RM_FFudA.jpeg)

# Monitor the core temperature of your Raspberry Pi.

Raspberry Pi is a pretty powerful device. That is why people are using their raspberry pi for performing some intensive tasks that squeeze last drop of CPU power from the Raspberry Pi. You can also overclock the Raspberry Pi to make it more powerful.

Raspberry Pi consumes very less power compare to your desktop CPU. But just like every other computer, while performing heavy tasks, it also gets hot.

### Why do you need to monitor core temperature?

Many times, you want to keep an eye on the core temperature. You want to constantly measure the core temperature of your raspberry pi.

In my last project, I was building Tensorflow on my raspberry pi. It was long running CPU intensive task. I also overclocked my raspberry pi to run on 1300 MHz. So, it was going to fry my CPU. (And nobody wants to do that with their little Pi.) I was looking for a way to measure core temperature constantly.

### What happens if your Raspberry Pi gets too hot?

Raspberry Pi is a low-end mobile computer. So it doesn't have fans to cool it down like other desktop/laptop CPUs.

If your temperature rises above _80°C_, you will see a little thermometer on you Raspbian desktop. That indicates that your Pi is getting hot.

![](https://cdn-images-1.medium.com/max/1600/1*JGkRCBW3uZ3HuDsWHQLHjg.png)

As the core temperature rises, the thermometer gets to fill. Then at 85°C, it changes to a full thermometer. However, that is the maximum recommended operating temperature. After this temperature, your CPU starts throttling and reduces the clock to cool down the temperature. This will decrease the performance.

So, I decided to write a small python script to monitor core temperature. Let's get started.

### How can you measure the core temperature?

You can measure the core temperature by issuing following command in your Raspberry Pi terminal.

/opt/vc/bin/vcgencmd measure_temp
[view raw](https://gist.github.com/kevalpatel2106/dd1cca23c04a9cf0ccebc8e485a94566/raw/67ddf35e2b86ea60a0ef947afdf3b68f16783041/monitor-temp.sh) [monitor-temp.sh](https://gist.github.com/kevalpatel2106/dd1cca23c04a9cf0ccebc8e485a94566#file-monitor-temp-sh) hosted with ❤ by [GitHub](https://github.com)

It will give you core temperature in Celcius.

pi@raspberrypi:~ $ /opt/vc/bin/vcgencmd measure_temp

temp=56.9'C
[view raw](https://gist.github.com/kevalpatel2106/bb4ab988179850f6d530b5137143e381/raw/3517cc8fcbf1e4b01cbacd79580534529ae48ce0/gistfile1.txt) [gistfile1.txt](https://gist.github.com/kevalpatel2106/bb4ab988179850f6d530b5137143e381#file-gistfile1-txt) hosted with ❤ by [GitHub](https://github.com)

Great. Let's write a python script to monitor and print the temperature every second.

### Constantly monitor the core temperature.

  * Login to your Raspberry Pi terminal by SSH or using VNC.
  * Create new python file monitor-temp.py by issuing following command.

nano monitor-temp.py
[view raw](https://gist.github.com/kevalpatel2106/b74e01b1a54dad005323e7126b366668/raw/384996b6290e85bee6e3e5ad0cba5a1df83c3775/bash.sh) [bash.sh](https://gist.github.com/kevalpatel2106/b74e01b1a54dad005323e7126b366668#file-bash-sh) hosted with ❤ by [GitHub](https://github.com)

  * Write down below code in that file. This script issues the command _/opt/vc/bin/vcgencmd measure_temp_ every second and print the formatted temperature in the console.

import os

import time

def measure_temp():

temp = os.popen("vcgencmd measure_temp").readline()

return (temp.replace("temp=",""))

while True:

print(measure_temp())

time.sleep(1)
[view raw](https://gist.github.com/kevalpatel2106/ac79e08e6362e246e757895d0e9aa1f6/raw/49761335a9caec4ff2a8b2e5dac597b6a1b51d53/monitor-temp.py) [monitor-temp.py](https://gist.github.com/kevalpatel2106/ac79e08e6362e246e757895d0e9aa1f6#file-monitor-temp-py) hosted with ❤ by [GitHub](https://github.com)

  * Press **Ctl+X** and then Y to save that file.

That's it. Now run the python script by issuing below command:

python monitor-temp.py
[view raw](https://gist.github.com/kevalpatel2106/4952e7257e2fa73c81c200f0fa4c8509/raw/1d120c85f18b4fb693b9f0312ee021612bdce4ef/bash.sh) [bash.sh](https://gist.github.com/kevalpatel2106/4952e7257e2fa73c81c200f0fa4c8509#file-bash-sh) hosted with ❤ by [GitHub](https://github.com)

Volla!!! You will see updated core temperature every second. You can stop the script anytime by issuing **Ctl+C** in the terminal.

### Conclusion:

So, now you can measure and monitor the temperature. You can easily modify the script to play a buzzer or start a cooling fan if the core temperature is more than the particular limit.

_~If you liked the article, click the 💚 below so more people can see it! Also, you can follow me on_ **_[Medium_**](http://bit.ly/2h9p8o2)_or on_**_[My Blog_**](http://kevalpatel2106.com)_, so you get updates regarding my future articles!!~_
