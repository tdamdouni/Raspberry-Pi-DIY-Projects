__author__ = "Matthew Dunn"

from tkinter import *
from copy import deepcopy
from datetime import datetime
from time import sleep
import displayTime

#set variables
root = Tk() #root window
root.title("Binary Clock GUI") #change window's title
auto=True #sets the auto incremntation to true

currenttime=0 #variable for a list for the current clock time ['00','00','00']
time=0 #variable for a list for the display time ['00','00','00']

currentdisplaytime=StringVar() #create a string variable to use in the UI
currentdisplaytime.set("00:00:00") #set to arbitrary placeholder default value

displaytime=StringVar()#create a string variable to use in the UI
displaytime.set("00:00:00") #set to a copy of the current display time

displayhour=StringVar()#create a string variable to use in the UI
displayhour.set("00") #set to arbitrary placeholder default value
displayminute=StringVar()#create a string variable to use in the UI
displayminute.set("00") #set to arbitrary placeholder default value
displaysecond=StringVar()#create a string variable to use in the UI
displaysecond.set("00") #set to arbitrary placeholder default value


#import images for buttons
playicon=PhotoImage(file="play.gif")
pauseicon=PhotoImage(file="pause.gif")
reset=PhotoImage(file="reset.gif")
uparrow=PhotoImage(file="uparrow.gif")
downarrow=PhotoImage(file="downarrow.gif")


"""
getCurrentTime
    gets the current time from the device and parses it in to a list
    format: ['hh','mm','ss']
returns
    curtime - the list of time items
"""
def getCurrentTime():
    curtime=(str(datetime.now()).split(" ")[1].split(".")[0].split(":"))
    #print(curtime)
    return curtime


"""
setDisplayTimeAsCurrentTime
    sets the display time to a copy of the current clock time
"""
def setDisplayTimeAsCurrentTime():
    global time
    time=deepcopy(currenttime)


"""
updateDisplayTime
    updates the UI display time
    updates the sensehat display time
"""
def updateDisplayTime():
    hour=time[0]
    minute=time[1]
    second=time[2]
    displaytime.set(hour+":"+minute+":"+second)
    displayhour.set(hour)
    displayminute.set(minute)
    displaysecond.set(second)
    displayTime.updateSenseDisplay(time)
    


"""
updateCurrentDisplayTime
    updates the UI current clock display time in the top right-hand corner
"""
def updateCurrentDisplayTime():
    hour=currenttime[0]
    minute=currenttime[1]
    second=currenttime[2]
    currentdisplaytime.set(hour+":"+minute+":"+second)


"""
toInt
    try/catch for converting 
"""
def toInt(numberString):
    try:
        return int(numberString)
    except:
        return 00


"""
addSecond
    converts the seconds (3rd value in time array) in to an integer to perform arithmetic
    adds one to it
    if it goes over 60, calls addMinute() and resets to 00
    converts it back in to a string and stores it back in the 3rd value in the time array
returns
    thistime - the time value given in the parameter
"""
def addSecond(thistime):
    second=toInt(thistime[2])
    if second<59:
        second+=1
    else:
        second=00
        thistime=addMinute(thistime)
    thistime[2]="{0:0>2}".format(second)
    return thistime


"""
addMinute
    converts the minutes (2rd value in time array) in to an integer to perform arithmetic
    adds one to it
    if it goes over 60, calls addHour() and resets to 00
    converts it back in to a string and stores it back in the 2nd value in the time array
returns
    thistime - the time value given in the parameter
"""
def addMinute(thistime):
    minute=toInt(thistime[1])
    if minute<59:
        minute+=1
    else:
        minute=00
        thistime=addHour(thistime)
    thistime[1]="{0:0>2}".format(minute)
    return thistime


"""
addHour
    converts the hours (1st value in time array) in to an integer to perform arithmetic
    adds one to it
    if it goes over 24, resets to 00
    converts it back in to a string and stores it back in the 1st value in the time array
returns
    thistime - the time value given in the parameter
"""
def addHour(thistime):
    hour=toInt(thistime[0])
    if(hour<23):
        hour+=1
    else:
        hour=00
    thistime[0]="{0:0>2}".format(hour)
    return thistime


