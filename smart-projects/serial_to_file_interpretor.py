import serial

serial_port = '/dev/INSERT SERIAL PORT HERE'
baud_rate = 9600
write_to_file_path = "serial.txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline()
    line = line.decode("utf-8")
    print(line);
    output_file.write(line)