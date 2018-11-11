import random

def game():
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    answer = int(input("What's {0} times {1}? ".format(num1,num2)))
    if num1*num2 == answer:
        return True
    else:
        return False

while True:
    win = game()
    if win:
        continue
    else:
        print("wrong")
        break
