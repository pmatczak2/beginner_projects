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

# Specifically a object has a state and collection of Methods it can do/preform
# The state is the thing the object knows about itself

# Example - using Turtle
import turtle

# the turtle position, color, ect, is the STATE:
turtle.color('red') # This is the state
# The turtles movement - forward, backwards, left, right are the methods
turtle.forward(100) # This is the method

# We can create our very own class with methods!
# with in this class we can define the methods/operations that our class will do.
# a method is just a function the goes inside out calls (essentially)

class Dog:

    def color(self):
        return "brown"

# Now we can create a variable of our class, Dog!
x = Dog()
print(x)
# The '__main__' is the module tht hte class was defined in this is set by degault to main

# We have created out cory first class!

# Now we can explore something known as the initializer
# This is something EVERY class should have! It essentially sets the default parameters for our class.
# So it's similar to how a turtle has its own default settings

# We will set up a new class to demonstrate the initializer!

class Dogs:

    def __init__(self):
        self.Labrador = "barnie"
        self.Poodle = 3

# Define a variable of this class - create instance of the class
a = Dogs()
# Shoeing our method in action!
print(a.Labrador)
print(a.Poodle)
# Two instances of the class are not always the same
b = Dogs()
print(a == b) # This is false!

# let's look a the extra features you can add

class Animals:

    # initializer
    def __init__(self, animal_type, animal_age, animal_name):
        self.type = animal_type
        self.age = animal_age
        self.name = animal_name

    def type_of_animal(self):
        return 'This animal is a {}'.format(self.type)

    def age_of_animal(self):
        return f"ths age is {self.age}"

    def name_of_animal(self):
        return f"the name of the animal is {self.name}"

    # You can also do some abstract things
    def number(self):
        return self.age + 100

# Create a new variable
# Its important to add the specific parameters!
c = Animals("dog", 10, "bornie")
d = Animals("cat", 9, "muffin")
print(c.type_of_animal())
print(c.age_of_animal())
print(c.type_of_animal())
print(c.number())