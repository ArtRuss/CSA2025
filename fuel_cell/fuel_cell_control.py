from arturolib import temperature
import time
def manageTemp(measured_temp):
    if(heat_on):
        if(measured_temp >= 25):
            heat_on = False
    elif(cool_on):
        if(measured_temp <= 25):
            cool_on = False
    else: 
        if(measured_temp <= 22):
            heat_on = True
        elif(measured_temp >= 28):
            cool_on = True
if __name__ == "__main__":
    while True:
        measured_temp = temperature.get_temperature()
        manageTemp(measured_temp)
        time.sleep(1)  # Check every 1 second