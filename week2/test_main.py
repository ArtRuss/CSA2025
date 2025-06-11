# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 14:40:20 2025

@author: haile
"""

# main.py

import time
from temperature import get_temperature
from alarm import set_alarm

def check_and_alarm():
    """
    This script monitors temperature.
    & triggers alarm with countdown if temperature is too high.
    """
    while True:
        temp = get_temperature()
        print(f"Current Temperature: {temp}")

        if temp >= 100:
            for i in range(5, -1, -1):
                set_alarm(True)
                time.sleep(i)
                set_alarm(False)
                time.sleep(1)
        else:
            set_alarm(False)

        time.sleep(1)

def main():
    check_and_alarm()

if __name__ == '__main__':
    main()
