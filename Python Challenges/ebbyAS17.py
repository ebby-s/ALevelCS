import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("green")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)
loop = True
tess.right(180)
tess.forward(300)
tess.right(180)
xs = []

def get_data():
    cx = int(input("Enter data or 'end' to end: "))
    xs.append(cx)
    

for i in range(0,5,1):
    get_data()

for a in xs:
    draw_bar(tess, a)
tess.right(180)
tess.forward(500)
wn.mainloop()
