import turtle
wn = turtle.Screen()
pen = turtle.Turtle()

color=input("""Choose Color:
1. red
2. blue
3. green
: """)
if color=="1":
    wn.bgcolor("Red")
elif color=="2":
    wn.bgcolor("Blue")
else:
    wn.bgcolor("Green")


for i in range(0,5,1):
    pen.forward(350)
    pen.left(144)

pen.right(72)

#for i in range(0,360,1):
    #pen.forward(3.2)
    #pen.left(1)

pen.penup()
pen.right(270)
pen.forward(200)
size=10
for i in range(0,50,1):
    pen.stamp()
    size+=5
    pen.forward(size)
    pen.right(30)


wn.mainloop()
