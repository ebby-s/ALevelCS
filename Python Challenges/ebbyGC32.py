import random

def computer_choice():
    return random.choice([True,False])

def user_choice():
    choice = input("Do you confess(y/n)? ")
    if choice == "y": return True
    else: return False

def check_rematch():
    choice = input("Do you want to try again(y/n)? ")
    if choice == "y": return True
    else: return False

def compare(choice1,choice2):
    if choice1 and choice2:
        return 5
    elif (not choice1) and choice2:
        return 0
    elif choice1 and (not choice2):
        return 20
    elif not (choice1 and choice2):
        return 1

while True:
    user = user_choice()
    computer = computer_choice()
    time = compare(computer,user)
    print("You will be in prison for {0} years.".format(time))
    rematch = check_rematch()
    if rematch:
        continue
    else:
        break
