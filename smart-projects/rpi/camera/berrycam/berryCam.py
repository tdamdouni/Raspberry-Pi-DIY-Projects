#!/usr/bin/env python
#
#  BerryCam.py
#  BerryCam - Raspberry Pi Camera Controller for use with iOS devices
#
#  Created by James Moore on 22/05/2013.
#  Copyright (c) 2013 Fotosyn. All rights reserved.
#
#  Raspberry Pi is a trademark of the Raspberry Pi Foundation.
#  IOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used by Apple Inc. under license.

import SimpleHTTPServer, SocketServer
import urlparse
import os

PORT = 8000 # CHange this if you wish to listen on a different port

class BerryCamHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):

   def do_GET(self):
       
       # Parse query data
       parsedParams = urlparse.urlparse(self.path)
       queryParsed = urlparse.parse_qs(parsedParams.query)

       # Add 'berrycam' prefix to URL to perform query
       if parsedParams.path == "/berrycam":
          
          awb = "'" + queryParsed['awb'][0] + "'" # Set AWB mode
          mm = "'" + queryParsed['mm'][0] + "'" # Set metering mode
          ev = queryParsed['ev'][0] # Set EV compensation
          ex = "'" + queryParsed['ex'][0] + "'" # Set exposure mode
          sh = queryParsed['sh'][0] #  Set image sharpness 
          br = queryParsed['br'][0] # Set image brightness
          co = queryParsed['co'][0] # Set image contrast
          sa = queryParsed['sa'][0] # Set image saturation
          #iso = queryParsed['iso'][0] #  Set capture ISO - NOT YET IMPLEMENTED        
          ifx = "'" + queryParsed['ifx'][0] + "'" # Set image effect
          #cfx = "'" + queryParsed['cfx'][0] + "'" # Set colour effect - NOT YET IMPLEMENTED IN BERRYCAM
          #rot = queryParsed['rot'][0] # Set image rotation - NOT YET IMPLEMENTED IN BERRYCAM
          filequality = queryParsed['fquality'][0]
          filewidth = queryParsed['fwidth'][0]
          fileheight = queryParsed['fheight'][0]
          filefolder = queryParsed['ffolder'][0]
          fileseq = queryParsed['fseq'][0]
          hflip = queryParsed['hf'][0]
          #exifmake = queryParsed['exifmake'][0]
          
          #filewidth = 2592 #- ((2592/4)*filesize) # Take the values passed, divide by 4 and multiply to get new size
          #fileheight = 1944 #- ((1944/4)*filesize) # Take the values passed, divide by 4 and multiply to get new size
          
          #Exposure mode options :
          #off,auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks
 
          #AWB mode options :
          #off,auto,sun,cloud,shade,tungsten,fluorescent,incandescent,flash,horizon
 
          #Image Effect mode options :
          #none,negative,solarise,sketch,denoise,emboss,oilpaint,hatch,gpen,pastel,watercolour,film,blur,saturation,colourswap,washedout,posterise,colourpoint,colourbalance,cartoon
 
          #Metering Mode options :
          #average,spot,backlit,matrix
          
          directory = 'berrycam/' + str(filefolder)
          if not os.path.exists(directory):
              os.makedirs(directory)

          # Build up a raspistill command line string
          command = "raspistill -v" # Initiate command for Raspicam
          command += " -awb " +   str(awb) # Define WB
          command += " -mm " +   str(mm) # Define Metering Mode
          command += " -ev " + str(ev) # Define the Exposure Adjustment
          command += " -ex " +   str(ex) # Define Exposure Mode
          command += " -sh " + str(sh) # Define Image Sharpness
          command += " -br " + str(br) # Define Image Brightness
          command += " -co " + str(co) # Define Image Contrast
          command += " -sa " + str(sa) # Define Image Saturation
          #command += " -ISO " + str(iso) # Define Image ISO - NOT YET IMPLEMENTED          
          command += " -ifx " +   str(ifx) # Define Image Effect
          #command += " -cfx " +   str(cfx) # Define Colour Effect - NOT YET IMPLEMENTED IN BERRYCAM
          #command += " -rot " +   str(rot) # Define Image Rotation - NOT YET IMPLEMENTED IN BERRYCAM
          command += " -q " + str(filequality) # Define Image Quality
          command += " -w " + str(filewidth) # Define output image width
          command += " -h " + str(fileheight) # Define output image height
          #command += " -o /berrycam/" + str(filefolder) + "/IMG-" + str(fileseq) +".jpg" 
          command += " -o berrycam/" + str(filefolder) + "/IMG-" + str(fileseq) +".jpg" 
          #command += " -x IFD1.Make=" + str(exifmake)  #Define Make for ESIF Data 'Raspberry Pi'
          
          if hflip == "1":
              command += " -hf "
          else:
              command += ""
                 
          
          os.system(command)
          self.processRequest(queryParsed)
          
       else:
          # Default to serve up a local file 
          SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);

   def processRequest(self, query):

       self.send_response(200)
       
       

httpd = SocketServer.TCPServer(("", PORT), BerryCamHandler)

print "B E R R Y C A M -- Listening on port", PORT
print "Please ensure your BerryCam App is installed and running on your iOS Device"

httpd.serve_forever()
