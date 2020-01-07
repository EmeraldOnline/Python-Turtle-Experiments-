import turtle
import random
import time

t = turtle.Pen()
t.speed(1000)
turtle.tracer(0)

for i in range(0,72000):
    angle = i/100
    repeat = int(angle*1.5)
    turtle.clear()
    for i in range(0,repeat):
        turtle.forward(i*2)
        turtle.right(angle)
    turtle.tracer(0)
    turtle.tracer(1)
    turtle.tracer(0)
    turtle.reset()
