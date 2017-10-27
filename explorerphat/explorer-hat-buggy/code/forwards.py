import explorerhat
from time import sleep

explorerhat.motor.one.forward(100)
explorerhat.motor.two.forward(100)

sleep(2)

explorerhat.motor.one.stop()
explorerhat.motor.two.stop()
