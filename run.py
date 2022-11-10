"""
Import modules:
random used for random choice and number.
time is used to allow the usertime to read or simulate cpu
decision making.
re to allow checking if a regular expression matches a string
"""
import random
import time
import re


# Global variables allocated to tiles in game boards
END_OF_ROUND = "*" * 80
ALREADY_GUESSED = "0"
EMPTY = "-"
SHIP = "§"
HIT = "X"


def start_screen():
    """
    Displays ASCII art to user
    each time the game begins.
    See credits for ASCII art.
    """
    print("""\

                 __________         __    __  .__                            
                 \______   \_____ _/  |__/  |_|  |   ____                    
  ______   ______ |    |  _/\__  \\   __\   __\  | _/ __ \   ______   ______ 
 /_____/  /_____/ |    |   \ / __ \|  |  |  | |  |_\  ___/  /_____/  /_____/ 
                  |______  /(____  /__|  |__| |____/\___  >                  
                         \/      \/                     \/                   
  _________.__    .__                 ____ __________________________        
 /   _____/|  |__ |__|_____  ______  /_   /   __   \______  \______  \       
 \_____  \ |  |  \|  \____ \/  ___/   |   \____    /   /    /   /    /       
 /        \|   Y  \  |  |_> >___ \    |   |  /    /   /    /   /    /        
/_______  /|___|  /__|   __/____  >   |___| /____/   /____/   /____/         
        \/      \/   |__|       \/                                           

                                                                      
""")


def get_name():
    """
    Prompts the user to enter their name.
    Stores the name for use in the game.
    """
    player_name = input("\nWelcome to BattleShips 1977, please enter your name...")
    return player_name


def back_story():
    """
    Displays a simple back story to the user.
    Uses time module to allow user to process the text.
    """
    print("A hostile Imperial fleet has jumped from Hyperspace and is \
preparing to attack!")
    print("You must take command of the fleet and destroy them before they \
destroy the rebel alliance!")
    time.sleep(2)
    print("Radar reveals the enemy have four ships of varying size.")
    print("Fortunately we have four ships of our own...")
    input("Press Enter to continue...")


def game_rules():
    """
    Displays rules and legend to the user.
    Uses time module to allow user to process the text.
    """
    print("Targeting scanners are ready")
    print("Please note the following: ")
    time.sleep(1.5)
    print(f"\nCoordinates marked {EMPTY} have not been guessed yet")
    print(f"Coordinates marked {SHIP} represent a spaceship")
    print(f"Coordinates marked {HIT} show a hit or destroyed enemy")
    print(f"Coordinates marked {ALREADY_GUESSED} have already been guessed\n")
    input("Press Enter to continue...")


