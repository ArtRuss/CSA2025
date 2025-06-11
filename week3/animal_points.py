# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 15:16:31 2025

@author: haile
"""

import random
import pandas as pd

random.seed(10)


def generate_animal_data(num_points):
    """
     artificial data points for animal data set 
    """
    data_points = []

    #  possible values for each characteristic
    possible_legs = [0, 1, 2, 3, 4] 
    possible_tail = [0, 1] # 0 for no tail 1 for yes tail
    min_height = 1
    max_height = 500


    for i in range(num_points): # generate points based on user input
        legs = random.choice(possible_legs)
        tail = random.choice(possible_tail)
        height = random.randint(min_height, max_height)
        animal_data = {
            "legs": legs,
            "tail": tail,
            "height": height
        }
        data_points.append(animal_data)
    return data_points


# run function
if __name__ == "__main__":
    # gen 30 pts
    my_artificial_data = generate_animal_data(30)
    # print to user
    for point in my_artificial_data:
        print(point)



# Create data fram from dictionary and print to user
df = pd.DataFrame(my_artificial_data)
print(df.head()) 
