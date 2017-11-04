#!/usr/bin/python

import shutil
import os

f = open("default.txt", "a+")
f.close()

def default():
    print("Warning: This script modifies Raspbian config files. If you are uncertain as to whether you need this script, please visit https://github.com/RaspberryPicardBox/DisplaySwitcher")
    f = open("default.txt", "w+")
    default_display = str.lower(raw_input("Which display would you like to use as your default? (This is a one time setup) HDMI = H Hyperpixel = P: "))
    if default_display == "h":
        shutil.copyfile("/boot/hdmi-config.txt", "/boot/config.txt")
        f.write("h")
    elif default_display == "p":
        shutil.copyfile("/boot/hyper-config.txt", "/boot/config.txt")
        f.write("p")
    else:
        print("Invalid input.")
        default()
    f.close()

def HDMI():
    shutil.copyfile("/boot/hdmi-config.txt", "/boot/config.txt")

def Hyperpixel():
    shutil.copyfile("/boot/hyper-config.txt", "/boot/config.txt")

def start():
    print(" ")
    print("Please select which display you would like to use.")
    print("Make absolute certain that your Hyperpixel display is connected to your Pi before selecting the Hyperpixel display!")
    print("Type H for HDMI, P for Hyperpixel or C to continue using current display: ")

    pref = str.lower(raw_input("Preference: "))

    if pref == "h":
        HDMI()
        print("HDMI selected. Rebooting Pi.")
        os.system("sudo reboot")
    elif pref == "p":
        Hyperpixel()
        print("Hyperpixel selected. Rebooting Pi.")
        os.system("sudo reboot")
    elif pref == "c":
        print("Continuing...")
        quit()
    else:
        print("Invalid input.")
        start()

f = open("default.txt", "r")
if f.mode == "r":
    start_display = f.read()
else:
    f.close()
    default()

if start_display == "h":
    HDMI()
elif start_display == "p":
    Hyperpixel()
else:
    default()
    
start()

f.close()




           
