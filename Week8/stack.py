class Stack:
    def __init__(self):
        self.list = []
    def is_empty(self):
        return len(self.list) == 0
    def top(self):
        if(self.is_empty()):
            return "Stack is empty"
        return self.list[len(self.list) - 1]
    def push(self, val):
        self.list.append(val)
    def pop(self):
        new_list = []
        val = self.list[len(self.list) - 1]
        for i in range(len(self.list) - 1):
            new_list.append(self.list[i])
        self.list = new_list
        return val
    def get_size(self):
        return len(self.list)

# Test stack class
if __name__ == "__main__":
    test_stack = Stack()
    test_stack.push(1)
    test_stack.push(5)
    print(test_stack.get_size())
    print(test_stack.pop())
    print(test_stack.is_empty())
    print(test_stack.pop())
    print(test_stack.is_empty())
