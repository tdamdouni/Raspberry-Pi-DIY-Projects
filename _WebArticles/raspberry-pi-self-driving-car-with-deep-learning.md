# Raspberry Pi Self Driving Car with Deep Learning

_Captured: 2017-08-05 at 17:14 from [medium.com](https://medium.com/@mslavescu/raspberry-pi-self-driving-car-with-deep-learning-8af69763df84?source=userActivityShare-c79006fee040-1501946030)_

# Raspberry Pi Self Driving Car with Deep Learning

![](https://cdn-images-1.medium.com/max/1600/1*SyJKZwcgJLlaHCbyMATG9w.png)

A very nice article and GitHub repository to get started in building a:

> Lane Following Autopilot with Keras & Tensorflow.

> This document walks through how to create a convolution neural network using Keras+Tensorflow and train it to keep a car between two white lines.

> Here is a Raspberry Pi controlled RC car using the autopilot crated in this document to drive between the lines. See the donkey repository for instructions to build your own car.

Read the whole story [here](https://wroscoe.github.io/keras-lane-following-autopilot.html) and Hacker News comments [here](https://news.ycombinator.com/item?id=13462136).

I forked the repository here for further integration in [OSSDC Initiative:](http://ossdc.org/)

> <https://github.com/OSSDC/donkey>

#### Update 1:

Sam pointed on Hacker News to his Tensorflow on Raspberry Pi repository.

I forked his repository here:

> <https://github.com/OSSDC/tensorflow-on-raspberry-pi>

The method described in the above article uses a computer to run Tensorflow (which is easier to get started) and gets the images and other sensors info from RPi over WiFi, if you want to make the RPi car fully autonomous (untethered) try Sam's approach to run everything on Raspberry Pi.

Another method to run Tensorflow on Raspberry Pi is described here:

> [How to build a robot that "sees" with $100 (with Raspberry Pi) and TensorFlow](https://medium.com/@mslavescu/how-to-build-a-robot-that-sees-with-100-with-raspberry-pi-and-tensorflow-e2f4feceed53)
