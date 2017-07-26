import threading
import serial
from time import sleep,strftime
import re
from math import sin,cos,radians,degrees,log,tan,pi,atan2,asin,sqrt

class GPS(object):

    def __init__(self, **kwargs):
        self._log = kwargs.get('log',False)
        self._logfile = kwargs.get('logfile','')
        print(self._log,self._logfile)
        
        try:
            self.datastream = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
        except:
            print("failed to write to serial port")
        self._gpsData = [0,0,0,0,0,0]        
        
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    @property
    def gpsData(self):
        return self._gpsData

    @gpsData.setter
    def gpsData(self,gpsData):
        self._gpsData = gpsData
        
    @property
    def fix(self):
        if int(self._gpsData[5]) == 0:
            return False
        else:
            return True
    
    @property
    def time(self):
        return self.gpsData[0]
    @property
    def lat(self):
        return float(self.gpsData[1])
    @property
    def lon(self):
        return float(self.gpsData[2])
    @property
    def alt(self):
        return float(self.gpsData[3])
    @property
    def sat(self):
        return int(self.gpsData[4])
    
    def distanceToTarget(self,target):
        if self.sat > 4:
            # convert decimal degrees to radians 
            lat1,lon1,lat2,lon2 = map(radians, [self.lat, self.lon, target[0],target[1]])

            # haversine formula 
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))
            r = 6371 # Radius of earth in kilometers. Use 3956 for miles
            return c * r
        else:
            return None

    def checksum(self,sentence):
        sentence = sentence.rstrip('\n').lstrip('$')
        try: 
            data,cs1 = re.split('\*', sentence)
        except ValueError:
            with open("gpsLog",'a') as f:
                pass 
                #print(sentence)
                #f.write(",".join(str(value) for value in [self.time,sentence]+ "\n"))
            
            return False
    
        cs2 = 0
        for c in data:
            cs2 ^= ord(c)

        if int(cs1,16)==cs2:
            return True
        else:
            return False

    def nmeaToDec(self,dm,dir):
        if not dm or dm == '':
            return 0.
        match = re.match(r'^(\d+)(\d\d\.\d+)$', dm) 
        if match:
            d, m = match.groups()
        if dir == "W":
            sign = -1
        else:
            sign = 1
        return (float(d) + float(m) / 60)*sign


    def parseGGA(self,ggaString):
        rawList = ggaString.split(",")
        time = rawList[1][0:2]+":"+rawList[1][2:4]+":"+rawList[1][4:6]
        gpsList = [time,self.nmeaToDec(rawList[2],rawList[3]),self.nmeaToDec(rawList[4],rawList[5]),rawList[9],rawList[7],rawList[6]]
        
        return gpsList

    def logdata(self):
        if self._logfile == '':
            self._logfile = 'gpsLog-%s-%s.csv' % (strftime("%d-%m-%Y"),self.time)
        with open(self._logfile,'a') as f:
            f.write(",".join(str(value) for value in self.gpsData)+ "\n")
            
                                            
    def run(self):
        with open("gpsLog",'a') as f:
            f.write("\n")

        while True:
            # Do something
            byteSentence = self.datastream.readline()
            try:
                nmeaSentence = byteSentence.decode("utf-8")
            except:
                nmeaSentence = byteSentence

            if nmeaSentence[3:6] == "GGA":
                if self.checksum(nmeaSentence):
                    self.gpsData = self.parseGGA(nmeaSentence)
                    if self._log and self.fix:
                        self.logdata()
                    with open("gpsLog",'a') as f:
                        f.write(nmeaSentence + "\n")
                        f.write(str(self.gpsData) + "\n")
                
            sleep(0.1)

if __name__ == '__main__':
    gps = GPS()
    while True:
        print(gps.gpsData)
        sleep(1)
