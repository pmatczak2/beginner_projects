import turtle
screen = turtle.Screen()
fun = turtle.Turtle()
screen.bgcolor('black')
fun.pencolor('cyan')
fun.speed(2000)
def crazy(var1):
    for i in range(720):
        fun.forward(i)
        fun.left(var1)
crazy(250)