"""
subtractSecond
    converts the seconds (3rd value in time array) in to an integer to perform arithmetic
    subtracts one from it
    if it goes under 0, calls subtractMinute() and sets it to 59
    converts it back in to a string and stores it back in the 3rd value in the time array
returns
    thistime - the time value given in the parameter
"""
def subtractSecond(thistime):
    second=toInt(thistime[2])
    if second>0:
        second-=1
    else:
        second=59
        thistime=subtractMinute(thistime)
    thistime[2]="{0:0>2}".format(second)
    return thistime


"""
subtractMinute
    converts the minutes (2rd value in time array) in to an integer to perform arithmetic
    subtracts one from it
    if it goes under 0, calls subtractHour() and sets it to 59
    converts it back in to a string and stores it back in the 2nd value in the time array
returns
    thistime - the time value given in the parameter
"""
def subtractMinute(thistime):
    minute=toInt(thistime[1])
    if minute>0:
        minute-=1
    else:
        minute=59
        thistime=subtractHour(thistime)
    thistime[1]="{0:0>2}".format(minute)
    return thistime


"""
subtractHour
    converts the hours (1st value in time array) in to an integer to perform arithmetic
    subtracts one from it
    if it goes under 0, set it to 23
    converts it back in to a string and stores it back in the 1st value in the time array
returns
    thistime - the time value given in the parameter
"""
def subtractHour(thistime):
    hour=toInt(thistime[0])
    if hour>0:
        hour-=1
    else:
        hour=23
    thistime[0]="{0:0>2}".format(hour)
    return thistime


"""
getAutoStatus
    takes a boolean statement and returns the correct icon to use for the auto-increment button
returns
    pauseicon - the address for the pause.gif icon
    playicon - the address for the play.gif icon
"""
def getAutoStatus(var):
    if var:
        return pauseicon
    else:
        return playicon


"""
updateAuto
    gets the auto status and updates the button on the GUI
"""
def updateAuto():
    #print(auto)
    newimage = getAutoStatus(auto)
    toggleAutoButton.config(image=newimage)


"""
resetTime
    gets the current clock time
    sets the display time to the current clock time
    updates the current clock time
    updates the display time
    resumes auto-incrementation
"""
def resetTime():
    global currenttime
    #print("reset")
    currenttime=getCurrentTime()
    setDisplayTimeAsCurrentTime()
    updateCurrentDisplayTime()
    updateDisplayTime()
    play()


"""
toggleAuto
    if auto is false, set to true and vice versa
    update the GUI to match
"""
def toggleAuto():
    global auto
    auto = not auto
    updateAuto()


"""
pause
    set auto to false
    update the GUI to match
"""
def pause():
    global auto
    auto=False
    updateAuto()


"""
play
    set auto to true
    update the GUI to match
"""
def play():
    global auto
    auto=True
    updateAuto()


"""
incrementHours
    add one hour to the display time
    update the GUI to match
    pause auto-incrementation
"""
def incrementHours():
    global time
    #print("ihour", time)
    time=addHour(time)
    updateDisplayTime()
    pause()


"""
decrementHours
    subtract one hour from the display time
    update the GUI to match
    pause auto-incrementation
"""
def decrementHours():
    global time
    #print("dhour",time)
    time=subtractHour(time)
    updateDisplayTime()
    pause()


"""
incrementMinutes
    add one minute to the display time
    update the GUI to match
    pause auto-incrementation
"""
def incrementMinutes():
    global time
    #print("imin", time)
    time=addMinute(time)
    updateDisplayTime()
    pause()


"""
decrementMinutes
    subtract one minute from the display time
    update the GUI to match
    pause auto-incrementation
"""
def decrementMinutes():
    global time
    #print("dmin", time)
    time=subtractMinute(time)
    updateDisplayTime()
    pause()


"""
incrementSeconds
    add one second to the display time
    update the GUI to match
    pause auto-incrementation
"""
def incrementSeconds():
    global time
    #print("isec", time)
    time=addSecond(time)
    updateDisplayTime()
    pause()


