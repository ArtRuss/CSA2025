# Fuel Cell Control

from arturolib import temperature

numCells = 5

while True:
    for i in range(numCells):
        if temperature.get_temperature(i) < 22:
            temperature.set_heat(i, True)
        if temperature.get_temperature(i) > 28:
            temperature.set_cool(i, True)
        if 24.9 < temperature.get_temperature(i) < 25.1:
            temperature.set_heat(i, False)
            temperature.set_cool(i, False)
    