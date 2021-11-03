# Solving the quadratic formuls
# ax^2 + dx +c = 0 # quadratic equation

# Important relevant modules
import cmath #complex math module

# solve the quadratic formula!
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

# Calculate the discriminant
d = (b**2 - 4*a*c)
# This will return an imaginary number if b^2 < 4ac

# Calculate the formula
solution1 = (-b + cmath.sqrt(d))/(2*a)
solution2 = (-b - cmath.sqrt(d))/(2*a)

# Print the solutions
print(f"The solutions to the quddratic equattion are {solution1} and {solution2} ")

# We know wo will have an imaginary nmber is b^2 - 4ac. We want a whole imaginary number so b^2 - 4ac must equal
# a square of the number
# a = 1
# b = 2
# C = 5