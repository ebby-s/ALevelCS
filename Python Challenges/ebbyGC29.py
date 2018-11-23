import random

choices = ["10/10 student","good student","needs improvement","unsatisfactory performance","needs to improve attendance","good performance in the last test","needs to practice more","lots of room for improvement"]
length = int(input("How many students? "))

comments = []
for i in range(length):
    comments.append(random.choice(choices))
print(comments)
