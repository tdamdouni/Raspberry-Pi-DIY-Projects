# Pimoroni STS PI ROS Gazebo Simulation

Provides a Gazebo Simulation and ROS wrapper for Pimoroni STS PI.  Allows you to control your Pimoroni STS PI from your PC running ROS using standard Twist.  It also includes a Gazebo simulation of Pimoroni STS PI. You can record movements of a real Pimoroni and then replay in the simulation like in the video below:

[![Youtube sumo](http://forthtemple.com/pimoroni/pimoroniyoutube.jpg)](https://www.youtube.com/watch?v=zDb48-HvZDI) 

The Pimoroni STS PI is a cheap roving robot that uses a Raspberry PI as a controller.

The ultimate aim of the Gazebo simulation of the Pimoroni is to use reinforcement learning to teach the Pimoroni to do tasks like find objects. Once the task has been learnt within the ROS Gazebo framework the results will be used on a real Pimoroni.

# Installation
To make it clear the setup is similar to the diagram below:

[![Youtube Pimoroni](http://forthtemple.com/pimoroni/pimoronisetup250ii.jpg)]

You run ROS Gazebo on a PC which in turns communicates with your Raspberry PI that is on your Pimoroni STS PI.

The steps of installation are:

1. On your Raspberry PI that is on your Pimoroni STS PI install and run app.py on:

https://github.com/sandyjmacdonald/sts_pi_controller

2. On your PC install ROS (eg http://wiki.ros.org/indigo/Installation/Ubuntu if from ubuntu)

3. On your PC install in catkin this source
```
cd ~/catkin_ws/src
git clone https://github.com/forthtemple/ros_pimoroni_sts_pi.git
cd ~/catkin_ws
catkin_make 
```
# Running Gazebo simulation
To use the Pimoron Gazebo simulation in one terminal run the following:
```
roslaunch pimoroni_sts_pi_gazebo myworld.launch
```
On another terminal to control your STS PI in Gazebo via a keyboard use:
```
rosrun pimoroni_sts_pi teleop_twist_keyboard.py
```

# Running Real Pimoroni STS PI
To control a real Pimoroni STS PI via ROS on your PC in one terminal run the following specifying the IP address of your Raspberry PI:
```
roslaunch pimoroni_sts_pi pimoroni_sts_pi.launch ip_address:=192.168.1.107
```
On another terminal to control your STS PI via a keyboard use:
```
rosrun pimoroni_sts_pi teleop_twist_keyboard.py
```

To record a real Pimoroni STS PI movements you can use ROSBAG:
```
rosbag record cmd_vel
```
To play it to your Gazebo Pimoroni STS PI replace xx-xxx-xx with your recorded bag file name. Play this while running the Gazebo simulation
```
rosbag play xx-xxx-xx.bag
```
