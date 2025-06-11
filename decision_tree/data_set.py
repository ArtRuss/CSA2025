import random

random.seed(30)

# create 30 random points for the legs and the tail

x_points = []

for i in range(30):
    legs = random.choice([2, 4])
    tail = random.choice([0, 1])
    class_ = random.choice(["dog", "flamingo", "frog"])
    x_points.append((legs, tail, class_))

# print each point
for i in x_points:
    print(i)

