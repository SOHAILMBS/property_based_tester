#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Engine: Starter module for the revised property-based testing suite.
"""
import subprocess
import rospy

from property_based_tester.configuration.config import Configuration
from property_based_tester.scen_gen.model_placement import world_placement
from property_based_tester.scen_gen.robot_placement import RobotModel

from termcolor import colored

print(colored('Starting Automated Testing Gazebo Simulation', 'green'))

try:
    conf = Configuration()
    robot_node = subprocess.Popen(['roslaunch', conf.rospkg_name, conf.launch_robot_file])

    world_placement()

    # UGVs
    robo = RobotModel(conf.robot_urdf,x=0,y=0,z=0.1,R=0,P=0,Y=0)
    # xARM6
    # robo = RobotModel(conf.robot_urdf,x=-0.2,y=-0.5,z=1.021 ,R=0,P=0,Y=1.571)  
    
    robo.spawn_robot('urdf')

    while not rospy.is_shutdown():
        pass

    robot_node.terminate()
    print(colored('Terminating ros! ~10 sec for Gazebo to shutdown','red'))  

except:
    robot_node.terminate()
    print(colored('Terminating ros!','red'))    