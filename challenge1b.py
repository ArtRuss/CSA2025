heat_on = False
cool_on = False

def get_temperature(cell_id):
    temp = int(input(f"What's the temperature of cell {cell_id}"))
    return temp
fuel_cells = [231, 433, 483, 695, 234, 112]

while True:
    for cell in fuel_cells:
        measured_temperature = get_temperature(cell)

        if measured_temperature < 22:
            temperature.set_heat(cell, True)
        elif measured_temperature > 28:
            temperature.set_cool(cell, True)
        
        if heat_on and measured_temperature >= 25:
            temperature.set_heat(cell, False)
        if cool_on and measured_temperature <= 25:
            temperature.set_cool(cell, False)
