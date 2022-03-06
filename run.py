import time

ALPHABETS = ('abcdefghijklmnopqrstuvwxyz')

# Function asking for user to input their name
# Validate that user inputs a letter only
def take_username_input():
    name = input("Enter your name: \n")
    if name.isalpha():
        return name.capitalize()
    else:
        print('Please enter your name using letter only: \n')
        return take_username_input()