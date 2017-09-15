import smbus
import time

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
GPIOA  = 0x12 # Register for inputs

# Set first 6 GPA pins as outputs and
# last one as input.
bus.write_byte_data(DEVICE,IODIRA,0x80)

# Loop until user presses CTRL-C
while True:

  # Read state of GPIOA register
  MySwitch = bus.read_byte_data(DEVICE,GPIOA)
  
  if MySwitch & 0b10000000 == 0b10000000:
   print "Switch was pressed!"
   time.sleep(1)