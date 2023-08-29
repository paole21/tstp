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
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
reverse_list = []

for i in range(1,6):
    stack.push(i)

while not stack.is_empty():
    l = stack.pop()
    reverse_list.append(l)

print(reverse_list)