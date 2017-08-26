from gpiozero import DigitalInputDevice

rain_sensor = DigitalInputDevice(6)
BUCKET_SIZE = 0.2794
count = 0

def bucket_tipped():
  global count
  count = count + 1
  print (count * BUCKET_SIZE)


rain_sensor.when_activated = bucket_tipped