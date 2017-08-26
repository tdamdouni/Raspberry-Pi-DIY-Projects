__author__ = "Nathan Evans"

from sense_hat import SenseHat
from datetime import datetime
from time import sleep

sense = SenseHat()

colors={
'white' : (255,255,255),
'red' : (255,0,0),
'orange' : (255, 125, 0),
'yellow' : (255,255,0),
'green' : (0,255,0),
'blue' : (0, 0, 255),
'purple' : (125, 0, 255)
}
color = colors['blue']

"""
getTime

get the current time and format it appropriately 
"""
def getTime():
    return str(datetime.now()).split(" ")[1].split(".")[0].split(":")

"""
getOnes

Returns the string representation of the ones digit of a number in binary
    ex) getOnes(9 -> 1001)

num - the number to convert
"""
def getOnes(num):
    strNum = str(num)
    return '{0:04b}'.format(int(strNum[len(strNum)-1]))


"""
getTens

Returns the string representation of the tens digit of a number <=79 in binary
    ex) getTens(79 -> 111)

num - the number to convert
"""
def getTens(num):
    strNum = str(num)
    if(int(num) < 10):
        strNum = "0"
    return '{0:03b}'.format(int(strNum[len(strNum)-2]))


"""
setHours

Sets the pixels for the hour

hh - string representation of the hour to be set

"""
def setHours(hh=0):
    #hh 10s place
    setTens(hh,0)

    #hh 1s place
    setOnes(hh, 1)


"""
setMinutes

Sets the pixels for the minute

mm - string representation of the minute to be set

"""
def setMinutes(mm=0):
    #mm 10s place
    setTens(mm, 3)

    #mm 1s place
    setOnes(mm, 4)


"""
setSeconds

Sets the pixels for the second

ss - string representation of the second to be set

"""
def setSeconds(ss=0):
    #ss 10s place
    setTens(ss,6)
    
    #ss 1s place
    setOnes(ss, 7)


"""
setOnes

Sets the appropriate pixels for the ones column of the number entered

num - string representation of the number to be set

pixelColumn - the column value of the pixels used to represent the ones place
    seconds -> 7, minutes -> 4, hours -> 1
"""
def setOnes(num="",pixelColumn=0):
    oneString = getOnes(num)
    for i in range(4):
        if(oneString[i] == "1"):
            sense.set_pixel(pixelColumn, 4+i, color)


"""
setTens

Sets the appropriate pixels for the ones column of the number entered

num - string representation of the number to be set

pixelColumn - the column value of the pixels used to represent the ones place
    seconds -> 6, minutes -> 3, hours -> 0
"""
def setTens(num="", pixelColumn=0):
    tenString = getTens(num)
    for i in range(3):
        if(tenString[i] == "1"):
            sense.set_pixel(pixelColumn,5+i, color)


"""
updateSenseDisplay
"""
def updateSenseDisplay(time):
    sense.clear()
    x = 0
    while x < 8:
        sense.set_pixel(2,x,colors["white"])
        sense.set_pixel(5,x,colors["white"])
        x+=1
    setHours(time[0])
    setMinutes(time[1])
    setSeconds(time[2])
