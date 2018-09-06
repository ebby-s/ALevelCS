import turtle

def koch(t, order, size,first=False):
    t.speed(100)
    t.ht()
    if first:
        angles = [-120, -120, 0]
    else:
        angles = [60, -120, 60, 0]
    if order == 0:
        t.forward(size)
    else:
        for angle in angles:
            koch(t, order-1, size/3)
            t.left(angle)

#koch(turtle.Turtle(),5,512,True)

def tl_fractal(t,order,size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [-85,170,-85,0]:
            tl_fractal(t, order-1, size/3)
            t.left(angle)

#tl_fractal(turtle.Turtle(),3,400)

def tl_square(t,order,size,tear,first=False):
    t.speed(100)
    t.ht()
    if first:
        angles = [-90, -90, -90, 0]
    else:
        angles = [-90+0.5*tear,180-tear,-90+0.5*tear,0]
    if order == 0:
        t.forward(size)
    else:
        for angle in angles:
            tl_square(t, order-1, size/3,tear)
            t.left(angle)

#tl_square(turtle.Turtle(),5,2000,10,True)

def triangle(t,order,size,color=-1,first = False):
    global current
    t.penup()
    colors = ['red','blue','green']
    if first:
        current = 0
        t.color(colors[current])
    for i in range(3):
        if order == 0:
            t.pendown()
            t.forward(size)
            t.left(120)
            t.penup()
        else:
            if color == 0:
                current += 1
                if current > 2:
                    current = 0
                t.color(colors[current])
            triangle(t,order-1,size/2,color-1)
            t.forward(size)
            t.left(120)

#triangle(turtle.Turtle(),2,300,1,True)

def recursive_min(xs):
    minx = None
    first = True
    for i in xs:
        if type(i) == type([]):
            val = recursive_min(i)
        else:
            val = i

        if first or val < minx:
            minx = val
            first = False
    return minx

def count(target, xs):
    counter = 0
    for i in xs:
        if type(i) == type([]):
            counter += count(target,i)
        else:
            if i == target:
                counter += 1
    return counter

def flatten(xs):
    flat = []
    for i in xs:
        if type(i) == type([]):
            add = flatten(i)
            for j in add:
                flat.append(j)
        else:
            flat.append(i)
    return flat

def fibonacci(order):
    x = 1
    y = 0
    for i in range(order):
        if i%2 == 0:
            x += y
            print(x)
        else:
            y += x
            print(y)




        







    
