from turtle import *
from math import sqrt
from random import randint

def domecek(a):
    forward(a)
    left(90)
    forward(a)
    left(135)
    forward(sqrt(2*a**2))
    right(135)
    forward(a)
    right(135)
    forward(sqrt(2*a**2))
    left(135)
    forward(a)
    left(90)
    forward(a)
    right(135)
    forward(sqrt(2*a**2)/2)
    right(90)
    forward(sqrt(2*a**2)/2)

penup()
goto(0, -150)
pendown()

for i in range(12):
    velikost = randint(50, 90)
    domecek(velikost)
    left(30)

exitonclick()





