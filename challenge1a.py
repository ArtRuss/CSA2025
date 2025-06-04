heat_on = False
cool_on = False

while True:
    measured_temperature = int(input("What's the temperature? "))

    if measured_temperature < 22:
        heat_on = True
    elif measured_temperature > 28:
        cool_on = True 
    
    if heat_on and measured_temperature >= 25:
        heat_on = False
    if cool_on and measured_temperature <= 25:
        cool_on = False
