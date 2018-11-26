class Switch:
    def __init__(self):
        self.state = False
    def toggle(self):
        if self.state == False: self.state = True
        else: self.state = False

switches = [Switch() for x in range(1000)]
in_file = open("switches.txt")
flipped = in_file.readlines()
for i in range(len(flipped)):
    flipped[i] = flipped[i].replace("\n","").split(" ")


for row in flipped:
    for i in range(int(row[0]),int(row[1])+1):
        switches[i].toggle()

on_count = 0
for switch in switches:
    if switch.state:
        on_count += 1

print(on_count)
