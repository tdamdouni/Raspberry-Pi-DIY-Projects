import serial

serialMsg = serial.Serial("/dev/ttyACM0", 9600)

while True:
    rawMsg = serialMsg.readline()
    message = (rawMsg.decode().strip())
    if (message == "Motion detected!"):
        print("Arduino says: Motion detected!")