### A program to find devices connected to a Network ###
### Uses Name of Device as IP address can change  and also MAC is private ###
### Coded by TeCoEd : @dan_aldred

###FINDS ALL DATA###
import nmap
import time
from espeak import espeak
from blinkt import set_clear_on_exit, set_pixel, show, set_brightness

import colorsys
from sys import exit
global scan_time
global scan_time
scan_time = 300 #used to time the pulse light

try:
    import numpy as np
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

global device_status
global Dictionary_Online 
global Dictionary_Offline

###dictionary of announcements###
Dictionary_Online = {"0": "Internet is Online", "1": "Raspberry Pi Online", "2": "Dan's Phone Online", "3": "Elizabeth Phone On line",
                     "4": "Kay's Laptop Online", "5": "James' Mobile Online", "6": "Archies' Phone Online", "7": "James' Laptop Online",}
Dictionary_Offline = {"0": "Hub OFF", "1": "Pi OFF", "2": "Dan's Phone Off", "3": "Elizabeth Phone Off", "4": "Kay's Laptop Offline", "5": "James' Phone Offline", "6": "Archie is Offline", "7": "James' Laptop Offline"}

device_status = [0,0,0,0,0,0,0,0] ## stores the speech status to announce the devices on the Internet

#used for creating the blue pulse
def make_gaussian(fwhm):
        x = np.arange(0, 8, 1, float)
        y = x[:, np.newaxis]
        x0, y0 = 3.5, 3.5
        fwhm = fwhm
        gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
        return gauss

