import time
from francislib import sounds, temperature

temperature = temperature.get_temperature()

while True:
    if temperature >= 100:
        sounds.set_alarm(True)
    else:
        sounds.set_alarm(False)
