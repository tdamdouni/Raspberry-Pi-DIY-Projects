import HTU21D as temp_humid
import ds18b20_therm as soil_temp
from time import sleep
import matplotlib.pyplot as plt

# Set up
interval = 5
temp_probe = soil_temp.DS18B20()
ambient_temp = temp_humid.HTU21D()
x = [i for i in range(0,10*interval,interval)]

soil_temp = []
amb_temp = []

# Take 10 readings
print("Taking 10 readings, one every " + str(interval) + " seconds...")


for i in range(10):
    soil_temp.append( temp_probe.read_temp() ) 
    amb_temp.append( ambient_temp.read_temperature() )    
    print("Reading " + str(i) )
    sleep(interval)


print("Finished readings, generating graph...")

# Make a figure

plt.plot(x, soil_temp, 'r', label="Soil Temperature")
plt.plot(x, amb_temp, 'g', label="Ambient Temperature")

plt.suptitle('Temperature sensor readings', fontsize=14, fontweight='bold')
plt.xlabel('Time in seconds')
plt.ylabel('Temperature in degrees Celsius')

plt.ylim(ymin=0)

plt.legend(loc="lower right")

plt.show()







