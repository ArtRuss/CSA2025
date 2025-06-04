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

    # alarm will sound 5sec, 4sec, 3sec, 2sec, 1sec...
    for i in range(5) # 0, 1, 2, 3, 4
        time.sleep(5-i)
    
    False