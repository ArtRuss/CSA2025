x = 1
def my_function():
    global x
    x = 10
def another_function():
    global x
    x += 1

if __name__ == "__main__":
    print(x)
    my_function()
    print(x)
    another_function()
    print(x)
    