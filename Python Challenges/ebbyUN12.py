Stat1 = 0
Stat2 = 0
Stat3 = 0
Stat4 = 0

import tkinter
window = tkinter.Tk()
window.wm_title("Button Clicker")

def Number1():
    global Stat1
    Stat1 += 1
def Number2():
    global Stat2
    Stat2 += 1
def Number3():
    global Stat3
    Stat3 += 1
def Number4():
    global Stat4
    Stat4 += 1

MyTitle = tkinter.Label(window, text="Click the buttons!!!",font="Helvetica 16 bold")
MyTitle.pack()
MyButton = tkinter.Button(window, text="  1  ", command=Number1)
MyButton.pack()
MyButton2 = tkinter.Button(window, text="  2  ", command=Number2)
MyButton2.pack()
MyButton3 = tkinter.Button(window, text="  3  ", command=Number3)
MyButton3.pack()
MyButton4 = tkinter.Button(window, text="  4  ", command=Number4)
MyButton4.pack()

window.mainloop()

window = tkinter.Tk()
window.wm_title("Button Clicker")

MyTitle2 = tkinter.Label(window, text="Stats:",font="Helvetica 16 bold")
MyTitle2.pack()
MyTitle1 = tkinter.Label(window, text="Button 1:"+str(Stat1),font="Helvetica 16 bold")
MyTitle1.pack()
MyTitle3 = tkinter.Label(window, text="Button 2:"+str(Stat2),font="Helvetica 16 bold")
MyTitle3.pack()
MyTitle4 = tkinter.Label(window, text="Button 3:"+str(Stat3),font="Helvetica 16 bold")
MyTitle4.pack()
MyTitle5 = tkinter.Label(window, text="Button 4:"+str(Stat4),font="Helvetica 16 bold")
MyTitle5.pack()

window.mainloop()
