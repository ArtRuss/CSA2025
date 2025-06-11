# Decision Tree Classifier
# Purpose: categorizes points as true or false based on their values

import random
import math

# TODO: delete later
random.seed(1)

# Functions

def random_points(num, points):
    for i in range(num):
        points.append((random.randint(0, 99), random.randint(0,99), \
                       random.choice([True, False])))

def print_points(points):
    for point in points:
        print(point)

def entropy(points):
    labels = [p[2] for p in points]
    percent_true = sum(labels) / len(labels)
    if percent_true == 0 or percent_true == 1:
        return 0
    return -percent_true * math.log2(percent_true) - \
        (1 - percent_true) * math.log2(1 - percent_true)

def info_gain(parent, left, right):
    cnt = len(parent)
    cnt_left = len(left)
    cnt_right = len(right)
    
    if cnt == 0:
        return 0

    ent_parent = entropy(parent)
    ent_left = entropy(left)
    ent_right = entropy(right)

    ent_weighted = (cnt_left / cnt) * ent_left + \
        (cnt_right / cnt) * ent_right
    
    gain = ent_parent - ent_weighted
    return gain

def best_split(points):
    max_gain = 0
    left_child = []
    right_child = []

    # Checks all possible x value splits
    for x in range(100):
        for point in points:
            if point[0] < x:
                left_child.append(point)
            else:
                right_child.append(point)
        gain = info_gain(points, left_child, right_child)

        # Resets child nodes if gain is not the new maximum
        if gain <= max_gain:
            left_child.clear()
            right_child.clear()

    # Checks all possible y value splits
    for y in range(100):
        for point in points:
            if point[1] < y:
                left_child.append(point)
            else:
                right_child.append(point)
        gain = info_gain(points, left_child, right_child)

        # Resets child nodes if gain is not the new maximum
        if gain <= max_gain:
            left_child.clear()
            right_child.clear()

# Main program
points = []
random_points(20, points)
print_points(points)
print("Entropy of all points: " + str(entropy(points)))