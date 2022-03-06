import time

ALPHABETS = ('abcdefghijklmnopqrstuvwxyz')


# Sleep time delay function
def print_with_sleep(msg, sleep_interval):
    print(msg)
    time.sleep(sleep_interval)


# Function asking for user to input their name
# Use a decision making process to accept only alphabets as name
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
    print_with_sleep("Hello" + " " + name + " " + "let's start playing Hangman!", 1)
    print_with_sleep("The objective of the game is to guess the secret word one letter at a time", 1)
    print_with_sleep("Don't forget to press 'enter key' after each guess.", 2)
    print_with_sleep("Let the fun begin!", 1)


def play_again():
    """ This function asks user/player if he/she wishes to replay"""
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()
    # Create a decision making process
    if response == 'y':
        run_game()
    else:
        print("Hope you enjoyed the game !. See you next time :)")