"""
decrementSeconds
    subtract one second from the display time
    update the GUI to match
    pause auto-incrementation
"""
def decrementSeconds():
    global time
    #print("dsec",time)
    time=subtractSecond(time)
    updateDisplayTime()
    pause()


"""
keepTime
    the main loop of the program that controls the time flow
"""
def keepTime():
    global time
    global currenttime
    sync=(currenttime==time) #is the display time the same as the current time?
    currenttime=addSecond(currenttime) #add one second to the display time
    if auto: #if auto-increment is on
        if sync: #if the display time was the same as the current clock time
            setDisplayTimeAsCurrentTime() #just set the display time to the current time
        else: #otherwise 
            time=addSecond(time) #add a second to the current display time
        #print("updating")
    updateCurrentDisplayTime() #update the current clock display to match
    updateDisplayTime() #update display time to match
        
    root.after(1000, keepTime) #wait 1 second then call again


#[0,0] label for hour
hourLabel= Label(root, text="Hour", font=("Helvetica", 16))
hourLabel.grid(row=0,column=0)

#[0,1] label for minute
minuteLabel= Label(root, text="Minute", font=("Helvetica", 16))
minuteLabel.grid(row=0,column=1)

#[0,2] label for second
secondLabel= Label(root, text="Second", font=("Helvetica", 16))
secondLabel.grid(row=0,column=2)

#[0,3] label for current clock time
clockLabel = Label(root, text="Time:", font=("Helvetica", 16))
clockLabel.grid(row=0, column=3)

#[0,4] actual current clock time displayed, variable
displayClock = Label(root, textvariable=currentdisplaytime, font=("Helvetica", 16))
displayClock.grid(row=0, column=4)

#[1,0] button to call incrementHours
upArrowHours = Button(root, command=incrementHours)
upArrowHours.config(image=uparrow)
upArrowHours.grid(row=1, column=0)

#[1,1] button to call incrementMinutes
upArrowMinutes = Button(root, command=incrementMinutes)
upArrowMinutes.config(image=uparrow)
upArrowMinutes.grid(row=1, column=1)

#[1,2] button to call incrementSeconds
upArrowSeconds = Button(root, command=incrementSeconds)
upArrowSeconds.config(image=uparrow)
upArrowSeconds.grid(row=1, column=2)

#[2,0] actual display time hours value displayed, variable
displayHour = Label(root, textvariable=displayhour, font=("Helvetica", 48))
displayHour.grid(row=2,column=0)

#[2,1] actual display time minutes value displayed, variable
displayMinute = Label(root, textvariable=displayminute, font=("Helvetica", 48))
displayMinute.grid(row=2,column=1)

#[2,2] actual display time minutes value displayed, variable
displaySecond = Label(root, textvariable=displaysecond, font=("Helvetica", 48))
displaySecond.grid(row=2,column=2)

#[2,3] button to call resetTime
resetButton= Button(root, command=resetTime)
resetButton.config(image=reset)
resetButton.grid(row=2, column=3)

#[2,4] button to pause/play, call toggleAuto
toggleAutoButton = Button(root, command=toggleAuto)
toggleAutoButton.config(image=pauseicon)
toggleAutoButton.grid(row=2, column=4)

#[3,0] button to call decrementHours
downArrowHours = Button(root, command=decrementHours)
downArrowHours.config(image=downarrow)
downArrowHours.grid(row=3, column=0)

#[3,1] button to call decrementMinutes
downArrowMinutes = Button(root, command=decrementMinutes)
downArrowMinutes.config(image=downarrow)
downArrowMinutes.grid(row=3, column=1)

#[3,2] button to call decrementSeconds
downArrowSeconds = Button(root, command=decrementSeconds)
downArrowSeconds.config(image=downarrow)
downArrowSeconds.grid(row=3, column=2)

currenttime=getCurrentTime() #set current time to current device clock time
setDisplayTimeAsCurrentTime() #set display time to current clock time
updateDisplayTime() #update GUI to match
updateCurrentDisplayTime() #update GUI to match

root.after(1000,keepTime) #after 1 second of starting, call keepTime
root.mainloop() #start the GUI
