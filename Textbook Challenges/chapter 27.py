import re

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def print_tree_inorder(tree):
    if tree is None: return
    if tree.left not in ['+','-','*','/',None]:
        print("(", end=" ")
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)
    if tree.right not in ['+','-','*','/',None]:
        print(")", end=" ")

def create_token_list(expr):
    import re
    token_list = []
    for i in range(len(expr)):
        if expr[i] != ' ':
            try:
                token_list.append(int(expr[i]))
            except:
                token_list.append(expr[i])
    token_list.append('end')
    return token_list

def yes(ques):
    ans = input(ques)
    return ans[0] == "y"

def animal():
    root = Tree("bird")

    while True:
        if not yes("Are you thinking of an animal? "):
            save_tree(root)
            break

        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

def save_tree(tree):
    if tree is None: return
    save_tree(tree.left)
    f.write(tree.cargo + "\n")
    save_tree(tree.right)

f = open("animaldata.txt", "w")
animal()
f.close()
