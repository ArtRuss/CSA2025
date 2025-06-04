def system(measured_temperature):


    while True: #so it is always checking
        
        if measured_temperature < 22:
            heat_on = True
            while measured_temperature < 25:
                heat_on = True
            heat_on = False

        elif measured_temperature > 28:
            cool_on = True
            while measured_temperature > 25:
                cool_on = True
            cool_on = False
