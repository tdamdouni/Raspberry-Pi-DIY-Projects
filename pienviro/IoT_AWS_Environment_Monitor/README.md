# IoT Smart Environmental Monitoring

A IoT Java based project developed for the Raspberry Pi used to participate in The AWS IoT Mega Contest Hackathon 

https://www.hackster.io/contests/AWSIoTMegaContest


Small and easy to use device to monitor temperature, humidity, noise levels, luminosity and atmospheric pressure.

It sends data to the AWS IoT Platform 


## Screenshots

### Device
![alt tag](https://hackster.imgix.net/uploads/image/file/113675/3.jpg?w=680&h=510)

### Reading sensors
![alt tag](https://hackster.imgix.net/uploads/image/file/116646/Screenshot%20from%202016-01-30%2001-10-44.png)

### Using the AWS IoT platform 
![alt tag](https://hackster.imgix.net/uploads/image/file/118254/Screenshot%20from%202016-02-01%2001-00-12.png)



## Code 

- The dist folder contains the compiled binaries to deploy to the Raspberry Pi

- The read_monitoring_device folder contains the application that reads the
  sensors , logs data and communicates with AWS

- The sensors_lib folder contains a Java library coded for this project that
  reads analog and digital data from the sensots and converts it to a known measure unit


- The update_AWS_device folder contains a javascript application that uses the
  official aws-iot-device-sdk for the raspberry to communicate with AWS


## User Guide

A complete user guide with step by step procedures on how to setup this project
from scratch, including raspberry setup and circuit schematics is found here:



https://www.hackster.io/alapisco/smart-environmental-monitoring-2552bb
