#!/usr/bin/env python

import explorerhat
from time import sleep
from random import randint
#the explorer hat has already some motor functions build in
#invert() - Reverses the direction of forwards for this motor
#forwards( speed ) - Turns the motor "forwards" at speed ( default 100% )
#backwards( speed ) - Turns the motor "backwards" at speed ( default 100% )
#speed(-100 to 100) - Moves the motor at speed, from full backwards to full forwards




#Left Motor is Motor2, Right motor is Motor1
speed = 65


def forwards():
    explorerhat.motor.one.forward(65)
    explorerhat.motor.two.forward(65)
    sleep(0.5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()


def backwards():
    explorerhat.motor.one.backward(65)
    explorerhat.motor.two.backward(65)
    sleep(0.5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def leftTurn():
    explorerhat.motor.one.forward(65)
    explorerhat.motor.two.backward(65)
    sleep(0.5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def rightTurn():
    explorerhat.motor.one.backward(65)
    explorerhat.motor.two.forward(65)
    sleep(0.5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()     

forwards()
sleep(1)
backwards()
sleep(1)
leftTurn()
sleep(1)
rightTurn()
sleep(1)
