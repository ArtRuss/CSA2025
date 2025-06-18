# Decision Tree Classifier (didn't finish)
# https://www.youtube.com/watch?v=ZVR2Way4nwQ

import random
from typing import List

class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value # 0 or 1

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, value={self.value})"

data = [Point(random.uniform(-10, 10), random.uniform(-10, 10), random.randint(0,1)) for _ in range(20)]


class Node:
    def __init__(self, data: List[Point]):
        self.data = data
        self.condition = None # ('x' or 'y', threshold)
        self.left = None # assume left is <=
        self.right = None # assume right is >

    def information_gain(self, left, right):


        return 1
    
    def build_tree(self):
        best_ig = 0
        best_condition = None
        best_left = None
        best_right = None
        for axis in ['x', 'y']:
            for threshold in range (-10, 11):
                if axis == 'x':
                    left = [p for p in self.data if p.x <= threshold]
                    right = [p for p in self.data if p.x > threshold]
                elif axis == 'y':
                    left = [p for p in self.data if p.y <= threshold]
                    right = [p for p in self.data if p.y > threshold]
                ig = self.information_gain(left, right)
                if ig > best_ig:
                    best_condition = (axis, threshold)

        self.condition = best_condition
        self.left = Node(best_left) if best_left else None
        self.right = Node(best_right) if best_right else None


root = Node(data)
