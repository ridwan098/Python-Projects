from turtle import*

from random import randint



bgcolour('orange')

x = 1

while x < 400:

    r = randint(0,255)
    g = randint(0,355)
    b = randint(0,255)

    colourmode(255)

    pencolour(r,g,b)

    fd(50 + x)
    rt(90, 911)


    x = x+1

exitonclick()
