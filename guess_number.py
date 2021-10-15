import random

number_guess = 0
number = random.randint(1, 20)

my_name = input("Hello, what is your name? ")
print(f"Welcome to the number guessing game {my_name}. Im thinking of a number between an number between 1 and 20.")

for number_guess in range(6):
    guess = input("Take a guess: ")
    guess = int(guess)

    if guess < number:
        print("you guessed too low")

    elif guess > number:
        print("you guessed too high")

    else:
        print("you guessed correctly")
        break

if guess == number:
    number_guess = (number_guess + 1)
    print(f"Great job {my_name}, you guessed my number in {number_guess} guesses")

else:
    print(f"No, the number i was thinking was {number}")