import turtle
import random

def walk(steps):
    pen = turtle.Turtle()
    for i in range(steps):
        pen.right(random.randint(-360,360))
        pen.forward(100)
    
