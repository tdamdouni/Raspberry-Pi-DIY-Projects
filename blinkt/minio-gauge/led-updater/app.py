from blinkt import set_all, set_clear_on_exit, show

import redis
import time

def paint(client):
    pulseVal = client.get("event_pulse")
    if(pulseVal == None or pulseVal == "" or pulseVal == 0):
        set_all(0,0,0)
        show()
        return

    pulse = int(pulseVal)
    if(pulse >= 400):
        set_all(0, 0, 255)
    elif(pulse >= 200):
        set_all(255,0,0)
    elif(pulse >= 100):
        set_all(0,255,0)
    elif(pulse >= 0):
        set_all(0,155,0)
    show()

if(__name__=="__main__"):
    host = "redis"
    refresh = 0.2
    redisClient = redis.StrictRedis(host)
    set_all(0,0,0)
    show()

    while(True):
        paint(redisClient)
        time.sleep(refresh)

