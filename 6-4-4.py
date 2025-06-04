# Golden Spiral

import math

def GoldenSpiral(max):
    seq = [1, 1]
    for i in range(2, max + 1):
        seq.append(seq[i - 2] + seq[i - 1])
    
    # compute length of spiral
    sum = 0
    for rad in seq:
        sum += math.pi/2 * rad
    return sum