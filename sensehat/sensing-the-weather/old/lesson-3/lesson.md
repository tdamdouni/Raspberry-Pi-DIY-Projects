#  Weather Station Basic I/O - Lesson Plan 3

In this lesson students will examine the weather station rain gauge and simulate it using a button. Students will first learn how the rain gauge works, then Python code will be written to interface with it, detect rainfall, and display the measurement value.

## Learning objectives

- To understand how the rain gauge works by creating signal pulses
- To be able to collect and interpret data from an external sensor
- To understand the difference between polling and interrupt handling

## Learning outcomes

### All students are able to

- Connect their rain gauge / buttons to another pin
- With direction, adapt the last lesson's code to poll the rain gauge and count signals


### Most students are able to

- Explain how we convert bucket tips into a useful measurement
- With direction, adapt the last lesson's code to use interrupts to count signals

### Some students are able to

- Independently adapt their code to count the number of bucket tips and display meaningful rainfall data
- Evaluate the differences between polling and using interrupts

## Lesson Summary

- How does the rain gauge work?
- Review pull up code
- Counting signals using polling
- Counting signals using interrupts
- Plenary: Which is best?

## Starter

Examine the rain gauge sensor and discuss with pupils how it works and measures the rainfall over time. Review the [Rain Gauge Guide](../guides/weather_station/rain_gauge.md) for more detailed information.
- Ask students what they think it does and how they think it works.
- Open it up and explore the sensor, reed switch and magnet.
- More able students could research the link between mm of rainfall and a ml quantity.

Once you have explored how the sensor works you should connect it up to a Pi in order to demonstrate later in the lesson.

## Main development

1. Students boot their Raspberry Pi. Review last lesson's code with them: students could add some comments or simply discuss what each line does.
2. Students follow [worksheet](worksheet.md) to:
  - connect a button to pin 6 (instead of pin 4)
  - adapt their code to the new pin
  - use their polling program to count sensor inputs
3. Discuss with students the difference between polling vs using interrupts: polling monopolises the processor whilst interrupts only occur when the sensor is triggered.
4. Students finish by creating an alternative program using interrupts rather than polling.

## Plenary

Ask the class the following questions:

1. Why could we not use a pull down circuit to detect the bucket tip?
1. Why is the unit of measurement for rainfall a length/depth as opposed to a volume?
1. What are the advantages of using interrupt handlers over continuous polling?
1. What is de-bouncing?

**Answers:**

1. The weather expansion board has fixed circuitry that we cannot change. The rain gauge has two wires; one is hardwired to GPIO 6, and the other is hardwired to ground, which means we can only short GPIO 6 to ground. If we used a pull down on GPIO 6 we would be shorting ground to ground, and this would not produce a detectable change in the `HIGH` or `LOW` state of GPIO 6 when the bucket tips; it would only ever read `LOW`.
1. The rain gauge measures only a small sample of the rain that falls from the sky. However, we can assume that the amount of rain falling into it will be the same as that falling everywhere locally per unit of surface area. This allows us to assert that our calculation of rainfall will equate to the amount of rain that has fallen over a much larger area than the rain gauge itself.
1. Interrupt handlers allow you to avoid having to write code to compare the current and previous states of the GPIO pin between each iteration of a continuous polling loop.
1. De-bouncing is a timeout, started when an interrupt occurs, during which subsequent interrupt events are ignored. This avoids switch bounce causing multiple, undesired event detections that could produce erroneous results.

## Extension

- Students could test the accuracy of their rain gauge program by pouring a known amount of water and observing the measured result.
