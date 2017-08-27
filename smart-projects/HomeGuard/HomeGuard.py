#!/usr/bin/env python

import os
from subprocess import check_output
import subprocess

homeDir = "/home/pi"
sensorDir = "/home/pi/Sensors"
emailDir = "/home/pi/Email"
cameraDir = "/home/pi/Camera"

snifferProcName = "RFSniffer"
sensorOutputFile = "sniff"

sensorAlertCodes = {'5707088': 'Door Open', '5592405': 'Motion 1', '16752505': 'Motion 2'}

def checkSensors():
   os.chdir(sensorDir)
   with open(sensorOutputFile) as f:
      content = f.readlines()
   content = [x.strip() for x in content] 

   sensors = set()
   for i in content:
      i = i.replace("Received ", "")
      sensors.add(i)
   return sensors

def clearSensorData():
   os.chdir(sensorDir)
   os.system("cat /dev/null > %s" % sensorOutputFile)

def checkRFSniffer():
   try:
      # Everything is good ie. Sniffer process running
      pid = check_output(["pidof", snifferProcName])
   except subprocess.CalledProcessError:
      # Sniffer process has died
      os.chdir(sensorDir)
      subprocess.Popen(["nohup","./start.sh"])
      
def sendAlert(subject):
   os.chdir(emailDir)
   os.system("./sendmail.py \"%s\"" % subject)

def formatAlertSubject(sensorData):
   subject = ""
   for code, text in sensorAlertCodes.items():
      if (code in sensorData):
         subject = subject + text + "," 
   print "Subj: %s" % subject
   return subject  
   
def takePicture():
   os.chdir(cameraDir)
   os.system("./capture.sh")

if __name__ == '__main__':
   checkRFSniffer()
   s = checkSensors()
   print s
   if len(s) > 0:
      takePicture()
      sendAlert("[Home Guard] %s" % formatAlertSubject(s))
   clearSensorData()
