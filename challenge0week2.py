# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 14:07:14 2025

@author: haile
"""


# pls work omg pls work
import time
from francislib import temperature, sounds

# make function for alarm to go off
def check_and_alarm():
    # read the temperature
    temp = temperature.get_temperature()
    
    # if temp 100°C or above make alarm go off???
    if temp >= 100:
        #  alarm on 
        sounds.set_alarm(True)  
        # alarm will go for 5 sec
        bip_durations = [5, 4, 3, 2, 1]  # durations for each bip
        
        
        # iterate thorugh each duraction
        for duration in bip_durations:
            print(f"Beep for {duration} second(s)")
            time.sleep(duration)  # simulate bip duration
            
            
            #  alarm off after one time through
        sounds.set_alarm(False)  
    else:
        
        # alarm automaticaly is  off if temp is less than 100 c
        sounds.set_alarm(False)  

# call function once
check_and_alarm()
