class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

def add_to_list(list,data):
    if list.next != None:
        add_to_list(list.next,data)
    else: list.next = Node(data)

test_list = Node(5)
add_to_list(test_list,4)
print(test_list.next)

class Stack:
    def __init__(
