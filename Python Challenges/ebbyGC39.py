import random

name = input("Enter your name: ")
insults = ["banana","apple","orange","pear","mango","coconut","tomato"]

print("{0} is a {1}!".format(name,random.choice(insults)))
