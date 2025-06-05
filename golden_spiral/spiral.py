#spiral.py
import math

def fib_sequence(n):
    if(n <= 1):
        return n
    return fib_sequence(n-1) + fib_sequence(n-2)

def spiral_length(n):
    length = 0
    for i in range(1, n+1):
        length += fib_sequence(i) * (math.pi/2)
    return length

if __name__ == "__main__":
   n = 5
   print(f"The {n}th number in the fibonacci seequence is {fib_sequence(n)}")
   print(f"The length of the fibonacci seequence of length {n} is {spiral_length(n)}")