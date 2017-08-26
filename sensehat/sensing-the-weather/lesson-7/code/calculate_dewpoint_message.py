import HTU21D as temp_humid

humidity_sensor = temp_humid.HTU21D()

humidity = humidity_sensor.read_humidity()
temperature = humidity_sensor.read_temperature()
dewpoint = ((humidity / 100) ** 0.125) * (112 + 0.9 * temperature) + (0.1 * temperature) - 112

print("Relative Humidity: " + str(humidity) )
print("Temperature: " + str(temperature) )
print("Dewpoint: " + str(dewpoint) )


dew_description = { 0 : "A bit dry for some",
                    12 : "Very comfortable",
                    16 : "Comfortable",
                    18 : "Upper edge of comfortable",
                    21 : "Somewhat uncomfortable",
                    24 : "Quite uncomfortable",
                    26 : "Extremely uncomfortable",
                    27 : "Severely high to deadly" }


# Get a list of the possible thresholds
thresholds = list(dew_description.keys())
print(thresholds)
thresholds.sort()

threshold_exceeded = 0

# Loop through all thresholds and set threshold_exceeded to the highest exceeded
for temp in thresholds:
    if dewpoint >= temp:
        threshold_exceeded = temp

# Print out the corresponding message
print( dew_description[threshold_exceeded] )
