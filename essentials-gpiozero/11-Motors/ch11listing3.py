import time, sysimport gpiozero as g0from threading import Threadsensor = g0.DistanceSensor(echo = 16, trigger = 20)IN1_m1 = g0.OutputDevice(17)IN2_m1 = g0.OutputDevice(18)IN3_m1 = g0.OutputDevice(21)IN4_m1 = g0.OutputDevice(22)StepPins_m1 = [IN1_m1,IN2_m1,IN3_m1,IN4_m1] # Motor 1 GPIO pins IN4_m2 = g0.OutputDevice(19)IN3_m2 = g0.OutputDevice(13)IN2_m2 = g0.OutputDevice(5)IN1_m2 = g0.OutputDevice(6)StepPins_m2 = [IN1_m2,IN2_m2,IN3_m2,IN4_m2] # Motor 2 GPIO pins 
Seq = [[1,0,0,1], # Define step sequence       [1,0,0,0], # as shown in manufacturers datasheet
       [1,1,0,0],       [0,1,0,0],       [0,1,1,0],       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]StepCount = len(Seq)
all_clear = True
running = Truedef bump_watch(): # thread to watch for obstacles
    global all_clear
    while running:
        value = sensor.distance
        if value < 0.1: # trigger if obstacle within 10cm
            all_clear = False
        else:
            all_clear = True
def move_bump(direction='F', seqsize=1, numsteps=2052):    counter = 0 # 2052 steps = 1 revolution for stepsize of 2
    StepDir = seqsize # Set to 1 or 2 for fwd, -1 or -2 for back
    if direction == 'B':        StepDir = StepDir * -1    WaitTime = 10/float(1000) # adjust this to change speed    StepCounter = 0    while all_clear and counter < numsteps: # only move if no obstacles        for pin in range(0, 4):            Lpin = StepPins_m1[pin]            Rpin = StepPins_m2[pin]            if Seq[StepCounter][pin]!=0: # F = fwd, B=back, L=left, R=right                if direction == 'L' or direction == 'B' or direction == 'F': 
                    Lpin.on() # Left wheel only                if direction == 'R' or direction == 'B' or direction == 'F': 
                    Rpin.on() # Right wheel only            else: 
                Lpin.off()
                Rpin.off()        StepCounter += StepDir        if (StepCounter>=StepCount): # Repeat sequence            StepCounter = 0
        if (StepCounter<0):            StepCounter = StepCount+StepDir
        time.sleep(WaitTime) #pause 
        counter+=1
t1 = Thread(target=bump_watch) # run as seperate thread
t1.start() # start bump watch threadfor i in range(4): # Draw a right-handes square    move_bump('F',-2,4104)    move_bump('R',-2,2052)running = False