from gpiozero import MCP3008
import time
import os

station_dial = MCP3008(0)
volume_dial = MCP3008(1)

Magic = "http://tx.whatson.com/icecast.php?i=magic1054.mp3.m3u"
Radio1 = "http://www.listenlive.eu/bbcradio1.m3u"

current_station = Radio1

def change_station(station):
    global current_station
    if station != current_station:
        os.system("killall mplayer")
        os.system("mplayer -playlist " + station + " &")
        current_station = station
        
while True:
    vol = (65 + volume_dial.value * 35)
    os.system("amixer set PCM -- " + str(vol) +"%")
    if station_dial.value >= 0.5:
        station = Magic
        change_station(station)
    elif station_dial.value < 0.5:
        station = Radio1
        change_station(station)
    time.sleep(0.1)
