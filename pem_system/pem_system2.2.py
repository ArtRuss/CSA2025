from arturolib import get_temperature, set_heat, set_cool, cell_stack

def pem_system(temperature):
    
    heat_on = False
    cool_on = False

    # if temp bellow 22, turn on heat
    if temperature < 22:
        while temperature < 25: # keep heat on while its below 25
            heat_on = True
    
    # if temp over 28, trun off heat
    elif temperature > 28:
        while temperature > 25: # keep cold on while its above 28
            cool_on = True

    return heat_on, cool_on

stack_temperature = cell_stack()

for i in range(len(stack_temperature)):
    temperature = stack_temperature[i]
    heat_state, cool_state = pem_system(get_temperature)
    set_heat(i, heat_state)
    set_cool(i, cool_state)
    