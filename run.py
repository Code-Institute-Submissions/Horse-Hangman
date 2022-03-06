import time

ALPHABETS = ('abcdefghijklmnopqrstuvwxyz')


# Function asking for user to input their name
# Validate that user inputs letters only
def take_username_input():
    name = input("Enter your name: \n")
    if name.isalpha():
        return name.capitalize()
    else:
        print('Please enter your name using letter only: \n')
        return take_username_input()


# Statements welcoming the user and asking for them to input their name
def show_greeting_and_take_username():
    print("-------------------------------------------")
    print("Welcome to Horsey Hangman")
    print("-------------------------------------------")
    name = take_username_input()
    print("-------------------------------------------")
    # Use a decision making process to accept only alphabets as name
    print_with_sleep("Hello" + " " + name + " " + "let's start playing Hangman!", 1)
    print_with_sleep("The objective of the game is to guess the secret word one letter at a time", 1)
    print_with_sleep("Don't forget to press 'enter key' after each guess.", 2)
    print_with_sleep("Let the fun begin!", 1)