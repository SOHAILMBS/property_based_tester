#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Temporal Logger: Logs the temporal properties of the scenario entities in a csv file.
"""
import numpy as np
import pandas as pd
import time
from property_based_tester.temporal_cache.data_depot import data_logger, world_state_extractor
from property_based_tester.configuration.config import Configuration

if __name__ == '__main__':
    try:
        
        logs_objects = ['Models', 'X-pos','Y-pos','Z-pos','Q-1','Q-2','Q-3','Q-4','Time']
        logs_all = [['------','------','------','------','------','------','------','------ ','------']]
        config = Configuration()
        
        while True:
            logs = world_state_extractor()
            logs_all.extend(logs)

            time.sleep(1)

            df = pd.DataFrame(columns=logs_objects, data=logs_all[1:])
            data_logger(df, config.workspace+'/src/property_based_tester/temporal_cache/logs/test')
            logs_all.extend([['------','------','------','------','------','------','------','------ ','------']])
    finally:
        print('Error in file storage')       