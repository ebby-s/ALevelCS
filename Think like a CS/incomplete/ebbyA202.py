class Node:
    def __init__(self, cargo=None, next_node=None):
        self.cargo = cargo
        self.next  = next_node

    def __str__(self):
        return str(self.cargo)

class linked_list:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self,item,pos=None):
        node = Node(item)
        last = self.head
        if self.head is None: self.head = node
        elif pos is None:
            print("ye")
            while last.next != None:
                print("ye2")
                last = last.next
            last.next = node
        else:
            for i in range(pos):
                last = last.next
            node.next = last.next
            last.next = node
        self.length += 1

    def find(self,element):
        last = self.head
        pos = 0
        while last.next != None:
            if last.cargo == element: return pos
            pos += 1
            last = last.next

    def delete(self,element):
        last = self.head
        while last.next != None:
            if last.next.cargo == element:
                last.next = last.next.next
                self.length -= 1
                return
            last = last.next

    def show(self):
        last = self.head
        while last != None:
            print(last)
            last = last.next
        
