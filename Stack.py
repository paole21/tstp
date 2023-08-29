
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
print(stack.is_empty())

stack.push("apple")
print(stack.is_empty())

stack.push("orenge")
stack.push("lemon")
stack.push("banana")
print(stack.peek())
print(stack.size())