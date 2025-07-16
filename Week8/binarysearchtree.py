class Node:
    def __init__(self, val):
        self.val = val
    def insert(self, val):
        if val < self.val:
            if hasattr(self, "left_node"):
                self.left_node.insert(val)
            else:
                self.left_node = Node(val)
        else:
            if hasattr(self, "right_node"):
                self.right_node.insert(val)
            else:
                self.right_node = Node(val)
    def in_order(self):
        if hasattr(self, "left_node"):
            self.left_node.in_order()
        print(self.val)
        if hasattr(self, "right_node"):
            self.right_node.in_order()

# Test binary search tree
if __name__ == "__main__":
    root = Node(8)
    root.insert(3)
    root.insert(10)
    root.insert(6)
    root.insert(1)
    root.insert(7)
    root.insert(4)
    root.insert(14)
    root.insert(13)
    root.in_order()