#main program code		
def find_who_is_connected():
    
    device_status2 = [0,0,0,0,0,0,0,0] ###updated status
    global device_status
    global Dictionary_Online 
    global Dictionary_Offline
    global scan_time ###for the pulse###
    
    scan_time = 300
    x=0 ### position of the device in check list, increments to check each position
    
    print ("SPEECH STATUS", device_status)
    final_devices = [] ## stores the found devices
          
    
    nm = nmap.PortScanner()
    data = nm.scan(hosts="192.168.1.1/24", arguments="-sP")
    print (data['scan'])

    text = str(data['scan'])
    text = text.split("{")

    ip_find = 'hostname'

    ###finds the ip addresses working!~
    for i in text:
        if ip_find in i:
            ##find the name of the device### 
            start = i.find("hostname")
            end = i.find(".default")
            final = i[start+12:end]
            final_devices.append(final)
         
    final_devices = str(final_devices)
    print (final_devices)

    ###Finds the position of the names of the devices, if it cannot find them ###
    ###then value is -1, so checks for a value that is not -1 ###

    ################ INTERNET #######################################
    ###0#############################################################
    if final_devices.find("BrightBox.ee") != -1:
        print ("Hub Found")
        set_pixel(0,255,255,255)
        show()
        if device_status2[0] == 0:    #check that the status is 0 and then update to 1
            device_status2[0] = 1
        else:
            pass
        
    else: ####IF DOWN THEN IT WILL FAIL SO NEED A FLASHING LIGHT!!
        set_pixel(0,0,0,0)
        show()
        print ("INTERNET CONNECTION DOWN")
        if device_status2[0] == 1:
            device_status2[0] = 0
        else:
            pass 
    ######################## PI############################
    ###1###################################################
    if final_devices.find("raspberrypi") != -1:
        print ("Pi Found")
        set_pixel(1,255,150,0)
        show()
        if device_status2[1] == 0:    #check that the status is 0 and then update to 1
            device_status2[1] = 1
        else:
            pass
    else:
        set_pixel(1,0,0,0)
        show()
        if device_status2[1] == 1:
            device_status2[1] = 0
        else:
            pass 

    ################### MY PHONE ######################################### 
    ###2##################################################################
    if final_devices.find("android-22340-fdfddef45fdgss") != -1:
        print ("Droid Found")
        set_pixel(2,0,255,0)
        show()
        if device_status2[2] == 0:    #check that the status is 0 and then update to 1
            device_status2[2] = 1
        else:
            pass
    else:
        set_pixel(2,0,0,0)
        show()
        if device_status2[2] == 1:
            device_status2[2] = 0
        else:
            pass    

    ############### BUPHA IPHONE #############
    ###3#####################################
    if final_devices.find("xs-iPhone") != -1:
        print ("Bupha Phone")
        set_pixel(3,255,80,203)
        show()
        if device_status2[3] == 0:    #check that the status is 0 and then update to 1
            device_status2[3] = 1
        else:
            pass
    else:
        set_pixel(3,0,0,0)
        show()
        if device_status2[3] == 1:
            device_status2[3] = 0
        else:
            pass 

    ####################### kAY lAP TOP#####################
    ## 4 ###################################################
    if final_devices.find("KayLapDog") != -1:
        print ("Kay Lap Top")
        set_pixel(4,255,0,0)
        show()
        if device_status2[4] == 0:    #check that the status is 0 and then update to 1
            device_status2[4] = 1
        else:
            pass
    else:
        set_pixel(4,0,0,0)
        show()
        if device_status2[4] == 1:
            device_status2[4] = 0
        else:
            pass 

    ########### James Mobile ######################
    ## 5 ##########################################
    if final_devices.find("James") != -1:
        print ("James Mobile")
        set_pixel(5,0,0,255)
        show()
        if device_status2[5] == 0:    #check that the status is 0 and then update to 1
            device_status2[5] = 1
        else:
            pass
    else:
        set_pixel(5,0,0,0)
        show()
        if device_status2[5] == 1:
            device_status2[5] = 0
        else:
            pass 

        
    # 6 ####archie phone######
    ##########################
        
    if final_devices.find("Archies-iPhone" or "Archies") != -1:
        print ("Archies Phone")
        set_pixel(6,128,0,128)
        show()
        #time.sleep(2)

        if device_status2[6] == 0:    #check that the status is 0 and then update to 1
            device_status2[6] = 1
        else:
            pass
    else:
        set_pixel(6,0,0,0)
        show()

        if device_status2[6] == 1:
            device_status2[6] = 0
        else:
            pass 

    ########JAMES#######
    if final_devices.find("James-PC") != -1:
        print ("James' Laptop")
        set_pixel(7,128,255,128)
        show()
        if device_status2[7] == 0:    #check that the status is 0 and then update to 1
            device_status2[7] = 1
        else:
            pass
    else:
        set_pixel(6,0,0,0)
        show()
        if device_status2[7] == 1:
            device_status2[7] = 0
        else:
            pass 

    print ("device status ", device_status)
    print ("device status 2", device_status2)
    print ("")
    time.sleep(5)

    ########### Find the changes and respond with announcements###

    for i in device_status2:
        if i == device_status[x]:
            print (i)
            print ("same")
            x = x + 1
            
        elif i != device_status[x]:
            print (i)
            print (type(i))
            print ("change")
            
            print ("Number", x, "changed")
            
            x = str(x)
            ####check for changes and pull out voice announcement#####
            if i == 0:
                #print ("went off")
                print (Dictionary_Offline[x])
                espeak.synth(Dictionary_Offline[x]) ###looks up key in dictionary and returns entry, reads it out
                time.sleep(1.5)
            elif i == 1:
                #print ("Went on")
                print (Dictionary_Online[x])
                espeak.synth(Dictionary_Online[x]) ###looks up key in dictionary and returns entry, reads it out
                time.sleep(1.5)
            x = int(x)
            x = x + 1

    device_status = device_status2
            
    print (device_status)
    print (device_status2)
      
    ###Pulse### from Pimoroni Example

    while scan_time > 0:
        for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
            fwhm = 5.0/z
            gauss = make_gaussian(fwhm)
            start = time.time()
            y = 4
            for x in range(8):
                h = 0.5
                s = 1.0
                v = gauss[x, y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r, g, b = [int(255.0 * i) for i in rgb]
                set_pixel(x, r, g, b)
            show()
            end = time.time()
            t = end - start
            if t < 0.04:
                time.sleep(0.04 - t)
            scan_time = scan_time - 1
            print (scan_time)
            scan_time = scan_time - 1

    
    
while True:
    find_who_is_connected()      
        

    
    
