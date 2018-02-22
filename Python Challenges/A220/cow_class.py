from animal_class import *

class Cow(Animal):
    """A Cow"""

    def __init__(self,name):
        super().__init__(name,1,6,6)
        self._type = "Cow"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Young":
                self._weight += self._growth_rate * 1.5
            elif self._status == "Juvenile":
                self._weight += self._growth_rate * 1.25
            elif self._status == "Mature":
                self._weight += self._growth_rate * 2
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

def main():
    new_cow = Cow()
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())

if __name__ == "__main__":
    main()
