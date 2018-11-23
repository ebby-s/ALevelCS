import random

choices = {"rock":"paper","paper":"scissors","scissors":"rock"}

def game():
    choice = random.choice(list(choices.keys()))
    user_choice = input("Enter a choice(rock,paper,scissors): ")
    print("* {0} *".format(choice))
    if user_choice == choices[choice]: print("You win this round")
    elif choice == user_choice: print("It's a tie")
    else: print("What a noob")

while True:
    game()
