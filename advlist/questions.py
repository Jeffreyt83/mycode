#! /usr/bin/env python3

"""
Author: J.Thomas

Objective: Ask user 3 questions, store answers in a list, display the standard list before exiting

Try to use best practice
"""

def main():

    #Create a list of questions
    question = []
    
    #ask question 1 and request input from user
    question.append(input("What is your favorite color? "))

    #ask question 2 and request input from user
    question.append(input("What is your favorite city? "))

    #ask question 3 and request input from user
    question.append(input("Who is your favorite cartoon character? "))

    #display answers to questions
    print(question)

if __name__ == "__main__":
    main()
