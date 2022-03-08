"""
Hangman game ascii artwork
"""
# import colorama to give pictures the traffic light colours
from colorama import Fore, init
init(autoreset=True)


def hangman_pic(wrong):
    """
    Function to hold the Hangman design, passing in wrong as an argument
    """
    if wrong == 0:
        print(Fore.GREEN + "\n+---+")
        print(Fore.GREEN + "    |")
        print(Fore.GREEN + "    |")
        print(Fore.GREEN + "    |")
        print(Fore.GREEN + "   ===")
    elif wrong == 1:
        print(Fore.GREEN + "\n+---+")
        print(Fore.GREEN + "O   |")
        print(Fore.GREEN + "    |")
        print(Fore.GREEN + "    |")
        print(Fore.GREEN + "   ===")
    elif wrong == 2:
        print(Fore.YELLOW + "\n+---+")
        print(Fore.YELLOW + "O   |")
        print(Fore.YELLOW + "|   |")
        print(Fore.YELLOW + "    |")
        print(Fore.YELLOW + "   ===")
    elif wrong == 3:
        print(Fore.YELLOW + "\n+---+")
        print(Fore.YELLOW + " O  |")
        print(Fore.YELLOW + "/|  |")
        print(Fore.YELLOW + "    |")
        print(Fore.YELLOW + "   ===")
    elif wrong == 4:
        print(Fore.RED + "DANGER ZONE")
        print(Fore.RED + "\n+---+")
        print(Fore.RED + " O  |")
        print(Fore.RED + "/|\ |")
        print(Fore.RED + "    |")
        print(Fore.RED + "   ===")
    elif wrong == 5:
        print(Fore.RED + "DANGER ZONE")
        print(Fore.RED + "\n+---+")
        print(Fore.RED + " O  |")
        print(Fore.RED + "/|\ |")
        print(Fore.RED + "/   |")
        print(Fore.RED + "   ===")
    elif wrong == 6:
        print(Fore.RED + "DANGER ZONE")
        print(Fore.RED + "\n+---+")
        print(Fore.RED + " O   |")
        print(Fore.RED + "/|\  |")
        print(Fore.RED + "/ \  |")
        print(Fore.RED + "    ===")
