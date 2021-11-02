# Import relevant modules
import matplotlib.pyplot as plt
# Take 2 coordinates, x and y. Essentially it just means that we will have two values for x adn y.

# Creating the class!

class Coordinates:

    def __init__(self, starting_x, starting_y):
    # create a new point at the coordinates give below
        self.x = starting_x
        self.y = starting_y

    def return_x(self):
        return self.x

    def return_y(self):
        return self.y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def distance_from_origin(self):
        return ((self.x)**2 + (self.y)**2)**0.5

    def plot(self):
        plt.plot(self.x, self.y, marker='o', markersize=10)
        plt.show()

a = Coordinates(10, 12)
print(a.return_x())
print(a.return_y())
print(a.multiplication())
print(a.distance_from_origin())
a.plot()