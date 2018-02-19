import tkinter
import random
names = ["Marcus","Aiden","Ebby","Vitthal"]
window = tkinter.Tk()
def RandomNumber():
     chosen = random.choice(names)
     MyTitle = tkinter.Label(window, text="Random Name Picker",font="Helvetica 16 bold")
     MyTitle.pack()
     MyButton = tkinter.Button(window, text="OK", command=RandomNumber)
     MyButton.pack()
     Name = tkinter.Label(window, text=chosen, font="Helvetica 16 bold")
     Name.pack()
