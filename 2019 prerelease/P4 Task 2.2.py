class Stack:
    def __init__(self):
        self.data = []
    def push(self,data):
        self.data.append(data)
    def pop(self):
        return self.data.pop()

test_stack = Stack()
test_stack.push(5)
test_stack.push(4)
print(test_stack.pop())
