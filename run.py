"""
Main python code for running the Horse Hangman game
"""
import time
import os
from colorama import Fore, init
from constants import hangman_status, TOTAL_ATTEMPTS, ALPHABETS
from words import select_word

init(autoreset=True)


# Prints a separator line
def print_lines():
    """
    Function to print the lines for the formatting
    """
    print(Fore.BLUE + "------------------------------------------------------")


def print_with_sleep(msg, sleep_interval):
    """
    Sleep time function
    """
    print(msg)
    time.sleep(sleep_interval)


def take_username_input():
    """
    Function asking for user to input their name
      Use a decision making process to accept only alphabets as name
    """
    name = input(Fore.MAGENTA + "Enter your name: \n")
    if name.isalpha():
        return name.capitalize()
    else:
        print(Fore.RED + 'You did not enter a valid name')
        print(Fore.RED + 'Please enter your name using letter only: \n')
        return take_username_input()


def show_greeting_and_take_username():
    """
    Statements welcoming the user and asking for them to input their name
    """
    print_lines()
    print(Fore.YELLOW + "Welcome to Horse Hangman")
    print(Fore.YELLOW + "Guess the word before the man is hung and you win!")
    print_lines()
    name = take_username_input()
    print_lines()
    print(Fore.YELLOW + "Hello & welcome" + " " + name + " ")
    print_with_sleep(Fore.YELLOW + "Please wait for the rules to load.....", 1)
    print()
    print_with_sleep(Fore.CYAN + "The objective of the game is to guess\
 the secret word one letter at a time", 1)
    print_with_sleep(Fore.BLUE + "Hint: All words are Horse related.", 1)
    print_with_sleep(Fore.CYAN + "Don't forget to press \
 'enter key' after each guess", 1)
    print()
    print_with_sleep(Fore.YELLOW + "Ok Lets start playing Horse Hangman!", 1)
    print_lines()


def play_again():
    """ This function asks user/player if he/she wishes to replay"""
    response = input(
        Fore.YELLOW + "Would you like to play again?\
 Enter 'Y' for Yes or any key for No: ").lower()
    print_lines()
    # Create a decision making process
    if response == 'y':
        run_game()
    elif response == 'n':
        os.system("clear")
        print("")
        print_lines()
        print(Fore.CYAN + "Hope you enjoyed the game, See you next time :)")
        print_lines()
    else:
        os.system("clear")


def run_game():
    """
    Define the main function that runs the game
    """
    # Set guess word to get_word function for a random word to be generated
    word = select_word()
    # Initiate an empty list for guessed letter
    guessed_letters = []
    # Initiate a counter for number of tries by the user
    total_attempt_counter = TOTAL_ATTEMPTS
    # Set inital guess to false
    sucessfully_guessed = False
    wrong_guess = 0
    # Initate a while loop and create decisions
    # Also a create decisions for if user inputs a wrong entry
    # Deduct attempts each user fails to guess incorrectly
    while sucessfully_guessed is not True and total_attempt_counter > 0:
        print()
        print(Fore.BLUE + 'You have ' + str(total_attempt_counter) + ' \
 guess attempts...')
        guessed_letter = input(Fore.YELLOW + 'Guess a letter: \n').lower()
        # user inputs a letter
        if len(guessed_letter) == 1:
            if guessed_letter not in ALPHABETS:
                print_lines()
                print(Fore.RED + 'You are yet to enter a letter, \
 check your entry')
                print(Fore.RED + 'Please only enter a letter')
                print()
            elif guessed_letter in guessed_letters:
                print_lines()
                print(Fore.RED + 'You have already guessed that letter before')
                print()
            elif guessed_letter not in word:
                print_lines()
                print(Fore.RED + 'Sorry, that letter is not part of the word')
                print()
                guessed_letters.append(guessed_letter)
                total_attempt_counter -= 1
                wrong_guess += 1
                hangman_status(wrong_guess)
                print()
            elif guessed_letter in word:
                print_lines()
                print(Fore.GREEN + 'Super that letter is in the word')
                print()
                guessed_letters.append(guessed_letter)
                hangman_status(wrong_guess)
                print()
        else:
            if len(guessed_letter) != 1:
                print_lines()
                print(Fore.RED + "Oops Please enter a letter")
                print()
        result = ''
        if sucessfully_guessed is not True:
            for letter in word:
                if letter in guessed_letters:
                    result += letter
                else:
                    result += '_'
            print(Fore.CYAN + " ".join(result.capitalize()))
        if result == word:
            print()
            sucessfully_guessed = True
            print_lines()
            print(Fore.GREEN + "Well Done :) You Won !!!")
            print(Fore.GREEN + "The right word is: ", word.capitalize())
            print_lines()
        elif total_attempt_counter == 0:
            print()
            print_lines()
            print(Fore.RED + "Opps! You ran out of guesses, \
 Hard Luck, You Lose !!")
            print(Fore.RED + "The correct word was: ", word.capitalize())
            print_lines()
# Initiate play_again function if user wishes to continue
    play_again()


def start_game():
    """
    Function that shows the greeting asks for the user name and runs the game
    """
    show_greeting_and_take_username()
    run_game()


# Full program run
start_game()
