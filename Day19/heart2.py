import turtle as t
import math as m
import random as r
import time

screen = t.Screen()
screen.setup(650, 650)
screen.bgcolor("black")
screen.tracer(0)
t.hideturtle()
t.width(2)

for i in range(320):
    a = 2 * m.pi * i / 320
    xo = 16 * m.sin(a) ** 3 * 16
    yo = (
        13 * m.cos(a)
        - 5 * m.cos(2 * a)
        - 2 * m.cos(3 * a)
        - m.cos(4 * a)
    ) * 16

    length = r.uniform(0.15, 0.5)
    xi, yi = xo * (1 - length), yo * (1 - length)

    for j in range(10):
        f = j / 10
        end = (j + 1) / 10
        t.pencolor(1 - 0.6 * f, 0.7 * (1 - f), 0.8 * (1 - f))

        t.penup()
        t.goto(xo + (xi - xo) * f, yo + (yi - yo) * f)
        t.pendown()
        t.goto(xo + (xi - xo) * end, yo + (yi - yo) * end)

        screen.update()
        time.sleep(0.02)

t.done()