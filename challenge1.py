def cooking_alarm(measure_temperature):
    
    cooking_alarm = False

    if measure_temperature >= 100:
        cooking_alarm = True
    
    return cooking_alarm

while True:
    water_temperature = float(input("What's the water temperature? "))
    alarm_state = cooking_alarm(water_temperature)

    print(alarm_state)
