#!/usr/bin/env python

# http://forums.pimoroni.com/t/night-clock-blinkt-vs-unicorn-phat/3502/14

import time
import unicornhat as unicorn
#period in seconds between steps - multiply by 81 to get total duration
interval = 18
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.clear()
#step1
unicorn.brightness(0.2)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step2
unicorn.brightness(0.21)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step3
unicorn.brightness(0.22)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step4
unicorn.brightness(0.23)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step5
unicorn.brightness(0.24)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step6
unicorn.brightness(0.25)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step7
unicorn.brightness(0.26)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step8
unicorn.brightness(0.27)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step9
unicorn.brightness(0.28)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step10 - start fade to orange
unicorn.brightness(0.29)
unicorn.set_all(255, 0, 0)
unicorn.show()
time.sleep(interval)
#step11
unicorn.brightness(0.3)
unicorn.set_all(255, 15, 0)
unicorn.show()
time.sleep(interval)
#step12
unicorn.brightness(0.31)
unicorn.set_all(255, 30, 0)
unicorn.show()
time.sleep(interval)
#step13
unicorn.brightness(0.32)
unicorn.set_all(255, 45, 0)
unicorn.show()
time.sleep(interval)
#step14
unicorn.brightness(0.33)
unicorn.set_all(255, 60, 0)
unicorn.show()
time.sleep(interval)
#step15
unicorn.brightness(0.34)
unicorn.set_all(255, 75, 0)
unicorn.show()
time.sleep(interval)
#step16
unicorn.brightness(0.35)
unicorn.set_all(255, 90, 0)
unicorn.show()
time.sleep(interval)
#step17 - orange
unicorn.brightness(0.36)
unicorn.set_all(255, 100, 0)
unicorn.show()
time.sleep(interval)
#step18
unicorn.brightness(0.37)
unicorn.set_all(255, 115, 0)
unicorn.show()
time.sleep(interval)
#step19
unicorn.brightness(0.38)
unicorn.set_all(255, 130, 0)
unicorn.show()
time.sleep(interval)
#step20
unicorn.brightness(0.39)
unicorn.set_all(255, 145, 0)
unicorn.show()
time.sleep(interval)
#step21
unicorn.brightness(0.4)
unicorn.set_all(255, 160, 0)
unicorn.show()
time.sleep(interval)
#step22
unicorn.brightness(0.41)
unicorn.set_all(255, 175, 0)
unicorn.show()
time.sleep(interval)
#step23
unicorn.brightness(0.42)
unicorn.set_all(255, 190, 0)
unicorn.show()
time.sleep(interval)
#step24
unicorn.brightness(0.43)
unicorn.set_all(255, 205, 0)
unicorn.show()
time.sleep(interval)
#step25
unicorn.brightness(0.44)
unicorn.set_all(255, 220, 0)
unicorn.show()
time.sleep(interval)
#step26
unicorn.brightness(0.45)
unicorn.set_all(255, 235, 0)
unicorn.show()
time.sleep(interval)
#step27 - yellow
unicorn.brightness(0.46)
unicorn.set_all(255, 255, 0)
unicorn.show()
time.sleep(interval)
#step28
unicorn.brightness(0.47)
unicorn.set_all(205, 255, 0)
unicorn.show()
time.sleep(interval)
#step29
unicorn.brightness(0.48)
unicorn.set_all(155, 255, 0)
unicorn.show()
time.sleep(interval)
#step30
unicorn.brightness(0.49)
unicorn.set_all(105, 255, 0)
unicorn.show()
time.sleep(interval)
#step31
unicorn.brightness(0.5)
unicorn.set_all(55, 255, 0)
unicorn.show()
time.sleep(interval)
#step32 - green
unicorn.brightness(0.51)
unicorn.set_all(0, 255, 0)
unicorn.show()
time.sleep(interval)
#step33
unicorn.brightness(0.52)
unicorn.set_all(0, 255, 18)
unicorn.show()
time.sleep(interval)
#step34
unicorn.brightness(0.53)
unicorn.set_all(0, 255, 36)
unicorn.show()
time.sleep(interval)
#step35
unicorn.brightness(0.54)
unicorn.set_all(0, 255, 54)
unicorn.show()
time.sleep(interval)
#step36
unicorn.brightness(0.55)
unicorn.set_all(0, 255, 72)
unicorn.show()
time.sleep(interval)
#step37
unicorn.brightness(0.56)
unicorn.set_all(0, 255, 90)
unicorn.show()
time.sleep(interval)
#step38
unicorn.brightness(0.57)
unicorn.set_all(0, 255, 108)
unicorn.show()
time.sleep(interval)
#step39
unicorn.brightness(0.58)
unicorn.set_all(0, 255, 126)
unicorn.show()
time.sleep(interval)
#step40
unicorn.brightness(0.59)
unicorn.set_all(0, 255, 144)
unicorn.show()
time.sleep(interval)
#step41
unicorn.brightness(0.6)
unicorn.set_all(0, 255, 162)
unicorn.show()
time.sleep(interval)
#step42
unicorn.brightness(0.61)
unicorn.set_all(0, 255, 180)
unicorn.show()
time.sleep(interval)
#step43
unicorn.brightness(0.62)
unicorn.set_all(0, 255, 198)
unicorn.show()
time.sleep(interval)
#step44
unicorn.brightness(0.63)
unicorn.set_all(0, 255, 216)
unicorn.show()
time.sleep(interval)
#step45
unicorn.brightness(0.64)
unicorn.set_all(0, 255, 234)
unicorn.show()
time.sleep(interval)
#step46
unicorn.brightness(0.65)
unicorn.set_all(0, 255, 252)
unicorn.show()
time.sleep(interval)
#step47 - cyan
unicorn.brightness(0.66)
unicorn.set_all(0, 255, 255)
unicorn.show()
time.sleep(interval)
#step48
unicorn.brightness(0.67)
unicorn.set_all(0, 219, 255)
unicorn.show()
time.sleep(interval)
#step49
unicorn.brightness(0.68)
unicorn.set_all(0, 183, 255)
unicorn.show()
time.sleep(interval)
#step50
unicorn.brightness(0.69)
unicorn.set_all(0, 147, 255)
unicorn.show()
time.sleep(interval)
#step51
unicorn.brightness(0.7)
unicorn.set_all(0, 111, 255)
unicorn.show()
time.sleep(interval)
#step52
unicorn.brightness(0.71)
unicorn.set_all(0, 75, 255)
unicorn.show()
time.sleep(interval)
#step53
unicorn.brightness(0.72)
unicorn.set_all(0, 39, 255)
unicorn.show()
time.sleep(interval)
#step54
unicorn.brightness(0.73)
unicorn.set_all(0, 3, 255)
unicorn.show()
time.sleep(interval)
#step55 - blue
unicorn.brightness(0.74)
unicorn.set_all(0, 0, 255)
unicorn.show()
time.sleep(interval)
#step56
unicorn.brightness(0.75)
unicorn.set_all(22, 22, 255)
unicorn.show()
time.sleep(interval)
#step57
unicorn.brightness(0.76)
unicorn.set_all(44, 44, 255)
unicorn.show()
time.sleep(interval)
#step58
unicorn.brightness(0.77)
unicorn.set_all(66, 66, 255)
unicorn.show()
time.sleep(interval)
#step59
unicorn.brightness(0.78)
unicorn.set_all(88, 88, 255)
unicorn.show()
time.sleep(interval)
#step60
unicorn.brightness(0.79)
unicorn.set_all(110, 110, 255)
unicorn.show()
time.sleep(interval)
#step61
unicorn.brightness(0.8)
unicorn.set_all(132, 132, 255)
unicorn.show()
time.sleep(interval)
#step62
unicorn.brightness(0.81)
unicorn.set_all(154, 154, 255)
unicorn.show()
time.sleep(interval)
#step63
unicorn.brightness(0.82)
unicorn.set_all(176, 176, 255)
unicorn.show()
time.sleep(interval)
#step64
unicorn.brightness(0.83)
unicorn.set_all(198, 198, 255)
unicorn.show()
time.sleep(interval)
#step65
unicorn.brightness(0.84)
unicorn.set_all(220, 220, 255)
unicorn.show()
time.sleep(interval)
#step66
unicorn.brightness(0.85)
unicorn.set_all(242, 242, 255)
unicorn.show()
time.sleep(interval)
#step67 - white
unicorn.brightness(0.86)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step68
unicorn.brightness(0.87)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step69
unicorn.brightness(0.88)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step70
unicorn.brightness(0.89)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step71
unicorn.brightness(0.9)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step72
unicorn.brightness(0.91)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step73
unicorn.brightness(0.92)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step74
unicorn.brightness(0.93)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step75
unicorn.brightness(0.94)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step76
unicorn.brightness(0.95)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step77
unicorn.brightness(0.96)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step78
unicorn.brightness(0.97)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step79
unicorn.brightness(0.98)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step80
unicorn.brightness(0.99)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)
#step81
unicorn.brightness(1)
unicorn.set_all(255, 255, 255)
unicorn.show()
time.sleep(interval)