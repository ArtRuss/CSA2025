def pem_system(get_temperature)
    
    heat_on = False
    cool_on = False

    if get_temperature < 22:
        heat_on = True
    
    elif get_temperature > 28:
        cool_on = True

    return heat_on, cool_on

    
