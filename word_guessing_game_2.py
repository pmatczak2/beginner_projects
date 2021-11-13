import random

words = ('axe', 'four', 'another', 'fives', 'zzzzzzzzzzz')
secret_word = random.choice(words)
print("I am thinking of a word; here it is:")

print("_ " * len(secret_word))

letters_guessed = []
my_attempt = " " * len(secret_word)
while True:
    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    if guess in secret_word:
        my_attempt += guess
        print(f"correct letter: {my_attempt}")
    else:
        print(f"Incorrect; try again {letters_guessed}")