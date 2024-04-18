import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
design = turtle.Turtle()
design.speed(10)  # Set the speed of drawing

# Set the pen color and thickness
design.color("blue")
design.pensize(2)

# Draw the design
for _ in range(36):
    for _ in range(4):
        design.forward(100)
        design.right(90)
    design.right(10)

# Hide the turtle and display the drawing
design.hideturtle()
turtle.done()
