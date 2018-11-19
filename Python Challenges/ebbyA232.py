import turtle

class Tree:             # Node for building trees
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)
    def __int__(self):
        return int(self.cargo)

def print_tree(tree,pen,pos=(0,-100),level=1):
    if tree is None: return
    pen.penup()
    pen.setpos(pos)
    pen.write(tree.cargo)
    print_tree(tree.left,pen,(pos[0]-50/level,pos[1]-20),level+1)
    print_tree(tree.right,pen,(pos[0]+50/level,pos[1]-20),level+1)
                                                           # v = u + a * t
equation = Tree("=",Tree("s"),Tree("+", Tree("*",Tree("v"),Tree("t")), Tree("*",Tree("*",Tree(-0.5),Tree("a")),Tree("^",Tree("t"),Tree(2))))) # s = vt - 0.5*at^2

print_tree(equation,turtle.Turtle())
