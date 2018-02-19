import random
number = random.randint(1,100)

while True:
    while True:
        guess = input("Guess a number")
        try:
            value = int(guess)
            break
        except ValueError:
            print("a number")
    if value == number:
            print("well done")
            break
    elif value > number:
            print("Guess is too big")
    elif value< number:
            print("Guess is too small")
