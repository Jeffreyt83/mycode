#! /usr/bin/env python3

"""
Author: J. Thomas

Objective: Practice if, elif, else 

"""

# standard library
import random

def main():

    #Welcome
    print("WELCOME TO THE GUESSING GAME!!")

    # Generate random number between 1 and 10
    number = random.randrange(1,10)

    # Have user guess a number between 1 and 10
    guess = input("Guess a number between 1 and 10: ")

    #Check if guess is an integer
   # if guess.isdigit():
    #    print('You guessed '+ print(guess))
    #else:
     #   print('Please choose between 1 and 10')

    # check if the guess was correct
    if guess == number:
        print("CONGRATULATIONS!! You guessed correct.")
    else:
        print("Sorry, try again!")

if __name__ == "__main__":
    main()
