# About the relative humidity sensor

Here is the relative humidity sensor component on the air quality sensor board included with the Raspberry Pi Weather Station. The component is circled in red. (The relative humidity and ambient temperature are both measured by the same sensor.)

![Relative Humidity Sensor](images/air_board.png)

## How does it work?

This sensor detects both the ambient temperature and the relative humidity of the air surrounding it. We have explored the temperature part of the sensor already in the [lesson on ambient temperature](../lesson-6/lesson.md).

These types of sensor detect changes in temperature and humidity in two possible ways, depending on how they are built.

**Capacitive sensing** - The sensor uses a material which absorbs water from the air. The sensor's capacitance (ability to store an electric charge) changes depending on how much water vapour the air contains, and this can be measured and converted into meaningful units.

**Resistive sensing** - The sensor uses a material which has the property that its resistance (how easy it is for a current to pass through it) changes depending on the humidity of the surrounding air, and this value is measured and converted into meaningful units.


## How does the sensor connect?

1. First, set up your main Raspberry Pi Weather Station box.
1. The ambient temperature and relative humidity sensor is a component on the air quality sensor board. Connect this board to the main Weather Station with the cable attached to the port labelled "Air Sensor".
1. Power on your Weather Station and log in.

## What does the relative humidity tell us?

Relative humidity is directly related to the ambient temperature. It's for this reason that we can access both temperature and relative humidity data from the same sensor. Relative humidity is defined as the amount of water vapour present in the air, as a percentage of the amount of water vapour needed for *saturation* at that temperature.

![Relative humidity equation](images/relative_humidity_equation.png)

For example, at 20 degrees C, the saturation vapour density is 17.3g/m<sup>3</sup>. The saturation vapour density is the maximum amount of water vapour the air can hold at that temperature.

This web page has details on [relative humidity](http://hyperphysics.phy-astr.gsu.edu/hbase/Kinetic/relhum.html) which may be interesting further reading, as well as the [data sheet](http://www.mouser.co.uk/pdfdocs/HTU21DF.PDF) for the ambient temperature sensor.

The more humid the air is, the more saturated it is with water vapour. We often describe the weather as feeling 'muggy' when there is a high relative humidity. In hot climates this is particularly important, because humans cool themselves down in hot weather by sweating. If the air is at 100% relative humidity, it's already completely saturated with water vapour and sweat can't evaporate into the air to cool us off. This means that the weather temperature can feel higher or lower to a human, depending on the relative humidity of the surrounding air. Some additional information about sweat evaporation and relative humidity is available [here](http://www.fs.fed.us/eng/pubs/htmlpubs/htm10512316/).

## What is the dew point?

Have you noticed that on some mornings there's 'dew' or water droplets collecting on grass or outside surfaces? The **dew point** is the highest temperature at which water vapour from the air will condense to form dew, or in other words the temperature at which the relative humidity is 100%. In colder climates, measuring relative humidity is also important because if the dew point is reached inside a building, this can result in mould and mildew (often referred to as 'damp') and this can cause problems for human health. Some people purchase dehumidifiers to remove water vapour from the air. You can use a [dew point calculator](http://www.ajdesigner.com/phphumidity/dewpoint_equation_dewpoint_temperature.php) to find the dew point of your environment; input the current temperature and relative humidity values to find out the temperature of the dew point. We are going to write a program to calculate the dew point.

## Sample code

The following program initialises a HTU21D object to interact with the sensor and takes a single reading of the current relative humidity. It's important that this code is saved inside the `weather_station` folder on the Raspberry Pi Weather Station, as it requires access to the HTU21D library code which is saved within this folder.

```python
import HTU21D as temp_humid

humidity_sensor = temp_humid.HTU21D()

current_humidity = humidity_sensor.read_humidity()
print( str(current_humidity) + "%")

```
