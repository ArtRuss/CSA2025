import random

def get_temperature():
   '''simulates getting the temperature'''
   temperature = random.randint(80,150)
   print("The temperature is: ", temperature)
   return temperature

