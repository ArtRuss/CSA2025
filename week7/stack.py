class Node:
    def __init__(self, value, below):
        self.value = value
        self.below = below

class Stack:
    def __init__(self, init_value=None):
        if init_value is None:
            self.top = None
        else:
            self.top = Node(init_value, None)

    def push(self, value):
        newnode = Node(value, self.top)
        self.top = newnode

    def pop(self):
        if self.top is None:
            raise IndexError("no popping from empty stack!")
        popnode = self.top
        self.top = self.top.below
        return popnode.value

    def peek(self):
        if self.top is None:
            raise IndexError("no peeking on empty stack!")
        return self.top.value

if __name__ == "__main__":
    stack = Stack(5)
    stack.push(21)
    stack.push(41)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.push(4)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
