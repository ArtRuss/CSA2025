class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self, top=None):

        if not top:
            self.top = top
            self.size = 0
        else:
            self.top = Node(top)
            self.size = 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def get_size(self):
        return self.size

    def peek(self):
        if self.is_empty():
            raise IndexError("No peek empty")
        else:
            return self.top.value

    def push(self, value):
        if self.is_empty():
            self.top = Node(value)
            self.size = 1
        else:
            temp = Node(value)
            temp.next = self.top
            self.top = temp
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            return_val = self.top.value
            self.top = self.top.next # NOTE: Is the popped self.head garbage collected?
            self.size -= 1
            return return_val

stack_1 = Stack()
stack_2 = Stack(3)

print(stack_1.is_empty())
print(stack_2.is_empty())

print(stack_1.get_size())
print(stack_2.get_size())

# print(stack_1.peek())
print(stack_2.peek())

stack_1.push(1)
stack_2.push(2)

print(stack_1.peek())
print(stack_2.peek())

print(stack_1.pop())
print(stack_2.pop())


