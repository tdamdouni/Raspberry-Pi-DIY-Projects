_https://raspberrypi.stackexchange.com/questions/56455/raspberry-pi-zero-battery-life-with-4400mah-battery_

If you want to evaluate the battery life by yourself, those are the considerations. You must evaluate the mean energy absorbed by Raspberry in your project. You can use a 'USB voltage and current tester' to check current need by your progect. If this value is not constant over the time, you have to do a mean.

The power (or if you prefer, the energy need for 1 second) absorbed by the device, is V*I. V for Raspberry is 5 Volt. Suppose, I = 150 mA so P=5*0,15 = 0.75 W or 750 mW.

Now, if your supply is a battery, I suppose you have a DC/DC converter, to convert the battery voltage to Raspberry's voltage. The converter isn't ideal. A small converter may have a performance of about 90%, so for every watt from Raspberry, you need 1.11W from battery. 10% of energy is wasted as heat on the converter.

In the example 0.75W from Raspberry is 0.75/.9 = 0.83 W from the battery or 0.83 W per second. Your battery with 4,4 Ah (or 4400 mAh) at 3,7 volt (I suppose a lithium battery) store an energy equal to 4,4*3,7*3600 = 58608 joule (we multiply by 3600, the seconds on one hour).

The life of your battery, in seconds, is (energy stored on battery)/( absorbed energy), in our example 58608/.83 = 70612 seconds or 70612/3600=19.6 hours.
