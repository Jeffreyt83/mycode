#! /usr/bin/env python3

def main():

    attempt = 0
    answer = " "

    while attempt < 3 and answer != "brian":
        attempt += 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ___": ')
        answer = answer.lower()
        if answer == "brian":
            print('Correct!')
        elif attempt == 3:
            print('Sorry, answer was Brian.')
        else:
            print("Sorry. Try Again.")

if __name__ == "__main__":
    main()
