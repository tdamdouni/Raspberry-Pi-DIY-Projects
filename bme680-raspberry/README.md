# BME680 interface with Raspberry Pi
## Introduction

This program serves as a working example to read the measurements from a BME680 via the raspberry pi. Actually I wanted to read out the sensor via python, but as the driver provided by Bosch is a C file, I created this small C program to communicate to the sensor. The compile program can then be called from python. 


## Usage guide
### Compiling the program
Download the driver for the [BME680](https://github.com/BoschSensortec/BME680_driver) from github.
Put the file from this repository into the same directory.

As this program uses i2c-dev, check you can use `i2cdetect -y 1` to verify if your I²C communication works via bus 1. You might need to adapt the code according your I²C Bus in the line `g_i2cFid = open("/dev/i2c-1", O_RDWR);` to `g_i2cFid = open("/dev/i2c-0", O_RDWR);` if bus 0 is used. Also check the I²C address of your sensor. The provided code uses `BME680_I2C_ADDR_SECONDARY` (0x77) as the address. 


After this adaption you can compile the program with
`gcc bme680_main.c bme680.c -o bme680`


### Command line interface 
The program can be called with up to three parameters. However, be aware that no special input check is implemented.
1. `./bme680`: This will print three measurement results with the time of the measurement on the standard output stream. The delay between each measurement is 3 seconds.
```shell
pi@raspberrypi:~/myproject/sensors/bme680 $ ./bme680 
**** BME680 start measurements  ****
2017-10-07 19:48:18 T: 19.51 degC, P: 1013.08 hPa, H: 69.61 %rH , G: 3954 ohms
2017-10-07 19:48:21 T: 19.53 degC, P: 1013.06 hPa, H: 69.43 %rH , G: 9471 ohms
2017-10-07 19:48:24 T: 19.54 degC, P: 1013.04 hPa, H: 69.28 %rH , G: 16839 ohms
**** Measurement finished ****
pi@raspberrypi:~/myproject/sensors/bme680 $ 
```
2. `./bme680 5 2`: The first parameter defines the delay between each measurement. The second parameter defines the number of measurements before the program is terminated.
```shell
pi@raspberrypi:~/myproject/sensors/bme680 $ ./bme680 5 2
**** BME680 start measurements  ****
2017-10-07 20:02:41 T: 19.51 degC, P: 1012.86 hPa, H: 69.87 %rH , G: 26970 ohms
2017-10-07 20:02:46 T: 19.52 degC, P: 1012.84 hPa, H: 69.71 %rH , G: 44102 ohms
**** Measurement finished ****
pi@raspberrypi:~/myproject/sensors/bme680 $ 
```
3. `./bme680 5 2 output.txt`: You can also provide a third argument, which will be used to write the measurements into a file.

### Usage within Python
If you want to use this program in python, you can simply call it with `check_output`.

```python
from subprocess import check_output
out = check_output(["bme680", str(measDelay), str(nMeas)])
```
If any problems with concurrent I²C bus usages occur, you can check if the file *~bme680i2c.lock* exists, as this is created at the start of the program and deleted shortly before termination.






