import random
number = random.uniform(0.1, 9.9)
print(number)



names = ["Marcus","Aiden","Ebby","Vitthal"]
for i in range(1,5):
    chosen = random.choice(names)
    print(chosen)
    choice = input("Do you want to keep this name in the list? y/n")
    if choice == "n":
        names.remove(chosen)