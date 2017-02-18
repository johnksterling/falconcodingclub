# hello_sporal.py
import turtle
import time

t = turtle.Pen()
for x in range(100):
        if(x % 3 == 0):
                t.pencolor("red")
        if(x % 3 == 1):
                t.pencolor("blue")
        if(x % 3 == 2):
                t.pencolor("purple")
                t.forward(x)
        t.left(95)
time.sleep(100)
