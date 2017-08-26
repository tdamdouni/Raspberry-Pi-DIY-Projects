#  Sensing the Weather - Rainfall Lesson

In this lesson students will learn how the rain gauge works, then Python code will be written to interface with it, detect rainfall, and display the measurement value.

## Sensor guide

Here is some background information [about the rain gauge](../guides/rain_gauge.md).

## Learning objectives

- To understand how the rain gauge works by creating signal pulses
- To be able to collect and interpret data from an external sensor
- To be able to convert bucket tips into a measurement of rainfall in mm
- Understand and evaluate the difference between polling a sensor and using interrupts

## Cross-curricular applications

- Computer Science - loops, functions, variables
- Geography - rainfall data from local area
- Physics - pull up/pull down circuits, sensors
- Mathematics - surface area, volume, conversion to mm


## Lesson summary

- How does the rain gauge work?
- Counting signals using polling
- Counting signals using interrupts
- Plenary: Which is best?

## Starter

Examine the rain gauge sensor and discuss with pupils how it works and measures the rainfall over time. Read the [rain gauge](../guides/rain_gauge.md) guide for more detailed information.

- Ask students what they think it does and how they think it works.
- Open it up and explore the sensor, reed switch, and magnet.
- More able students could research the link between mm of rainfall and a ml quantity.

Once you have explored how the sensor works, you should connect it up to the Raspberry Pi Weather Station in order to demonstrate it later in the lesson.

## Main development

1. Students boot their Raspberry Pi.
1. Students follow the [worksheet](worksheet.md) to create a polling program to gather data from the sensor, and create an interrupt program to gather data from the sensor.
1. Discuss with students the difference between polling vs. using interrupts: polling monopolises the processor, but interrupts only occur when the sensor is triggered.

## Plenary

Ask the class the following questions:

1. Why is the unit of measurement for rainfall a length/depth as opposed to a volume?
1. What are the advantages of using interrupt handlers over continuous polling?

**Answers:**

1. The rain gauge measures only a small sample of the rain that falls from the sky. However, we can assume that the amount of rain falling into it will be the same as that falling everywhere locally per unit of surface area. This allows us to assert that our calculation of rainfall will equate to the amount of rain that has fallen over a much larger area than the rain gauge itself.
1. Interrupt handlers allow you to avoid having to write code to compare the current and previous states of the GPIO pin between each iteration of a continuous polling loop.


## Extension

- Students could test the accuracy of their rain gauge program by pouring a known amount of water and observing the measured result. 1mm of rainfall equates to 1 litre of water per square metre (1mm of rainfall = 1L/m^2).
