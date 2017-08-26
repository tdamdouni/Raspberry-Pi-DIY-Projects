import ds18b20_therm as soil_temp
from time import sleep
import matplotlib.pyplot as plt


interval = 5
temp_probe = soil_temp.DS18B20()
x = [i for i in range(0,10*interval,interval)]
y = []

print("Taking 10 readings, one every " + str(interval) + " seconds...")

for i in range(10):
    y.append(temp_probe.read_temp())
    print("Reading " + str(i) )
    sleep(interval)


print("Finished readings, generating graph...")

# Make a figure

plt.plot(x,y)

plt.suptitle('Soil Temperature', fontsize=14, fontweight='bold')
plt.xlabel('Time in seconds')
plt.ylabel('Temperature in degrees Celsius')

plt.show()
