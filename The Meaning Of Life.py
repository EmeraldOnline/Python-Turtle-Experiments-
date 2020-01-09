import turtle

t = turtle.Pen()
t.speed(1000)
turtle.tracer(0)
speed = int(turtle.numinput("Speed of drawing","How fast would you like the program to draw the spirals? Smaller is faster, can only be an integer."))
maxtimes = 360*speed


while True:
    for i in range(0,maxtimes):
        angle = i/speed
        print(angle)
        repeat = int(angle)
        turtle.clear()
        for i in range(0,repeat):
            turtle.forward(i*2)
            turtle.right(angle)
        turtle.tracer(0)
        turtle.tracer(1)
        turtle.tracer(0)
        turtle.reset()
    for i in range(0,maxtimes):
        angle = 360-(i/speed)
        print(angle)
        repeat = int(angle*1.5)
        turtle.clear()
        for i in range(0,repeat):
            turtle.forward(i*2)
            turtle.right(angle)
        turtle.tracer(0)
        turtle.tracer(1)
        turtle.tracer(0)
        turtle.reset()
