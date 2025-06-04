#healthy_cooking.py
from francislib import temperature
from francislib import sounds
import time

def check_temp(measured_temperature):
    if measured_temperature >= 100:
        for i in range (5, 0, -1):
            sounds.play_sound("alarm", i)
            time.sleep(i) #Sleeps for the duration of the sound
            sounds.set_alarm(alarm_state=False)
            time.sleep(.5)  # Wait for half a second before next sound
    else:
        sounds.set_alarm(alarm_state=False)

if __name__ == "__main__":
    while True:
        measured_temperature = temperature.get_temperature()
        print(f"Measured Temperature: {measured_temperature}°C")  # Debugging output
        check_temp(measured_temperature)
        time.sleep(1)  # Check every 1 seconds