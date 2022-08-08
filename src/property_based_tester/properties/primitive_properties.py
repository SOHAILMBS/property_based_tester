#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---------------------------------------------------- 
Primitive properties

Contains spatial and temporal information logged during
navigation.
----------------------------------------------------
Supervisor: Prof. Dr. Nico Hochgeschwender
            Prof. Dr. Paul Ploger
            Sven Schneider 

Author    : Salman Omar Sohail
----------------------------------------------------
Date: July 01, 2022
----------------------------------------------------
"""

import rospy
import numpy as np
from termcolor import colored

from property_based_tester.temporal_cache.data_depot import data_reader
from property_based_tester.configuration.config import Configuration

class PrimitiveProperties():

    def __init__(self) -> None:
        self.config = Configuration()       

    def spatial_temporal_information(self):

        data = data_reader(self.config.workspace+'/src/property_based_tester/temporal_cache/logs/navi')
        data = data.drop(columns=['Unnamed: 0'])

        self.robot_data = data.loc[data['Models'] == self.config.robot_urdf]

# a = PrimitiveProperties()
# a.spatial_information()