# Healthy Cooking v1.1.1

from francislib import temperature
from francislib import sounds
import time

while True:
    if temperature.get_temperature() >= 100:
        for i in range(5, 0, -1):
            sounds.set_alarm(True)
            time.sleep(i)
            sounds.set_alarm(False)