"""
This file contains the words that are randomly called in the main run.py file
"""
import random


def select_random_word():
    """ This function generates the word the user will attempt guessing"""
    words = [
        "Horse",
        "Pony",
        "Saddle",
        "Bridle",
        "Girth",
        "Mare"
    ]

    random_word = random.choice(words)
    return random_word.lower()
