import time
import os
from hangman_pics import hangman_pic
from words import select_word
from colorama import Fore, init
init(autoreset=True)

# Set alphabet as constant
ALPHABETS = ('abcdefghijklmnopqrstuvwxyz')


def print_lines():
    print(Fore.BLUE + "--------------------------------------------------------------------------")

# Sleep time delay function
def print_with_sleep(msg, sleep_interval):
    print(msg)
    time.sleep(sleep_interval)


# Function asking for user to input their name
# Use a decision making process to accept only alphabets as name
def take_username_input():
    name = input(Fore.MAGENTA + "Enter your name: \n")
    if name.isalpha():
        return name.capitalize()
    else:
        print(Fore.RED + 'You did not enter a valid name ! Please enter your name using letter only: \n')
        return take_username_input()


# Statements welcoming the user and asking for them to input their name
def show_greeting_and_take_username():
    print_lines()
    print(Fore.YELLOW + "Welcome to Horse Hangman")
    print_lines()
    name = take_username_input()
    print_lines()
    print_with_sleep(
        Fore.YELLOW + 
        "Hello & welcome" + " " 
        + name + " " 
        + "please wait for the rules to load.....", 1)
    print()
    print_with_sleep(Fore.YELLOW + "The objective of the game is to guess the secret word one letter at a time",1)
    print_with_sleep(Fore.BLUE + "Hint: All words are Equine related.", 1)
    print_with_sleep(Fore.YELLOW + "Don't forget to press 'enter key' after each guess.", 1)
    print_with_sleep(Fore.YELLOW + "Lets start playing Horse Hangman!", 1)
    print_lines()


def play_again():
    """ This function asks user/player if he/she wishes to replay"""
    response = input(Fore.YELLOW + "Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()
    print_lines()
    # Create a decision making process
    if response == 'y':
        run_game()
    else:
        os.system("clear")
        print("")
        print(Fore.MAGENTA + "Hope you enjoyed the game, See you next time :)")


# print letter or dash under hangman pic
    

# Define function to run the gamey
def run_game():
    # Set guess word to get_word function for a random word to be generated
    word = select_word()
    # Initiate an empty list for guessed letter
    guessed_letters = []
    # Initiate a counter for number of tries by the user
    total_attempt_counter = 6
    # Set inital guess to false
    sucessfully_guessed = False
    wrong_guess = 0
    # Initate a while loop and create decisions
    # Also a create decisions for if user inputs a wrong entry
    # Deduct attempts each user fails to guess incorrectly
    while sucessfully_guessed is not True and total_attempt_counter > 0:
        print()
        print(Fore.GREEN + 'You have ' + str(total_attempt_counter) + ' guess attempts...')
        guessed_letter = input(Fore.YELLOW + 'Guess a letter: \n').lower()
        # user inputs a letter
        if len(guessed_letter) == 1:
            if guessed_letter not in ALPHABETS:
                print_lines()
                print(Fore.RED + 'You are yet to enter a letter, check your entry,') 
                print(Fore.RED + 'please enter a letter not a number or character')
                print()
            elif guessed_letter in guessed_letters:
                print_lines()
                print(Fore.RED + 'You have already guessed that letter before.Try again!')
                print()
            elif guessed_letter not in word:
                print_lines()
                print(Fore.RED + 'Sorry, that letter is not part of the word')
                print()
                guessed_letters.append(guessed_letter)
                total_attempt_counter -= 1
                wrong_guess += 1
                hangman_pic(wrong_guess)
                print()
            elif guessed_letter in word:
                print_lines()
                print(Fore.GREEN + 'Super that letter is in the word')
                print()
                guessed_letters.append(guessed_letter)
                hangman_pic(wrong_guess)
                print()
        else:
            if guessed_letter.isalpha() is not True:
                print_lines()
                print(Fore.RED + 'You did not enter a letter ! Please enter a letter !')
                print()
                
        result = ''
        if sucessfully_guessed is not True:
            for letter in word:
                if letter in guessed_letters:
                    result += letter
                else:
                    result += '_'
            print(Fore.GREEN + " ".join(result.capitalize()))
        if result == word:
            print()
            sucessfully_guessed = True
            print_lines()
            print(Fore.GREEN + "Well Done you guessed the right word. You Won :)")
            print_lines()
        elif total_attempt_counter == 0:
            print()
            print_lines()
            print(Fore.RED + "Opps! You ran out of guesses, Hard Luck, You Lose !!")
            print(Fore.RED + "The correct word was: ", word.capitalize())
            print_lines()
# Initiate play_again function if user wishes to continue
    play_again()

      
# Function that shows the greeting asks for the user name and runs the game
def start_game():
    show_greeting_and_take_username()
    run_game()


# Full program run
start_game()
