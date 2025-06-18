import time
from francislib import sounds, temperature

temperature = temperature.get_temperature()

while True:
    if temperature >= 100:
        for i in range(5,0,-1):
            sounds.set_alarm(True)
            time.sleep(i)
            sounds.set_alarm(False)
            time.sleep(1)
    sounds.set_alarm(False)
