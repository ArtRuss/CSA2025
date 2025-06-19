import random

def get_temperature():
    '''simulates getting the temperature'''
    temperature = random.randint(20,35)
    print("The temperature is: ", temperature)
    return temperature

def cell_stack():
    '''simulates the cell stack of temperatures'''
    cell_stack = [] # initialize empty cell stack
    for i in range(10):
        cell_stack.append(get_temperature)
    return cell_stack


def set_heat(cell_number, heat_state):
    '''turns heat on/off'''
    print("Temperature: ", cell_number)
    if heat_state:
        print("HEAT ON")
    else:
        print("HEAT OFF")

def set_cool(cell_number, cold_state):
    '''turns cold on/off'''
    print("Temperature: ", cell_number)
    if cold_state:
        print("COLD ON")
    else:
        print("COLD OFF")

    