import RPi.GPIO as gp
import os
from pyPiCamLed import PiCamLed as cl

gp.setwarnings(False)
gp.setmode(gp.BCM)

led = cl() 
led.Open()
led.SetState(1)
 
def main():
    led.SetState(1)
    capture(1)

    #led.SetState(0)
    #capture(2)
  
def capture(cam):
    cmd = "raspistill -o capture_%d.jpg" % cam
    os.system(cmd)
    led.Close()

if __name__ == "__main__":
    main()

    led.SetState(1)
    
