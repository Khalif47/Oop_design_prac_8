from Node import Node


class Stack:
    def __init__(self):
        self.top = None

    def is_full(self):
        return False

    def is_empty(self):
        return self.top is None

    def reset(self):
        self.top = None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        try:
            assert not self.is_empty(), "Stack is empty"
            item = self.top.item
            self.top = self.top.next
            return item
        except AssertionError:
            print("")
            return

