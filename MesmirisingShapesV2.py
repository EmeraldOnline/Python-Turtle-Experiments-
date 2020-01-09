import turtle

turtle.speed(1000)
speed = int(turtle.numinput("Speed of drawing","How fast would you like the program to draw the spirals? Smaller is faster, can only be an integer."))
maxtimes = 360*speed


while True:
    for i in range(maxtimes):
        angle = i/speed
        repeat = int(angle)
        for i in range(0,repeat):
            turtle.forward(i*2)
            turtle.right(angle)
        turtle.tracer(0)
        turtle.tracer(1)
        turtle.tracer(0) #Needed as a slight delay
        turtle.reset()
    for i in range(maxtimes):
        angle = 360-(i/speed)
        repeat = int(angle*1.5)
        for i in range(0,repeat):
            turtle.forward(i*2)
            turtle.right(angle)
        turtle.tracer(0)
        turtle.tracer(1)
        turtle.tracer(0) #Needed as a slight delay
        turtle.reset()
