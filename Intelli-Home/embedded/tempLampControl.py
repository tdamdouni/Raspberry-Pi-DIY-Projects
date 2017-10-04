import spidev
import time
import os
import RPi.GPIO as GPIO

lampPin = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)

# Create a spidev object and open /dev/spidev(0,1)
spi = spidev.SpiDev()
spi.open(0,1)

def getTempReading(channel):
    # We read the sensor voltage through ADC
    adcValue = spi.xfer2([1, (8+channel) << 4, 0])
    # spidev writes back the data onto same buffer used to send data
    # We have 10-bit resoultion, so 2 bits from first byte and then 8 bits from last
    reading = ((adcValue[1]&3) << 8) + adcValue[2]
    print "Adc reading : ",reading

    # We have put reference voltage as 5V from RPi
    analogVoltage = (reading * 5) / float(1023)
    print "Voltage reading : ",analogVoltage

    tempinC = ((analogVoltage*1000) - 500) / 10
    print "Temperature in C : ",tempinC


def lampControl(state):
    if state == "OFF":
        GPIO.output(lampPin, 0)
    elif state == "ON":
        GPIO.output(lampPin, 1)

if __name__ == "__main__":
    lamp = "OFF"
    while(1):
        getTempReading(0)
        print "Toggling lamp"
#        if lamp == "OFF":
 #           lampControl("ON")
  #          malp = "ON"
   #     else:
    #        lampControl("OFF")
     #       lamp = "OFF"
        time.sleep(1)
