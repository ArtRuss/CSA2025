import random

def get_temperature():
    '''simulates getting the temperature'''
    temperature = random.randint(80,150)
    print("The temperature is: ", temperature)
    return temperature

def set_heat(temperature, heat_state):
    '''turns heat on/off'''
    print("Temperature: ", temperature)
    if heat_state:
        print("HEAT ON")
    else:
        print("HEAT OFF")

def set_cold(temperature, cold_state):
    '''turns cold on/off'''
    if cold_state:
        print("COLD ON")
    else:
        print("COLD OFF")

    