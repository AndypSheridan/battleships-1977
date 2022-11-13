"""
Import modules:
random used for random choice and number.
time is used to allow the user time to read
or simulate cpu decision making.
os is used to prevent overloading the display
re to check owner input is valid
matches a string.
"""
import random
import time
import os
import re


# Global variables used to update game boards
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
    print("\nA long time ago, in a galaxy far, far away...\n")
    print("""
                                                                                    
    +             +             +               +          +       +       +       
         +                +            +                      +              + 
               +       +                       +    +                  +
 +                   +        +                         +                  +     
                                 +        +                  +               +
       +           +                  +                         +         +
                          +     +                +     +             +
        +               +          +      +                 +              +
   +          +         +                           +               +
                +                       +  +            +                  +
                      +            +                          +
        +                +         +                               +        +
    +         +                 +                +        +
                   +                  +             +            +        +
    """)
    time.sleep(2)
    input("Press Enter...")
    os.system("clear")
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
    player_name = input("Welcome to BattleShips 1977, \
please enter your name... ")
    return player_name


def back_story():
    """
    Displays a simple back story to the user.
    Uses time module to allow owner time to process the text.
    """
    print("A hostile Imperial fleet has jumped from Hyperspace and is \
preparing to attack!\n")
    print("Take command of our own ships and destroy them before they \
can wipe us out.")
    input("\nPress Enter to continue...")
    os.system("clear")
    print("Targeting scanners reveals the enemy have four ships of varying \
size.")
    print("\nFortunately we have four ships of our own...")
    time.sleep(1)
    print("\nA stolen Imperial Star Destroyer (length: 4)")
    time.sleep(1)
    print("\nA CR90 Corvette (length: 3)")
    time.sleep(1)
    print("\nThe Millennium Falcon with functioning hyperdrive (length: 2)")
    time.sleep(1)
    print("\nAn X-Wing (length: 1)")
    time.sleep(1)
    input("\nPress Enter to continue...")
    os.system("clear")


def game_rules():
    """
    Displays rules and legend to the user.
    Uses time module to allow owner to process the text.
    """
    print("Targeting scanners are ready!\n")
    print("Please note the following...")
    time.sleep(2)
    print(f"\nCoordinates marked {EMPTY} have not been guessed yet\n")
    time.sleep(1)
    print(f"Coordinates marked {SHIP} represent a spaceship\n")
    time.sleep(1)
    print(f"Coordinates marked {HIT} show a hit or destroyed enemy\n")
    time.sleep(1)
    print(f"Coordinates marked {ALREADY_GUESSED} have already been guessed\n")
    time.sleep(1)
    input("\nPress Enter to continue...")
    os.system("clear")
    print("The enemy are using the same shield configuration as us, \
Commander\n")
    time.sleep(1)
    print("Ten direct hits on the enemy will give us the victory!\n")
    time.sleep(1)
    print("Unfortunately, we can also only withstand ten direct hits.\n")
    time.sleep(1)
    input("Press Enter to continue...")
    os.system("clear")


def win_screen():
    print(""" 

____    ____  ______    __    __     ____    __    ____  __  .__   __.  __  
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | |  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | |  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | |__| 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| (__) 
                                                                            

""")


