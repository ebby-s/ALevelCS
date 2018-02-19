import turtle
import math
import tkinter
size=0
size2=0
a=turtle.Turtle()

def square():
    global size
    global size2
    size=int(input("Line size: "))
    for i in range(0,4,1):
        a.forward(size)
        a.right(90)

def rect():
    global size
    global size2
    size=int(input("First line size: "))
    size2=int(input("Second line size: "))
    for i in range(0,2,1):
        a.forward(size)
        a.right(90)
        a.forward(size2)
        a.right(90)

def circle():
    global size
    global size2
    size=int(input("Radius: "))
    a.penup()
    a.forward(size)
    a.right(90)
    a.pendown()
    size2=2*math.pi*size/360
    for i in range(0,360,1):
        a.forward(size2)
        a.right(1)
    a.penup()
    a.right(90)
    a.forward(size)
    a.right(180)
    a.pendown()

def regular_polygon():
    global size
    global size2
    sides=int(input("How many sides?: "))
    
