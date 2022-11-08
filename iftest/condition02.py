#! /usr/bin/env python3

def main():

    #hostname
    hostname = input("What value should we set for hostname?")

    if hostname.lower() == "mtg":
        print("The hostname was found to be MTG")
        print("hostname matches expected config")

    #Always print out to the user
    print("Exiting the script")

if __name__ == "__main__":
    main()
