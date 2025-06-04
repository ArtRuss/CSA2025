
from francislib import temperature, sounds, time



def cooking_alarm(measure_temperature):
    
    cooking_alarm = False

    if measure_temperature >= 100:
        cooking_alarm = True
    
    return cooking_alarm

while True:

    # get the temperature form francislib 
    water_temperature = temperature.get_temperature()

    # call the built function to say if the alarm should sound (True) or not (False)
    alarm_state = cooking_alarm(water_temperature)

    # if True, it will sound, if False, it wont
    sounds.set_alarm(alarm_state)

    # print test
    print(alarm_state)

    # use time funciton to wait a few seconds to test again
    time.sleep(5)
