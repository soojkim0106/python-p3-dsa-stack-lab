class Stack:

    def __init__(self, items=None, limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit 

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None

    def pop(self):
        return None if self.isEmpty() else self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            raise ValueError('Stack is empty')
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.size() - self.items.index(target)-1
        else:
            return -1
