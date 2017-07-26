from datetime import datetime
from sense_hat import SenseHat
from evdev import InputDevice, categorize, ecodes,list_devices
from select import select
import threading

sense = SenseHat()

## Logging Settings
TEMPERATURE=True
HUMIDITY=True
PRESSURE=True
ORIENTATION=True
ACCELERATION=True
MAG=True
GYRO=True
DELAY = 0
BASENAME = ""

def file_setup(filename):
    header =[]
    if TEMPERATURE:
        header.extend(["temp_h","temp_p"])
    if HUMIDITY:
        header.append("humidity")
    if PRESSURE:
        header.append("pressure")
    if ORIENTATION:
        header.extend(["pitch","roll","yaw"])
    if MAG:
        header.extend(["mag_x","mag_y","mag_z"])
    if ACCELERATION:
        header.extend(["accel_x","accel_y","accel_z"])
    if GYRO:
        header.extend(["gyro_x","gyro_y","gyro_z"])
    header.append("timestamp")

    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")

## Function to capture input from the Sense HAT Joystick
def get_joystick():
    devices = [InputDevice(fn) for fn in list_devices()]
    for dev in devices: 
        if dev.name == "Raspberry Pi Sense HAT Joystick":
            return dev

## Function to collect data from the Sense HAT and build a string
def get_sense_data():
    sense_data=[]
    
    if TEMPERATURE:
        sense_data.extend([sense.get_temperature_from_humidity(),sense.get_temperature_from_pressure()])
        
    if HUMIDITY:
        sense_data.append(sense.get_humidity())
     
    if PRESSURE:
        sense_data.append(sense.get_pressure())
        
    if ORIENTATION:
        yaw,pitch,roll = [sense.get_orientation()[key] for key in ['yaw','pitch','roll']]
        sense_data.extend([pitch,roll,yaw])

    if MAG:
        mag_x,mag_y,mag_z = [sense.get_compass_raw()[key] for key in ['x','y','z']]
        sense_data.append([mag_x,mag_y,mag_z])

    if ACCELERATION:
        x,y,z = [sense.get_accelerometer_raw()[key] for key in ['x','y','z']]
        sense_data.extend([x,y,z])

    if GYRO:
        gyro_x,gyro_y,gyro_z = [sense.get_gyroscope_raw()[key] for key in ['x','y','z']]
        sense_data.extend([gyro_x,gyro_y,gyro_z])
    
    sense_data.append(datetime.now())
     
    return sense_data

def show_state(logging):
    if logging:
        sense.show_letter("!",text_colour=[0,255,0])
    else:
        sense.show_letter("!",text_colour=[255,0,0])

def check_input():
    r, w, x = select([dev.fd], [], [],0.01)
    for fd in r:
        for event in dev.read():
            if event.type == ecodes.EV_KEY and event.value == 1:
                print(event.code)
                if event.code == ecodes.KEY_UP:
                    print("quiting")
                    return True,False
                else:
                    return True,True
    return False,True

def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)

def timed_log():
  threading.Timer(DELAY, timed_log).start()
  if logging == True:
        print("logged")
        log_data()


## Main Program
run=True
logging=False
show_state(logging)
dev = get_joystick()
batch_data= []

if BASENAME == "":
    filename = "SenseLog-"+str(datetime.now().strftime("%Y-%m-%d-%H%M"))+".csv"
else:
    filename = BASENAME+"-"+str(datetime.now().strftime("%Y-%m-%d-%H%M"))+".csv"

file_setup(filename)

if DELAY >= 1:
    timed_log()

while run==True:
    
    key_press,run = check_input()

    if key_press:
        if logging==True:
            with open(filename,"a") as f:
                for line in batch_data:
                    f.write(str(line) + "\n")
            batch_data= []
        logging = not(logging)
        show_state(logging)

    sense_data = get_sense_data()
    if logging == True and DELAY < 1:
        log_data()


sense.clear()
