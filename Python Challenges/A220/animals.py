from cow_class import *
from sheep_class import *

def display_menu():
    print()
    print("Which animal would you like to get?: ")
    print()
    print("1. Sheep")
    print("2. Cow")
    print()
    print("Select an option from the above menu")

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected:"))
            if choice in (1,2):
                valid_option = True
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
    return choice

def create_animal(name):
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Sheep(name)
    elif choice == 2:
        new_animal = Cow(name)
    return new_animal

def main():
    name = str(input("Enter a name: "))
    new_animal = create_animal(name)
    manage_animal(new_animal)

if __name__ == "__main__":
    main()
