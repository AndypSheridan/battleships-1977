import random
import time
import re


# Global variables used in game boards
EMPTY = "-"
SHIP = "@"
HIT = "X"
ALREADY_GUESSED = "0"
END_OF_ROUND = "*" * 80


def start_screen():
    """
    Displays a welcome message to the user,
    each time the game begins.
    Displays the rules and the legend.
    See credits for ASCII art.
    """
    print("""\

.______        ___   .___________.___________. __       _______ 
|   _  \      /   \  |           |           ||  |     |   ____|
|  |_)  |    /  ^  \ `---|  |----`---|  |----`|  |     |  |__   
|   _  <    /  /_\  \    |  |        |  |     |  |     |   __|  
|  |_)  |  /  _____  \   |  |        |  |     |  `----.|  |____ 
|______/  /__/     \__\  |__|        |__|     |_______||_______|
                                                                
     _______. __    __   __  .______     _______.               
    /       ||  |  |  | |  | |   _  \   /       |               
   |   (----`|  |__|  | |  | |  |_)  | |   (----`               
    \   \    |   __   | |  | |   ___/   \   \                   
.----)   |   |  |  |  | |  | |  |   .----)   |                  
|_______/    |__|  |__| |__| | _|   |_______/                   
                                                                
 __    ___    ______   ______                                   
/_ |  / _ \  |____  | |____  |                                  
 | | | (_) |     / /      / /                                   
 | |  \__, |    / /      / /                                    
 | |    / /    / /      / /                                     
 |_|   /_/    /_/      /_/                                      
                                                                
                                                                                
                                                                                                                
""")
    print("\nA hostile Imperial fleet has jumped from Hyperspace and is\
         poised for attack!")
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
    player_name = input("\nGreetings commander, please enter your name...")
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
        self.column_list = [6]
        self.row_list = [6]
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
            print('%d|%s' % (row_number, ' '.join(row)))
            row_number += 1
        print(f"\nLives left: {self.lives}\n")

    def place_ships(self, ship_size, row, column, orientation):
        """
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
        Allows user to place ships on board.
        """
        print("Please select horizontal\u2192 or vertical\u2193 orientation")
        print("Ship coordinates must not overlap")
        if ship_size == 4:
            print(" ")
            print("We have stolen an imperial Star Destroyer(3), let's deploy it now!\n")
        elif ship_size == 3:
            print(" ")
            print("Let's deploy a CR90 Corvette(3)\n")
        elif ship_size == 2:
            print(" ")
            print("Let's deploy the Millennium Falcon(2)\n")
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
                column = input("Please select a column A-F: \n").upper()
                if not re.match("^[A-F]*$", column):
                    print("Beep...does not compute...please enter a letter A-F...")
                else:
                    column = self.col_letters_as_numbers[column]
                    break
            except KeyError:
                print("Please enter a letter A-F")
        while True:
            try:
                row = input("Please select a row 0-5:  \n")
                if row in self.valid_row_input:
                    row = int(row)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number 0-5")
        return orientation, column, row

    def populate_boards(self):
        """
        Populates boards
        """
        size_of_ships = [4, 3, 2, 1]
        for ship_size in size_of_ships:
            while True:
                if self.user == "computer":
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
        Int used to decide computer attack.
        """
        attack_random = random.randint(1, 2)
        return attack_random

    def comp_attack_column(self):
        """
        Holds logic for computers attack.
        Returns a value for the row based
        off last hit ship on comp_guess board.
        """
        column_hit = self.column_list[-1]
        if column_hit == 6:
            column = random.randint(0, 5)
            return column
        else:
            attack_random = self.random_number()
            if attack_random == 1:
                column = column_hit + 1
                return column
            elif attack_random == 2:
                column = column_hit - 1
                return column

    def comp_attack_row(self):
        """
        Holds the logic for computers attack.
        Returns a value for the column based
        off last hit ship on comp_guess board.
        """
        row_hit = self.row_list[-1]
        if row_hit == 6:
            row = random.randint(0, 6)
            return row
        else:
            attack_random = self.random_number()
            if attack_random == 1:
                row = row_hit + 1
                return row
            elif attack_random == 2:
                row = row_hit - 1
                return row

    def player_attack(self):
        """
        Prompts player to input attack coordinates.
        Uses comp AI methods to decide computer attack coordinates.
        Returns cooordinates to be used in the game.
        """
        while True:
            if self.user == "player":
                print("Sir, weapons are charged and ready!\n")
                try:
                    column = input("Please select a column A-F: \n").upper()
                    if not re.match("^[A-F]*$", column):
                        print("Sir, those coordinates are out of range...please enter a number 0-5")
                    else:
                        column = self.col_letters_as_numbers[column]
                        break
                except KeyError:
                    print("Sir, please enter a letter")
            elif self.user == "computer guess":
                column = self.comp_attack_column()
                if column == range(0, 6):
                    break
                else:
                    column = random.randint(0, 5)
                    break
        while True:
            if self.user == "player":
                try:
                    row = input("Please select a row 0-5")
                    if row in self.valid_row_input:
                        row = int(row)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Please Enter a number 0-5")
            elif self.user == "computer guess":
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
        one = self.attack_list[-1]
        two = self.attack_list[-2]
        three = self.attack_list[-3]
        four = self.attack_list[-4]
        sum_of_attack = one + two + three + four
        if sum_of_attack == 8:
            self.column_list.append(6)
            self.row_list.append(6)
        else:
            pass

    def lives_counter(self):
        """
        ohkjj
        """
        counter = 8
        for row in self.board:
            for column in row:
                if column == HIT:
                    counter -= 1
                    self.lives = counter
        return self.lives

def play_game(player_board, player_guess, computer_board, computer_guess):
    """
    giugiui
    """
    player_turn = 0
    computer_turn = 1
    player_lives = 8
    computer_lives = 8
    while True:
        if player_turn < computer_turn:
            player_guess.display_board()
            column, row = player_board.player_attack()
            if player_guess.board[row][column] == ALREADY_GUESSED:
                print("Sir, we have already fired on these coordinates!\n")
            elif player_guess.board[row][column] == HIT:
                print("Sir, we have already hit a ship at these coordinates!\n")
            elif computer_board.board[row][column] == SHIP:
                print(" ")
                print(END_OF_ROUND)
                print("Great shot Sir, we hit a ship!\n")
                player_guess.board[row][column] = HIT
                player_turn += 1
                player_guess.lives_counter()
                player_guess.display_board()
                computer_lives -= 1
                print("Brace yourself Sir, the enemy are attacking...")
                time.sleep(1)
                if computer_lives == 0:
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
        if computer_turn == player_turn:
            row, column = computer_guess.player_attack()
            if computer_guess.board[row][column] == ALREADY_GUESSED:
                pass
            elif computer_guess.board[row][column] == HIT:
                pass
            elif player_board.board[row][column] == SHIP:
                print("Sir, the enemy have hit one of our ships!\n")
                computer_turn += 1
                player_lives -= 1
                computer_guess.column_list.append(column)
                computer_guess.row_list.append(row)
                computer_guess.board[row][column] = HIT
                player_board.board[row][column] = HIT
                player_board.lives_counter()
                player_board.display_board()
                computer_guess.attack_list.append(0)
                time.sleep(1)
                if player_lives == 0:
                    print("Sir, our shields are depleted, we have lost!")
                    print(" ")
                    print(END_OF_ROUND)
                    break
            else:
                print("Sir, they have missed our ships!\n")
                computer_guess.board[row][column] = ALREADY_GUESSED
                computer_turn += 1
                player_board.display_board()
                computer_guess.attack_list.append(1)
                computer_guess.count_misses()
                time.sleep(2)


def play_again():
    """
    Gives the user a choice of quitting,
    or playing another game.
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


def new_game():
    """
    revrrev
    """
    start_screen()
    player_name = get_name()
    player_board = Board(player_name, "player")
    player_guess = Board("Space Radar", "player guess")
    computer_board = Board("ENEMY", "computer")
    computer_guess = Board("ENEMY GUESS", "computer guess")
    computer_board.populate_boards()
    player_board.display_board()
    player_board.populate_boards()
    time.sleep(1)
    print(END_OF_ROUND)
    print(" ")
    play_game(player_board, player_guess, computer_board, computer_guess)
    play_again()


new_game()