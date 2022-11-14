"""
Import random for random attack and
random number generator.
Import re to check for correct input
"""
import random
import re


END_OF_ROUND = "*" * 80
ALREADY_GUESSED = "0"
EMPTY = "\u2022"
SHIP = "§"
HIT = "X"


class Board:
    """
    Class to create player and cpu boards,
    plus guess boards for each.
    Only player and player guess boards will
    be displayed in the game.
    """
    def __init__(self, name, owner):
        # List comprehension to create board
        self.board = [[EMPTY] * 6 for i in range(6)]
        # Sets first four computer attacks
        self.cpu_attacks = [1, 1, 1, 1]
        self.name = name
        self.owner = owner
        # Defines board columns
        self.columns = [6]
        # Defines board rows
        self.rows = [6]
        self.shields = 10

    valid_row_input = {
        "0", "1", "2", "3", "4", "5"
    }

    col_letters_as_numbers = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5
    }

    def display_board(self):
        """
        Prints boards to the terminal.
        Displays shield strength.
        See credits in readme for further details.
        """
        print(f"\nBoard: {self.name}\n")
        print("  A B C D E F ")
        print("  +-+-+-+-+-+")
        row_number = 0
        for row in self.board:
            print(f"{row_number}|{' '.join(row)}")
            row_number += 1
        print(f"Shield strength: {self.shields}\n")

    def ship_type(self, ship_size):
        """
        Related to placing ships on board.
        Method defines ship sizes.
        Informs user of ship type and size.
        If/elif statement runs through ships sequentially
        in decreasing order of size.
        """
        print("You can position ships horizontally \u2192 or \
vertically \u2193")
        print("Commander, make sure the ships do not collide!")
        if ship_size == 4:
            print(" ")
            print("We've stolen an Imperial Star Destroyer(4), \
let's deploy it now!\n")
        elif ship_size == 3:
            print(" ")
            print("Let's deploy our CR90 Corvette(3)\n")
        elif ship_size == 2:
            print(" ")
            print("The Millennium Falcon(2) has been repaired, \
let's place it\n")
        elif ship_size == 1:
            print("We have an X-wing(1) ready to go, let's place that too!")

    def place_ships(self, ship_size, row, column, direction):
        """
        Related to ship placement.
        Method to ensure user places a ship at
        valid coordinates and not off the board.
        """
        if direction == "H":
            if column + ship_size > 6:
                if self.owner == "player":
                    print("C3PO: Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True
        else:
            if row + ship_size > 6:
                if self.owner == "player":
                    print("C3PO: Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True

    def player_ship_input(self):
        """
        Prompts the user for their preferred direction,
        row and column.
        Validates input and provides feedback to user
        if invalid input is entered.
        """
        while True:
            try:
                direction = input("Select Ship Direction (H or V): ")\
                    .upper()
                if direction == "H" or direction == "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("R2D2: Beep...Invalid input, please try again...boop")
        while True:
            try:
                column = input("Commander, please select a column A-F: ")\
                    .upper()
                if not re.match("^[A-F]*$", column):
                    print("C3PO: Sir! Please enter a letter A-F...")
                else:
                    column = self.col_letters_as_numbers[column]
                    break
            except KeyError:
                print("C3PO: Sir! Please enter a letter A-F")
        while True:
            try:
                row = input("Commander, please select a row 0-5: ")
                if row in self.valid_row_input:
                    row = int(row)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("R2D2: Beep...Please enter a valid number 0-5...boop")
        return direction, column, row

    def check_ship_placement(self, board, row, column, direction, ship_size):
        """
        Method to ensure ships do not overlap when placed.
        If coordinates overlap, prompts user to try again.
        """
        if direction == "H":
            for i in range(column, column + ship_size):
                if board[row][i] == SHIP:
                    if self.owner == "player":
                        print("\nC3PO: We've already placed a ship \
here, sir...")
                        print("Let's try that again!\n")
                        return True
                    else:
                        return True
        else:
            for i in range(row, row + ship_size):
                if board[i][column] == SHIP:
                    if self.owner == "player":
                        print("\nC3PO: We've already placed a ship \
here, sir...")
                        print("Let's try that again!\n")
                        return True
                    else:
                        return True
        return False

    def populate_boards(self):
        """
        Populates player and cpu boards.
        CPU ship placement is decided randomly.
        """
        size_of_ships = [4, 3, 2, 1]
        for ship_size in size_of_ships:
            while True:
                if self.owner == "cpu":
                    direction = random.choice(["H", "V"])
                    row = random.randint(0, 5)
                    column = random.randint(0, 5)
                    if self.place_ships(ship_size, row, column, direction):
                        if self.check_ship_placement(
                            self.board, row, column, direction, ship_size
                                ) is False:
                            if direction == "H":
                                for i in range(column, column + ship_size):
                                    self.board[row][i] = SHIP
                            else:
                                for i in range(row, row + ship_size):
                                    self.board[i][column] = SHIP
                            break
                else:
                    if self.owner == "player":
                        self.ship_type(ship_size)
                        direction, column, row = self.player_ship_input()
                        if self.place_ships(
                                ship_size, row, column, direction):
                            if self.check_ship_placement(
                                self.board, row, column, direction, ship_size
                                    ) is False:
                                if direction == "H":
                                    for i in range(column, column + ship_size):
                                        self.board[row][i] = SHIP
                                else:
                                    for i in range(row, row + ship_size):
                                        self.board[i][column] = SHIP
                                print(" ")
                                self.display_board()
                                break

    def player_attack(self):
        """
        Prompts user to input attack coordinates.
        Uses cpu attack column and row methods to determine
        cpu guesses.
        Returns cooordinates to be used in the game.
        """
        while True:
            if self.owner == "player":
                try:
                    column = input(
                        "C3PO: Weapons are ready! Please select a \
column A-F: ").upper()
                    if not re.match("^[A-F]*$", column):
                        print("C3PO: Sir, those coordinates are out of range!\
Please enter a number 0-5: ")
                    else:
                        column = self.col_letters_as_numbers[column]
                        break
                except KeyError:
                    print("C3PO: Sir, please enter a letter")
            elif self.owner == "cpu guess":
                column = self.cpu_attack_column()
                if column == range(0, 6):
                    break
                else:
                    column = random.randint(0, 5)
                    break
        while True:
            if self.owner == "player":
                try:
                    row = input("C3PO: Please select a row 0-5: ")
                    if row in self.valid_row_input:
                        row = int(row)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("C3PO: Please Enter a number 0-5")
            elif self.owner == "cpu guess":
                row = self.cpu_attack_row()
                if row == range(0, 6):
                    break
                else:
                    row = random.randint(0, 5)
                    break
        return column, row

    def random_number(self):
        """
        Method returns a random number between 1 and 2.
        Used to determine a random cpu attack.
        """
        random_attack = random.randint(1, 2)
        return random_attack

    def cpu_attack_column(self):
        """
        Determines cpu attack column.
        Returns a column value based
        on last hit ship on cpu guess board.
        """
        column_hit = self.columns[-1]
        if column_hit == 6:
            column = random.randint(0, 5)
            return column
        else:
            random_attack = self.random_number()
            if random_attack == 1:
                column = column_hit + 1
                return column
            elif random_attack == 2:
                column = column_hit - 1
                return column

    def cpu_attack_row(self):
        """
        Determines cpu attack row.
        Returns a row value based
        on last hit ship on cpu guess board.
        """
        row_hit = self.rows[-1]
        if row_hit == 6:
            row = random.randint(0, 5)
            return row
        else:
            random_attack = self.random_number()
            if random_attack == 1:
                row = row_hit + 1
                return row
            elif random_attack == 2:
                row = row_hit - 1
                return row

    def shields_counter(self):
        """
        Tracks cpu and player hits.
        Uses a nested for loop to deduct
        one from shield counter
        on each successful hit.
        """
        counter = 10
        for row in self.board:
            for column in row:
                if column == HIT:
                    counter -= 1
                    self.shields = counter
        return self.shields
