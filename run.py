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
        self.row_list = [6]
        self.column_list = [6]
        self.attack_list = [1, 1, 1, 1]

    valid_row_input = {
        "0", "1", "2", "3", "4", "5"
    }

    col_letters_as_numbers = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5
    }

    def display_board(self):
        """
        Prints boards to the terminal.
        """
        print(f"Board: {self.name}\n")
        print("  A B C D E F ")
        print("  +-+-+-+-+-+")
        row_number = 0
        for row in self.board:
            print('%d|%s ' % (row_number, ' '.join(row)))
            row_number += 1
        print(f"\nLives left: {self.lives}\n")

    def place_ships(self, ship_size, row, column, orientation):
        """
        """
        if orientation == "H":
            if row + ship_size > 6:
                if self.user == "player":
                    print("Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True
        else:
            if column + ship_size > 6:
                if self.user == "player":
                    print("Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True

    def check_ship_placement(self, board, row, column, orientation, ship_size):
        """
        Function to ensure ships do not overlap when placed.
        If coordinates overlap, prompts user to try again.
        """
        if orientation == "H":
            for i in range(row, row + ship_size):
                if board[column][i] == SHIP:
                    if self.user == "player":
                        print("\We've already placed a ship here, sir...")
                        print("Let's try that again!\n")
                        return True
                    else:
                        return True
        else:
            for i in range(column, column + ship_size):
                if board[i][row] == SHIP:
                    if self.user == "player":
                        print("\We've already placed a ship here, sir...")
                        print("Let's try that again!\n")
                        return True
                    else:
                        return True
        return False

    def ship_type(self, ship_size):
        """
        Allows user to place ships on board.
        """
        print("Please select horizontal or vertical orientation")
        print("Ship coordinates must not overlap")
        if ship_size == 3:
            print(" ")
            print("We have stolen an imperial Star Destroyer(3), let's deploy it now!\n")
        elif ship_size == 2:
            print(" ")
            print("Let's deploy a CR90 Corvette(2)\n")
        elif ship_size == 1:
            print("We have an X-wing, let's place that too!")

    def player_ship_placement(self):
        """
        Asks the user for their preferred orientation,
        row and column. Places ships on the board.
        """
        while True:
            try:
                orientation = input("Select Ship Orientation (H or V): \n").upper()
                if orientation == "H" or orientation == "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid coordinates, please try again")
        while True:
            try:
                row = input("Please select a row 0-5: \n")
                if row in self.valid_row_input:
                    row = int(row)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number between 0-5")
        while True:
            try:
                column = input("Please select a column A-F: \n").upper()
                if not re.match("^[A-F]*$", column):
                    print("Beep...does not compute...please enter a letter A-F...")
                else:
                    column = self.col_letters_as_numbers[column]
                    break
            except KeyError:
                print("Please enter a letter A-F")
        return orientation, row, column

    def add_ships_to_board(self):
        """
        Populates boards
        """
        size_of_ships = [3, 2, 2, 1]
        for ship_size in size_of_ships:
            while True:
                if self.user == "computer":
                    orientation = random.choice(["H", "V"])
                    row = random.randint(0, 3)
                    column = random.randint(0, 3)
                    if self.place_ships(ship_size, row, column, orientation):
                        if self.check_ship_placement(board, row, column, orientation, ship_size)


