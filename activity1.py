import turtle
#creating canvas
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
turtle.title("Welcome to turle")
#turtle object
board=turtle.Turtle()
#creating a square
for i in range(4):
    board.forward(400)
    board.left(90)
    i = i+i
    turtle.done