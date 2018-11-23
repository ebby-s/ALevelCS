import random

def game(mode):
    question = random.randint(0,100)
    if mode == "bin": ans = "{0:b}".format(int(question))
    else: ans = "{0:x}".format(int(question))
    user_ans = str(input("Enter the {0} value for {1}: ".format(mode,question)))
    if user_ans == ans: return True
    else: return ans

mode = input("Choose a mode(bin/hex): ")

while True:
    print(game(mode))
