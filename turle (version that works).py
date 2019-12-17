import turtle
def drawSquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        


wn = turtle.Screen()
wn.bgcolor("green")

alex = turtle.Turtle()
drawSquare(alex,50)

