n = int(input())
if n <= 0:
    fib = []
elif n == 1:
    fib = [0]
else:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-2] + fib[i-1])

print(*fib)

length = 0
for r in fib:
    length += r*3.14159*0.5

print(f"Arc Length: {length}")
