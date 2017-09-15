#!/usr/bin/env python
import rospy
import urllib2
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty, String
import std_srvs
import json
import sys
import os
#sys.path.append('/home/skinhat/catkin_ws/src')
#from pimoroni_sts_pi.srv import *
#response = urllib2.urlopen('http://192.168.1.107/forward')
#html = response.read()

def callback(msg):
    #ip = '192.168.1.107'
    global ip
    #print 'vel'
    #print msg.linear.x
    max_vel=0.065
    max_turn=1.2
    vel = int(100*msg.linear.x/ max_vel)
    turn = int(100*msg.angular.z/ max_turn)
    url=''
    if msg.linear.x>0:
         if msg.linear.x<max_vel:		
         	url='http://'+ip+'/forward?vel='+str(vel)
         else:
         	url='http://'+ip+'/forward'
    elif msg.linear.x<0:
         if msg.linear.x>-max_vel:
         	url='http://'+ip+'/back?vel='+str(vel)
         else:
         	url='http://'+ip+'/back'
    elif msg.angular.z<0:
         if msg.angular.z>-max_turn:
         	url='http://'+ip+'/clockwise?vel='+str(turn)
         else:
         	url='http://'+ip+'/clockwise'
    elif msg.angular.z>0:
         if msg.angular.z<max_turn:
         	url='http://'+ip+'/anti-clockwise?vel='+str(turn)
         else:
         	url='http://'+ip+'/anti-clockwise'
    else:
         url='http://'+ip+'/stop'
    #print 'url'
    #print url
    urllib2.urlopen(url)
'''
def callback_scan(self):
    global ip
    global pubscan
    str= urllib2.urlopen('http://'+ip+'/ultrasonic')
    ret =json.load(str)
    pubscan.publish(ret)
    print repr(ret)
    #return ret


def handle_add_two_ints(req):
    print "Returning " #"%(req.a, req.b, (req.a + req.b))
    return std_srvs.srv.EmptyResponse() #EmptyResponse(req.a + req.b)
'''
if __name__ == '__main__':
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    if len(sys.argv) < 2:
        print("usage: roslaunch pimoroni_sts_pi pimoroni_sts_pi.launch ip_address:=xxx.xxx.xxx.xxx")
    else:
        ip = sys.argv[2]
        rospy.init_node('cmd_vel_listener')#, anonymous=True)

        rospy.Subscriber("/cmd_vel", Twist, callback)

        #s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
        #rospy.Subscriber("/scan", Empty, callback_scan)
        #pubscan = rospy.Publisher("/scanpub",Empty)
        #pubscan = rospy.Publisher("/scanpub", String)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

