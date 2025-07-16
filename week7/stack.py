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

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def get_size(self):
        node = self.top
        count = 1
        while node.below is not None:
            node = node.below
            count += 1
        return count

if __name__ == "__main__":
    stack = Stack(5)
    stack.push(21)
    stack.push(3)
    stack.push(41)
    stack.push(4)
    print(stack.get_size())
    stack.pop()
    print(stack.peek())

