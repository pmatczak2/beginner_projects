# oop in python
# every value in Python is considered a object
number = 987453
word = "hello"
# number is an object of the class 'int' and word is an object of the class 'str'
print(type(number), type(word))

# We can also find the type of a function
def my_name():
    print("Pete")

print(type(my_name))

# WE CAN CREATE OUR OWN CLASSES

# EVERY TIME YOU CREATE SOMETHING IN PYTHON YOU ARE CREATING A OBJECT IN A CLASS!
# This class defines the things that the specific object can do.

# Specificly a object has a state and collection of Methods it can do?preform
# The state is the thing the object knows about itself

# Example - using Turtle
import turtle

# the turtle position, color, ect, is the STATE:
turtle.color('red') # This is the state
# The turtles movement

