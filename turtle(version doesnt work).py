import turtle
def drawSquare(t, sz):
    """make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)




wn = turtle.Screen() # Set up the window and its attributs
wn.bgcolor("green")

alex = turtle.Turtle() # create alex
drawSquare(alex, 50)  # call the function to draw the sqaure passing the actual turtle and the actual side size

wn.exitonclick()
