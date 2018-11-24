

class Overhead:
    def __init__(self,name,cost,fractions):
        self.name = name
        self.fractions = [fraction*cost for fraction in fractions]
        self.total = cost

    def show(self):
        layout = "{0:>32}{1:>32}"
        print(layout.format(self.name,self.fractions))

length = int(input("How many overheads would you like to enter? "))
overheads = []
while len(overheads)<length: overheads.append(Overhead(input("Enter name of overhead: "),float(input("Enter cost of overhead: ")),[float(x) for x in input("Enter fractions: ").split()]))

costs = [float(x) for x in input("Enter direct costs: ").split()]
for overhead in overheads:
    for i,cost in enumerate(overhead.fractions):
        costs[i] += cost

print(costs)
