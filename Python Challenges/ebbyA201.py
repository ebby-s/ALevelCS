class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def insert(tree,item):
    node = Tree(item)
    last = tree
    while True:
        direction = input("Direction(r/l): ")
        if direction == "r": last = last.right
        elif direction == "l": last = last.left
        else:
            side = input("Side to insert(r/l): ")
            node.right = last.right
            node.left = last.left
            if side == "r":
                last.right = node
                last.left = None
            elif side == "l":
                last.left = node
                last.right = None

def find(tree,item):
    if tree.cargo == item: return True
    if tree.right != None:
        if contains_x(tree.right): return True
    if tree.left != None:
        if contains_x(tree.left): return True
    return False