class Board:
    """
    Class to create player and cpu boards, 
    plus guess boards for each.
    Only player and player guess boards will be displayed in the game.
    """
    def __init__(self, name, user):
        self.board = [[EMPTY] * 6 for i in range(6)]
        self.cpu_attacks = [1, 1, 1, 1]
        self.name = name
        self.user = user
        self.columns = [6]
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
        """
        print(f"Board: {self.name}\n")
        print("  A B C D E F ")
        print("  +-+-+-+-+-+")
        row_number = 0
        for row in self.board:
            print('%d|%s' % (row_number, ' '.join(row)))
            row_number += 1
        print(f"\nShield strength: {self.shields}\n")

    def place_ships(self, ship_size, row, column, orientation):
        """
        Method to ensure user places a ship at
        valid coordinates and not off the board.
        """
        if orientation == "H":
            if column + ship_size > 6:
                if self.user == "player":
                    print("Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True
        else:
            if row + ship_size > 6:
                if self.user == "player":
                    print("Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True

    def check_ship_placement(self, board, row, column, orientation, ship_size):
        """
        Method to ensure ships do not overlap when placed.
        If coordinates overlap, prompts user to try again.
        """
        if orientation == "H":
            for i in range(column, column + ship_size):
                if board[row][i] == SHIP:
                    if self.user == "player":
                        print("\nWe've already placed a ship here, sir...")
                        print("Let's try that again!\n")
                        return True
                    else:
                        return True
        else:
            for i in range(row, row + ship_size):
                if board[i][column] == SHIP:
                    if self.user == "player":
                        print("\nWe've already placed a ship here, sir...")
                        print("Let's try that again!\n")
                        return True
                    else:
                        return True
        return False

    def ship_type(self, ship_size):
        """
        Method defines ship sizes.
        Informs user of ship type and size.
        """
        print("Please select horizontal \u2192 or vertical \u2193 orientation")
        print("Commander, make sure the ships do not collide!")
        if ship_size == 4:
            print(" ")
            print("We've stolen an Imperial Star Destroyer(4), let's deploy it now!\n")
        elif ship_size == 3:
            print(" ")
            print("Let's deploy our CR90 Corvette(3)\n")
        elif ship_size == 2:
            print(" ")
            print("The Millennium Falcon(2) has been repaired, let's place it\n")
        elif ship_size == 1:
            print("We have an X-wing(1) ready to go, let's place that too!")

    def player_ship_placement(self):
        """
        Asks the user for their preferred orientation,
        row and column.
        Provides feedback to user if invalid input is entered.
        """
        while True:
            try:
                orientation = input("Select Ship Orientation (H or V): \n")\
                    .upper()
                if orientation == "H" or orientation == "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("R2D2: Beep...Invalid input, please try again...boop")
        while True:
            try:
                column = input("Commander, please select a column A-F: \n")\
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
                row = input("Commander, please select a row 0-5:  \n")
                if row in self.valid_row_input:
                    row = int(row)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("R2D2: Beep...Please enter a valid number 0-5...boop")
        return orientation, column, row

    def populate_boards(self):
        """
        Populates player and cpu boards.
        CPU ship placement is decided randomly.
        """
        size_of_ships = [4, 3, 2, 1]
        for ship_size in size_of_ships:
            while True:
                if self.user == "cpu":
                    orientation = random.choice(["H", "V"])
                    row = random.randint(0, 5)
                    column = random.randint(0, 5)
                    if self.place_ships(ship_size, row, column, orientation):
                        if self.check_ship_placement(self.board, row, column, orientation, ship_size) is False:
                            if orientation == "H":
                                for i in range(column, column + ship_size):
                                    self.board[row][i] = SHIP
                            else:
                                for i in range(row, row + ship_size):
                                    self.board[i][column] = SHIP
                            break
                else:
                    if self.user == "player":
                        self.ship_type(ship_size)
                        orientation, column, row = self.player_ship_placement()
                        if self.place_ships(ship_size, row, column, orientation):
                            if self.check_ship_placement(self.board, row, column, orientation, ship_size) is False:
                                if orientation == "H":
                                    for i in range(column, column + ship_size):
                                        self.board[row][i] = SHIP
                                else:
                                    for i in range(row, row + ship_size):
                                        self.board[i][column] = SHIP
                                print(" ")
                                self.display_board()
                                break

    def random_number(self):
        """
        Method returns a random int between 1 and 2.
        Used to decide random cpu attack.
        """
        random_attack = random.randint(1, 2)
        return random_attack

    def comp_attack_column(self):
        """
        Holds logic for cpu attack.
        Returns a value for the row based
        off last hit ship on cpu guess board.
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

    def comp_attack_row(self):
        """
        Holds the logic for cpu attack.
        Returns a value for the column based
        off last hit ship on comp_guess board.
        """
        row_hit = self.rows[-1]
        if row_hit == 6:
            row = random.randint(0, 6)
            return row
        else:
            random_attack = self.random_number()
            if random_attack == 1:
                row = row_hit + 1
                return row
            elif random_attack == 2:
                row = row_hit - 1
                return row

    def player_attack(self):
        """
        Prompts player to input attack coordinates.
        Uses AI methods to decide cpu attack coordinates.
        Returns cooordinates to be used in the game.
        """
        while True:
            if self.user == "player":
                print("Sir, weapons are charged and ready!\n")
                try:
                    column = input("Please select a column A-F: \n").upper()
                    if not re.match("^[A-F]*$", column):
                        print("Sir, those coordinates are out of range...please enter a number 0-5: ")
                    else:
                        column = self.col_letters_as_numbers[column]
                        break
                except KeyError:
                    print("Sir, please enter a letter")
            elif self.user == "cpu guess":
                column = self.comp_attack_column()
                if column == range(0, 6):
                    break
                else:
                    column = random.randint(0, 5)
                    break
        while True:
            if self.user == "player":
                try:
                    row = input("Please select a row 0-5: \n")
                    if row in self.valid_row_input:
                        row = int(row)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Please Enter a number 0-5")
            elif self.user == "cpu guess":
                row = self.comp_attack_row()
                if row == range(0, 6):
                    break
                else:
                    row = random.randint(0, 5)
                    break
        return column, row

    def count_misses(self):
        """
        Tracks last four AI attacks. If 4, 
        forces random column and row.
        """
        one = self.cpu_attacks[-1]
        two = self.cpu_attacks[-2]
        three = self.cpu_attacks[-3]
        four = self.cpu_attacks[-4]
        sum_of_attack = one + two + three + four
        if sum_of_attack == 8:
            self.columns.append(6)
            self.rows.append(6)
        else:
            pass

    def shields_counter(self):
        """
        ohkjj
        """
        counter = 10
        for row in self.board:
            for column in row:
                if column == HIT:
                    counter -= 1
                    self.shields = counter
        return self.shields


