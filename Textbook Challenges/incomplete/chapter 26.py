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

    def __str__(self):

class linked_queue:

    def __init__(self):
        self.items = None

    def insert(self,item,node=None,first=True):
        if first:
            node = self.items
            if node <= item:
                item.next = node
                self.items = item
                return
            self.insert(item,node)
        if node <= item:
                item.next = node
                self.items = item
                return
            self.insert(item,node)
        

    def remove(self):
        item = str(self.items)
        self.items = self.items.next
        return str(item)
