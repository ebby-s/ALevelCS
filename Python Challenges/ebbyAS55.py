import turtle, random, sys
resolution = (1200,600)

def stars(resolution,seed=None):
    if seed == None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)
    print("Seed was:", seed)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.ht()
    pen.penup()
    pen.color("white")
    for i in range(50):
        pen.setpos(random.randint(resolution[0]*-0.49,resolution[0]*0.49),random.randint(resolution[1]*-0.49,resolution[1]*0.49))
        pen.stamp()

turtle.setup(resolution[0],resolution[1])
turtle.bgcolor("black")
stars(resolution)