def play_game(player_board, player_guess, cpu_board, cpu_guess):
    """
    giugiui
    """
    player_turn = 0
    cpu_turn = 1
    player_shields = 10
    cpu_shields = 10
    while True:
        if player_turn < cpu_turn:
            player_guess.display_board()
            column, row = player_board.player_attack()
            if player_guess.board[row][column] == ALREADY_GUESSED:
                print("Sir, we have already fired on these coordinates!\n")
            elif player_guess.board[row][column] == HIT:
                print("Sir, we have already hit a ship at these coordinates!\n")
            elif cpu_board.board[row][column] == SHIP:
                print(" ")
                print(END_OF_ROUND)
                print("Great shot Sir, we hit a ship!\n")
                player_guess.board[row][column] = HIT
                player_turn += 1
                player_guess.shields_counter()
                player_guess.display_board()
                cpu_shields -= 1
                print("Brace yourself Sir, the enemy are attacking...")
                time.sleep(1)
                if cpu_shields == 0:
                    print("Sir, enemy shields are depleted, they're retreating!")
                    print("We have won!!")
                    print(" ")
                    print(END_OF_ROUND)
                    break
            else:
                print(" ")
                print(END_OF_ROUND)
                print("\nMissiles have missed, Sir!\n")
                player_guess.board[row][column] = ALREADY_GUESSED
                player_turn += 1
                player_guess.display_board()
                print("Brace yourself Sir, the enemy are attacking...")
                time.sleep(1)
        if cpu_turn == player_turn:
            row, column = cpu_guess.player_attack()
            if cpu_guess.board[row][column] == ALREADY_GUESSED:
                pass
            elif cpu_guess.board[row][column] == HIT:
                pass
            elif player_board.board[row][column] == SHIP:
                print("Sir, the enemy have hit one of our ships!\n")
                cpu_turn += 1
                player_shields -= 1
                cpu_guess.columns.append(column)
                cpu_guess.rows.append(row)
                cpu_guess.board[row][column] = HIT
                player_board.board[row][column] = HIT
                player_board.shields_counter()
                player_board.display_board()
                cpu_guess.cpu_attacks.append(0)
                time.sleep(1)
                if player_shields == 0:
                    print("C3PO: Sir, our shields are depleted, we're doomed!")
                    print(" ")
                    print(END_OF_ROUND)
                    break
            else:
                print("Sir, they have missed our ships!\n")
                cpu_guess.board[row][column] = ALREADY_GUESSED
                cpu_turn += 1
                player_board.display_board()
                cpu_guess.cpu_attacks.append(1)
                cpu_guess.count_misses()
                time.sleep(2)


def play_again():
    """
    Upon finishing the game,
    The player is offered the choice
    of playing another game or 
    quitting.
    """
    print("\nWould you like to play again?")
    player_response = input("Please enter Y or N: \n").upper()
    print(" ")
    while True:
        if player_response == "Y":
            print(END_OF_ROUND)
            new_game()
        elif player_response == "N":
            print(" ")
            print("Thank you for playing. May the force be with you...always")
            print(" ")
            print(END_OF_ROUND)
            return False
        else:
            print(" ")
            print("Please enter Y or N")
            player_response = input("Enter Y or N: \n").upper()


def main():
    """
    Runs all functions above to start new game.
    Shows start screen,
    Prompts player for their name.
    Creates four instances of board class.
    Populates boards
    """
    start_screen()
    player_name = get_name()
    print(f"Welcome, Commander {player_name}, may the force be with us!")
    back_story()
    game_rules()
    print("Now, we must deploy our fleet, we have four ships...")
    player_board = Board(player_name, "player")
    player_guess = Board("Space Radar", "player guess")
    cpu_board = Board("Empire", "cpu")
    cpu_guess = Board("Empire guess", "cpu guess")
    cpu_board.populate_boards()
    player_board.display_board()
    player_board.populate_boards()
    time.sleep(1)
    print(END_OF_ROUND)
    print(" ")
    play_game(player_board, player_guess, cpu_board, cpu_guess)
    play_again()

# Calls main function to start game
main()()