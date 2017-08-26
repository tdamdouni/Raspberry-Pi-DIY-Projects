import HTU21D as temp_humid

humidity_sensor = temp_humid.HTU21D()

humidity = humidity_sensor.read_humidity()
temperature = humidity_sensor.read_temperature()
dewpoint = ((humidity / 100) ** 0.125) * (112 + 0.9 * temperature) + (0.1 * temperature) - 112

print("Relative Humidity: " + str(humidity) )
print("Temperature: " + str(temperature) )
print("Dewpoint: " + str(dewpoint) )



