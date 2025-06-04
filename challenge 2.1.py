def pem_system(get_temperature)
    
    heat_on = False
    cool_on = False

    # if temp bellow 22, turn on heat
    if get_temperature < 22:
        while get_temperature < 25: # keep heat on while its below 25
            heat_on = True
    
    # if temp over 28, trun off heat
    elif get_temperature > 28:
        while get_temperature > 25: # keep cold on while its above 28
            cool_on = True

    return heat_on, cool_on