def lose_screen():
    print("""

____    ____  ______    __    __      __        ______        _______. _______ 
\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|
 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   
  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ 
    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|
                                                                               
""")


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

    """
    Stores valid row input to be used when
    determining x axis coordinates.
    """
    valid_row_input = {
        "0", "1", "2", "3", "4", "5"
    }

    """
    Variable to store converted column letters as
    numbers when determining y-axis coordinates.
    """
    col_letters_as_numbers = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5
    }

    def display_board(self):
        """
        Prints boards to the terminal.
        Displays shield strength.
        See credits in Readme for further information
        """
        print(f"\nBoard: {self.name}\n")
        print("  A B C D E F ")
        print("  +-+-+-+-+-+")
        row_number = 0
        for row in self.board:
            print('%d|%s' % (row_number, ' '.join(row)))
            row_number += 1
        print(f"Shield strength: {self.shields}\n")

    def ship_type(self, ship_size):
        """
        Related to placing ships on board.
        Method defines ship sizes.
        Informs user of ship type and size.
        If/elif statement runs through ships sequentially
        in decresing order of size.
        """
        print("Please select horizontal \u2192 or vertical \u2193 orientation")
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

    def place_ships(self, ship_size, row, column, orientation):
        """
        Related to ship placement.
        Method to ensure user places a ship at
        valid coordinates and not off the board.
        """
        if orientation == "H":
            if column + ship_size > 6:
                if self.owner == "player":
                    print("Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True
        else:
            if row + ship_size > 6:
                if self.owner == "player":
                    print("Sir, that is out of range, try again!\n")
                    return False
                else:
                    return False
            else:
                return True

    def player_ship_input(self):
        """
        Prompts the user for their preferred orientation,
        row and column.
        Validates input and provides feedback to user
        if invalid input is entered.
        """
        while True:
            try:
                orientation = input("Select Ship Orientation (H or V): ")\
                    .upper()
                if orientation == "H" or orientation == "V":
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
        return orientation, column, row

    def check_ship_placement(self, board, row, column, orientation, ship_size):
        """
        Method to ensure ships do not overlap when placed.
        If coordinates overlap, prompts user to try again.
        """
        if orientation == "H":
            for i in range(column, column + ship_size):
                if board[row][i] == SHIP:
                    if self.owner == "player":
                        print("\nWe've already placed a ship here, sir...")
                        print("Let's try that again!\n")
                        return True
                    else:
                        return True
        else:
            for i in range(row, row + ship_size):
                if board[i][column] == SHIP:
                    if self.owner == "player":
                        print("\nWe've already placed a ship here, sir...")
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
                    orientation = random.choice(["H", "V"])
                    row = random.randint(0, 5)
                    column = random.randint(0, 5)
                    if self.place_ships(ship_size, row, column, orientation):
                        if self.check_ship_placement(
                            self.board, row, column, orientation, ship_size
                                ) is False:
                            if orientation == "H":
                                for i in range(column, column + ship_size):
                                    self.board[row][i] = SHIP
                            else:
                                for i in range(row, row + ship_size):
                                    self.board[i][column] = SHIP
                            break
                else:
                    if self.owner == "player":
                        self.ship_type(ship_size)
                        orientation, column, row = self.player_ship_input()
                        if self.place_ships(
                                ship_size, row, column, orientation):
                            if self.check_ship_placement(
                                self.board, row, column, orientation, ship_size
                                    ) is False:
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

    def player_attack(self):
        """
        Prompts user to input attack coordinates.
        Uses cpu attack column and row methods to determine
        cpu guesses.
        Returns cooordinates to be used in the game.
        """
        while True:
            if self.owner == "player":
                print("C3PO: Sir, weapons are charged and ready!")
                try:
                    column = input(
                        "C3PO: Please select a column A-F: ").upper()
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


def play_game(player_board, player_guess, cpu_board, cpu_guess):
    """
    Contains game logic.
    Ensures user goes first.
    Adjust shield counter based on cpu and player guesses.
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
                print("C3PO: Sir, we have already fired on these \
coordinates!\n")
            elif player_guess.board[row][column] == HIT:
                print("C3PO: Sir, we have already hit a ship at \
these coordinates!\n")
            elif cpu_board.board[row][column] == SHIP:
                print(" ")
                print(END_OF_ROUND)
                print("C3PO: Great shot Sir, we hit a ship!\n")
                time.sleep(1.5)
                player_guess.board[row][column] = HIT
                player_turn += 1
                player_guess.shields_counter()
                player_guess.display_board()
                cpu_shields -= 1
                print("C3PO: Brace yourself Sir, the enemy are attacking...")
                time.sleep(1.5)
                if cpu_shields == 0:
                    print("C3PO: Sir, enemy shields are depleted, \
they're retreating!")
                    print("We have won!!")
                    win_screen()
                    print(" ")
                    time.sleep(3)
                    print(END_OF_ROUND)
                    os.system("clear")
                    break
            else:
                print(" ")
                print(END_OF_ROUND)
                print("\nC3PO: Our missiles have missed, Sir!\n")
                time.sleep(1.5)
                player_guess.board[row][column] = ALREADY_GUESSED
                player_turn += 1
                player_guess.display_board()
                print("C3PO: Brace yourself Sir, the enemy are attacking...")
                time.sleep(1.5)
        if cpu_turn == player_turn:
            row, column = cpu_guess.player_attack()
            if cpu_guess.board[row][column] == ALREADY_GUESSED:
                pass
            elif cpu_guess.board[row][column] == HIT:
                pass
            elif player_board.board[row][column] == SHIP:
                print("C3PO: Sir, the enemy have hit one of our ships!\n")
                time.sleep(1.5)
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
                    lose_screen()
                    print(" ")
                    print(END_OF_ROUND)
                    break
            else:
                print("Sir, they have missed our ships!\n")
                time.sleep(1.5)
                cpu_guess.board[row][column] = ALREADY_GUESSED
                player_board.board[row][column] = ALREADY_GUESSED
                cpu_turn += 1
                player_board.display_board()
                cpu_guess.cpu_attacks.append(1)
                time.sleep(2)


def play_again():
    """
    Upon finishing the game,
    The user is offered the choice
    of playing another game or
    quitting.
    """
    print("\nWould you like to play again?")
    player_response = input("Please enter Y or N: \n").upper()
    print(" ")
    while True:
        if player_response == "Y":
            print(END_OF_ROUND)
            main()
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
    Prompts user for their name.
    Creates four instances of board class.
    Populates boards
    """
    start_screen()
    player_name = get_name()
    print(f"\nWelcome, Commander {player_name}, may the force be with us!\n")
    back_story()
    game_rules()
    print("Now, we must deploy our fleet, we have four ships...")
    player_board = Board(player_name, "player")
    player_guess = Board("Targeting Scanners", "player guess")
    cpu_board = Board("Empire", "cpu")
    cpu_guess = Board("Empire guess", "cpu guess")
    cpu_board.populate_boards()
    player_board.display_board()
    time.sleep(1)
    player_board.populate_boards()
    time.sleep(1)
    print(END_OF_ROUND)
    print(" ")
    time.sleep(3)
    os.system("clear")
    play_game(player_board, player_guess, cpu_board, cpu_guess)
    play_again()


# Calls main function to start game
main()
