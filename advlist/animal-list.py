#! /usr/bin/env python3

"""
J.Thomas Learning Python

List of Animals
"""

def main():

    #create a list of animals
    animals1 = ["Fox", "Dog", "Yak"]
    
    #display list of animals
    print(animals1)

    #create a new list of animals
    animals2 = ["Cow", "Tiger", "Lion"]

    #extend list of animals
    animals1.extend(animals2)

    #display animals1 list, which now contains animals from animals2 list
    print(animals1)

    #create list 3
    animals3 = ["Zebra", "Elephant"]

    #print the second item in animals3 list
    print(animals3[1])

    #extend list of animals
    animals1.extend(animals3)

    #display the new long list of animals
    print(animals1)

    #display the long list of animals
    for animals in animals1:
        print(animals, end=" ")

if __name__ == "__main__":
    main()
