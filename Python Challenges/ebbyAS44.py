

class Door:
    def __init__(self):
        self.state = 0
        self.states = ["CLOSED","OPEN",
                       "CLOSING","OPENING",
                       "STOPPED_WHILE_CLOSING","STOPPED_WHILE_OPENING"]
    def click(self):
        if self.state in [0,4]:
            self.state = 3
        elif self.state in [1,5]:
            self.state = 2
        elif self.state == 2:
            self.state = 4
        elif self.state == 3:
            self.state = 5
        print(self.states[self.state])


    def cycle(self):
        if self.state == 2:
            self.state = 0
        elif self.state == 3:
            self.state = 1
        print(self.states[self.state])

commands = """button_clicked
cycle_complete
button_clicked
button_clicked
button_clicked
button_clicked
button_clicked
cycle_complete""".split("\n")
door = Door()

for command in commands:
    print(command)
    if command == "button_clicked": door.click()
    elif command == "cycle_complete" : door.cycle()
