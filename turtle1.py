import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.color("red")
turtle.speed(30)

for i in range(12):
    for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(5)
turtle.done()