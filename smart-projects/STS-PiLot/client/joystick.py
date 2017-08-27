# -*- coding: utf-8 -*-
import sys
import pygame
import requests
import signal
import argparse

# Target system default address
address = '192.168.83.4'
port = '5000'

# Define range of buttons to be used to control touch pads.
firstbutton = 1
lastbutton = 4

# Internal variables - should not need editing
xold = 0
yold = 0
reqtimeout = 1
runloop = True

# Handler for a clean shutdown when pressing Ctrl-C
def signal_handler(signal, frame):
    global runloop
    runloop == False
    print(" Shutting down...")
    sys.exit(0)


if __name__ == '__main__':

    # register signal handler for a clean exit
    signal.signal(signal.SIGINT, signal_handler)

    # command line parser
    parser = argparse.ArgumentParser(description='Joystick interface for STS-PiLot')
    parser.add_argument('-a', '--address', default=address, help='Name or IP of STS-PiLot')
    parser.add_argument('-p', '--port', default=port, help='Port of STS-PiLot')
    parser.add_argument('-j', '--joystick', default=0, help='Joystick to use')
    args = parser.parse_args()

    # create URLs
    joystickurl = 'http://' + str(args.address) + ':' + str(args.port) + '/joystick'
    touchpadurl = 'http://' + str(args.address) + ':' + str(args.port) + '/touchpad'

    pygame.init()

    # Initialize the joystick
    pygame.joystick.init()
    try:
        joystick = pygame.joystick.Joystick(int(args.joystick))
    except:
        print('Device ' + str(args.joystick) + ' not found. No. of joysticks: ' + str(pygame.joystick.get_count()))
        sys.exit(0)
    joystick.init()

    numbuttons = joystick.get_numbuttons()
    btnstatus = [0] * numbuttons
    oldstatus = [0] * numbuttons

    # main input --> http request loop
    with requests.Session() as session:
        while runloop == True:
            # EVENT PROCESSING STEP
            for event in pygame.event.get(): # User did something
                # Process joystick event and control robots motors.
                if event.type == pygame.JOYAXISMOTION:
                    x = int(joystick.get_axis(2) * 100)
                    y = int(joystick.get_axis(3) * -100)
                    if x != xold or y != yold:
                        payload = {'x': str(x), 'y': str(y)}
                        try:
                            r = session.get(joystickurl, params=payload, timeout=reqtimeout)
                        except:
                            print("HTTP Request timed out")
                        xold = x
                        yold = y

                # Process button presses and control robots "touch pad" inputs.
                if event.type == pygame.JOYBUTTONUP or event.type == pygame.JOYBUTTONDOWN:
                    for button in range(firstbutton - 1, lastbutton):
                        btnstatus[button] = joystick.get_button(button)
                        if btnstatus[button] == 1 and btnstatus[button] != oldstatus[button]:
                            payload = {'pad': str(button + 1)}
                            try:
                                r = session.get(touchpadurl, params=payload, timeout=reqtimeout)
                            except:
                                print("HTTP Request timed out")
                        oldstatus[button] = btnstatus[button]
