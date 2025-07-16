class Queue:
    def __init__(self):
        self.list = []
    def is_empty(self):
        return len(self.list) == 0
    def get_size(self):
        return len(self.list)
    def front(self):
        return self.list[0]
    def enqueue(self, val):
        self.list.append(val)
    def dequeue(self):
        new_list = []
        val = self.list[0]
        for i in range(1, len(self.list)):
            new_list.append(self.list[i])
        self.list = new_list
        return val

# Test queue class
if __name__ == "__main__":
    test_queue = Queue()
    test_queue.enqueue(10)
    test_queue.enqueue(11)
    test_queue.enqueue(12)
    print("size: " + str(test_queue.get_size()))
    print("is empty: " + str(test_queue.is_empty()))
    print("front: " + str(test_queue.front()))
    print("first value: " + str(test_queue.dequeue()))
    print("second value: " + str(test_queue.dequeue()))
    print("third value: " + str(test_queue.dequeue()))
    print("is empty: " + str(test_queue.is_empty()))