import turtle,random

def tree(branchLen,thickness,t):
    t.pensize(thickness)
    if branchLen < 20: t.color("lightgreen")
    else: t.color("brown")
    angle = int(40*random.uniform(0.7,branchLen/75))
    if branchLen > 5:
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen*random.uniform(0.7,branchLen/75),thickness*0.8,t)
        t.left(2*angle)
        tree(branchLen*random.uniform(0.7,branchLen/75),thickness*0.8,t)
        t.right(angle)
        t.penup()
        t.backward(branchLen)
        t.pendown()

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75,3,t)
    myWin.exitonclick()

main()

