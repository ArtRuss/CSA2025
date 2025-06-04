import arturolib
import array as arr

stack = input("how big is the stack? ")
d = arr.array('i', [0] * int(stack))
for i in range(len(d)): 
    temp = arturolib.getTemperature(i)
    if temp == 25: 
        arturolib.setHeater(i,False)
        arturolib.setFan(i,False)
    elif temp < 22: 
        arturolib.setHeater(i,True)
        arturolib.setFan(i,False) 
    elif temp > 28: 
        arturolib.setHeater(i,False)
        arturolib.setFan(i,True)
    else: 
        pass

    print("done" + str(i) + "temp is " +str(temp) + " heater is " + str(arturolib.getHeater(i)) + " fan is " + str(arturolib.getFan(i)))
    
        
        