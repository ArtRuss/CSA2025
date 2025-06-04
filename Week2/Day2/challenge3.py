import math
# Task 1
def fib(n):
    lst = []
    for i in range(n):
        if i == 0 or i == 1:
            lst.append(int(1))
        else:
            lst.append(int(lst[i-1] + lst[i-2]))
    return lst


# Task 2
def fib_spiral_approx(n):
    lst = fib(n)
    approx = 0
    for num in lst:
        approx += math.pi * num / 4
    return approx


# Test Cases

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))

print(fib_spiral_approx(0))
print(fib_spiral_approx(1))
print(fib_spiral_approx(2))
print(fib_spiral_approx(3))
print(fib_spiral_approx(4))
print(fib_spiral_approx(5))
print(fib_spiral_approx(6))
print(fib_spiral_approx(7))
print(fib_spiral_approx(8))
print(fib_spiral_approx(9))
