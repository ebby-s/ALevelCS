import random
random.seed = 0

class list_queue:

    def __init__(self):
        self.items = []

    def insert(self,item):
        self.items.append(item)

    def remove(self):
        item = self.items[0]
        del(self.items[0])
        return item

    def is_empty(self):
        return self.items == []


class Node:
    def __init__(self, cargo=None, next_node=None):
        self.cargo = cargo
        self.next  = next_node

    def __int__(self):
        return int(self.cargo)


class linked_queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        elif self.length == 1:
            if int(node) > int(self.head):
                node.next = self.head
                self.head = node
            else:
                self.head.next = node
        else:
            last = self.head
            while last.next != None and int(last.next) > int(node):
                last = last.next
            node.next = last.next
            last.next = node
        self.length += 1

    def remove(self):
        item = int(self.head)
        self.head = self.head.next
        self.length -= 1
        return item

def print_list(list,first = True):
    if first:
        print("[", end = " ")
    if list.next == None:
        print(int(list),"]")
        return
    print(int(list),",",end = " ")
    print_list(list.next,False)

test = linked_queue()
for i in range(10):
    num = random.randint(4,64)
    print(num)
    test.insert(num)



print_list(test.head)
