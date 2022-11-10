#! /usr/bin/env python3

# Import random number generator
import random

# create a function for the game
def guessing_game():

    # Greet the user
    print("Welcome to the guessing game ", name)

    # Generate a random number between 1 and 10
    y = random.randint(1, 10)

    # Request a number between 1 and 10 from the user and convert it to an intiger
    x = int(input("\nGuess a number between 1 and 10:  "))
    attempt = 1 # Initial attempt
    print("Number of attempts: ", attempt) # Display the current attempt number
    # Check to see if user's guess equals the winning number
    while x != y: 
        print("Sorry, try again.") # If the guess is incorrect, inform the user
        x = int(input("Guess a number between 1 and 10: ")) # Request for a new answer from user
        attempt = attempt + 1 # This increases the attempt by 1 for each incorrect asnwer
        print("Number of attempts: ", attempt) # Display the current attempt number
    print("Congratulations, you guessed correct!") # If the user guessed correct number, congratulate them
    print("Your number of attempts: ", attempt) # Display the number of attempts

# Request user's name
name = input("What is your name: ")

# Ask user what they would like to do
z = int(input("Press 1 to play Guessing Game, Press 2 to quit: "))
if z == 1: # If user select 1, play game
    guessing_game()
elif z == 2: # If user select 2, quit app
    exit()

