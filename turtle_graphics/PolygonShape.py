# import package
import turtle

WIDTH, HEIGHT = 360, 360
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
turtle.penup()
turtle.goto(120, 250)
turtle.pendown()
# for default shape
turtle.forward(100)

# for circle shape
turtle.shape("circle")
turtle.right(60)
turtle.forward(100)

# for triangle shape
turtle.shape("triangle")
turtle.right(60)
turtle.forward(100)

# for square shape
turtle.shape("square")
turtle.right(60)
turtle.forward(100)

# for arrow shape
turtle.shape("arrow")
turtle.right(60)
turtle.forward(100)

# for turtle shape
turtle.shape("turtle")
turtle.right(60)
turtle.forward(100)
turtle.done()
