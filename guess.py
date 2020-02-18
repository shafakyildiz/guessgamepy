# Produce a random num
from random import randrange
num = randrange(10)

# Take a guess from user

guess = int(input("Please make a guess between 1-10: "))

while num != guess:
    print("Your guess is not correct.")
    guess = int(input("Please make another guess: "))

if num == guess:
        print("You guessed the number correctly, congrats!")