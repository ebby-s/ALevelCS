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


