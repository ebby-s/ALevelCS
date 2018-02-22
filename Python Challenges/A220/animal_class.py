import random

class Animal():
    """A generic animal"""
    def __init__(self, name, growth_rate, food_need, water_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "New Born"
        self._type = "Generic"
        self._name = name

    def needs(self):
        return {"food need" : self._food_need, "water need" : self._water_need}

    def report(self):
        return {"name":self._name,"type":self._type,"weight":self._weight,"days growing":self._days_growing,"status":self._status}
    
    def _update_status(self):
        if self._weight > 20:
            self._status = "Old"
        elif self._weight > 15:
            self._status = "Mature"
        elif self._weight > 10:
            self._status = "Juvenile"
        elif self._weight > 0:
            self._status = "Young"
        elif self._weight == 0:
            self._status = "New Born"
        
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Enter food value(1-10: "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Invalid value")
        except ValueError:
            print("Invalid value")
    valid = False
    while not valid:
        try:
            water = int(input("Enter water value(1-10: "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Invalid value")
        except ValueError:
            print("Invalid value")
    animal.grow(food,water)

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit program")
    print()
    print("Select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Selected option: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
    return choice

def manage_animal(animal):
    print("Animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Exiting animal management program")

def main():
    new_animal = Animal("Shaun",1,4,3)
    manage_animal(new_animal)

if __name__ == "__main__":
    main()
