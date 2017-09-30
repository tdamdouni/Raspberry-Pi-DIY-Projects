import requests
import json
from Adafruit_IO import Client

file = open('/home/pi/Pi-Web-Status-Display/weatherapikey.txt', 'r')

weatherapikey = file.readline().replace("\n", '')

file.close()

def main():
    print 'main'
    
    #response = requests.get(requestURL)
    
    #return response.json()['main']['temp']-273.15
    
def local(cityid):
    
    requestURL = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(cityid) + '&APPID=' + weatherapikey
    
    response = requests.get(requestURL)
    
    return response.json()['main']['temp']-273.15
    
def room(apikey, *feeds):
    
    temp = []
    
    aio = Client(apikey)
    
    for feed in feeds:
        iotemp = aio.receive(feed)
        temp.append(float(iotemp.value))
        
    roomtemp = sum(temp)/len(temp)
    return roomtemp
