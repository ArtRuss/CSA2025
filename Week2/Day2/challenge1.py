#1.1
def temperature_control():
    while True:
        if get_temperature() < 22.:
            while get_temperature() < 25.:
                set_heat(True)
                set_cool(False)
        else if get_temperature > 28.0:
            while get_temperature() > 25.0:
                set_cool(True)
                set_heat(False)
        else:
            set_heat(False)
            set_cool(False)
# 2.0
def (fuel_cells: int):
    while True:
        for i in range(fuel_cells): # How many fuel cells are there
            if get_temperature(i) < 22.0:
                while get_temperature(i) < 25.0:
                    set_heat(i, True)
                    set_cool(i, False)
        else if get_temperature(i) > 28.0:
            while get_temperature(i) > 25.0:
                set_cool(i, True)
                set_heat(i, False)
        else:
            set_heat(i, False)
            set_cool(i, False)
