import explorerhat as eh
import time

print("Distance Measurement in Progress")

eh.output.one.off()
print("Waiting for Sensor to Settle")
time.sleep(2)

def measure():
    eh.output.one.on()
    print("Out on")
    time.sleep(0.01)
    eh.output.one.off()
    print("Out off")

    while eh.input.one.read()==0:
        pulse_start = time.time()
    while eh.input.one.read()==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    print(pulse_duration)

    distance = pulse_duration*17150
    distance = round(distance,2)

    print"Distance: ",distance," cm"

while True:
    measure()
    time.sleep(1)


