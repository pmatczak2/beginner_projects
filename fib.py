# Fibonacci sequence
# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
# The simplest is the series 1, 1, 2, 3, 5, 8, etc.
def fib(n):
    a = 0
    b = 1



    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fib(5)

def num(n):
    a=0
    b=1
    if(n<0):
        print("number is invalid")
    elif(n==1):
        print(a)
    else:
        print(0)
        print(1)
        c=0
        for i in range(2,n):
            c = a + b
            if(c<100):
                a=b
                b=c
                print(c)

num(100)

# At (1) we build a function named fib()
# we assign a value of 0, and 1 to a and b variables
#  have a for loop to iterate through the range() starting at value 2.
# we must add the value of a and b in the c variable.
# next important thing to do is to have the values swap. this is how you shift down


