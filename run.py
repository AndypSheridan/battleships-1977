import random
import time
import re


# Global variables used in game boards

EMPTY = "-"
SHIP = "@"
HIT = "X"
ALREADY_GUESSED = "0"
END_OF_ROUND = "*" * 50


def start_screen():
    """
    Displays a welcome message to the user,
    each time the game begins.
    Displays the rules and the legend.
    """
    print("\nWelcome to Battleships 1977")
    print("You have 10 attempts to destroy the enemy!")
    print(f"Tiles marked {EMPTY} have not been guessed")
    print(f"Tiles marked {SHIP} represent a ship")
    print(f"Tiles marked {HIT} show a hit or destroyed enemy")
    print(f"Tiles marked {ALREADY_GUESSED} have already been guessed\n")


def get_name():
    """
    Prompts the user to enter their name.
    Stores the name for use in the game.
    """
    player_name = input("\nPlease enter your name...")
    return player_name


class Board:
    """
    Class to create player and computer boards, 
    plus guess boards for each.
    Only player and player guess boards will be displayed.
    """
    def __init__(self, name, user):
        self.board = [[EMPTY] * 6 for i in range(6)]
        self.lives = 8
        self.name = name
        self.user = user
        self.row_arr = [6]
        self.column_arr = [6]
        self.attack_arr = [1, 1, 1, 1]

    col_letters_as_numbers = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5
    }

    valid_row_input = {
        "0", "1", "2", "3", "4", "5"
    }

