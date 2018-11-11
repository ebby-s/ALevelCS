class Node:
    def __init__(self, cargo=None, next_node=None):
        self.cargo = cargo
        self.next  = next_node

    def __str__(self):
        return str(self.cargo)

def print_list(list,first = True):
    if first:
        print("[", end = " ")
    if list == None:
        return
    if list.next == None:
        print(list,"]")
        return
    print(list,",",end = " ")
    print_list(list.next,False)

list = Node(5)
node1 = Node(10)
node2 = Node(15)
node3 = Node(20)
node4 = Node(25)

node3.next = node4
node2.next = node3
node1.next = node2
list.next = node1

print_list(list)
