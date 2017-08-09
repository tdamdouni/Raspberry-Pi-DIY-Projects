# Accurate temperature reading from Raspberry PI Sense HAT

_Captured: 2017-07-30 at 15:46 from [yaab-arduino.blogspot.de](http://yaab-arduino.blogspot.de/2016/08/accurate-temperature-reading-sensehat.html?m=1)_

When I first received the Sense HAT for my Raspberry PI 3 I decided to start building a nice weather station using the embedded environmental sensors and RGB LED matrix.  
From a quick experiment it turns out that the temperature readings are not accurate. The problem is caused by thermal conduction from the Pi CPU to the humidity and pressure sensors on the Sense HAT.  
I have experimented few algorithms and I have found the following formula to be the most reliable. It basically compensate the temperature reading (t) with the CPU temperature (tCpu).  
_tCorr = t - ((tCpu-t)/1.5_)

Here is the full script to print each 5 seconds the environmental data including the corrected temperature.
    
    
    import os import time from sense_hat import SenseHat def get_cpu_temp(): res = os.popen("vcgencmd measure_temp").readline() t = float(res.replace("temp=","").replace("'C\n","")) return(t) sense = SenseHat() while True: t = sense.get_temperature_from_humidity() t_cpu = get_cpu_temp() h = sense.get_humidity() p = sense.get_pressure() # calculates the real temperature compesating CPU heating t_corr = t - ((t_cpu-t)/1.5) print("t=%.1f t_cpu=%.1f t_corr=%.1f h=%d p=%d" % (t, t_cpu, t_corr, round(h), round(p))) time.sleep(5) 

Running this script I have noticed that the CPU temperature reading is not very stable making the corrected temperature a little bit unstable. To fix this issue I have decided to apply a moving average to the temperature reading.  
As a further improvement I'm also the temperature both from the humidity and pressure sensors and calculating the average.
    
    
    import os import time from sense_hat import SenseHat # get CPU temperature def get_cpu_temp(): res = os.popen("vcgencmd measure_temp").readline() t = float(res.replace("temp=","").replace("'C\n","")) return(t) # use moving average to smooth readings def get_smooth(x): if not hasattr(get_smooth, "t"): get_smooth.t = [x,x,x] get_smooth.t[2] = get_smooth.t[1] get_smooth.t[1] = get_smooth.t[0] get_smooth.t[0] = x xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3 return(xs) sense = SenseHat() while True: t1 = sense.get_temperature_from_humidity() t2 = sense.get_temperature_from_pressure() t_cpu = get_cpu_temp() h = sense.get_humidity() p = sense.get_pressure() # calculates the real temperature compesating CPU heating t = (t1+t2)/2 t_corr = t - ((t_cpu-t)/1.5) t_corr = get_smooth(t_corr) print("t1=%.1f t2=%.1f t_cpu=%.1f t_corr=%.1f h=%d p=%d" % (t1, t2, t_cpu, t_corr, round(h), round(p))) time.sleep(5) 
