"""
Libaries:
random used for random choice and number.
time is used to allow the user time to read
or simulate cpu decision making.
os is used to prevent overloading the display
re to check owner input is valid
matches a string.
"""
from classes.board import Board
import time
import os


# Global variables used to update game boards
END_OF_ROUND = "*" * 80
ALREADY_GUESSED = "0"
EMPTY = "\u2022"
SHIP = "§"
HIT = "X"


def start_screen():
    """
    Displays ASCII art to user
    each time the game begins.
    See credits for ASCII art.
    """
    print("\u001b[36m\nA long time ago, in a galaxy far, far away...\n")
    time.sleep(1.5)
    print("""\u001b[37m
                                                                                
    +             +             +               +          +       +       +       
         +                +            +                      +              + 
               +       +                       +    +                  +
 +       +            +        +                         +                  +     
                                 +        +                  +               +
       +           +                  +                         +         +
  +            +            +     +                +     +             +
        +               +          +      +                 +              +
   +          +         +                           +               +
+          +      +                       +  +            +                  +
                      +            +                          +
 +      +                +         +                               +        +
    +         +                 +                +        +
                   +                  +             +            +        +
    """)
    time.sleep(1.5)
    input("\u001b[33mPress Enter...")
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
    Validates username.
    Stores the name for use in the game.
    """
    while True:
        player_name = input("Welcome to BattleShips 1977, \
please enter your name... ")
        if player_name.isalpha():
            break
    return player_name


def back_story():
    """
    Displays a simple back story to the user.
    Uses time module to allow owner time to process the text.
    """
    print("A hostile Imperial fleet has jumped from Hyperspace and is \
preparing to attack!\n")
    time.sleep(2)
    os.system("clear")
    print("Scanners detect an Imperial Star Destroyer (length: 4)\n")
    time.sleep(1)
    print("An Imperial Light Cruiser (length: 3)\n")
    time.sleep(1)
    print("An Imperial Frigate (length: 2)\n")
    time.sleep(1)
    print("An Imperial T.I.E. Fighter (length: 1)\n")
    time.sleep(1)
    print("Take command of our own ships and destroy them before they \
can wipe us out.\n")
    time.sleep(1)
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
    time.sleep(1)
    print("\nThe battle area is a 6 x 6 grid...")
    time.sleep(1)
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


def play_game(player_board, player_guess, cpu_board, cpu_guess):
    """
    Contains game logic.
    Ensures user goes first.
    Adjust shield counter based on cpu and player guesses.
    """
    player_shields = 10
    cpu_shields = 10
    player_move = 0
    cpu_move = 1
    while True:
        if player_move < cpu_move:
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
                player_move += 1
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
                player_move += 1
                player_guess.display_board()
                print("C3PO: Brace yourself Sir, the enemy are attacking...")
                time.sleep(1.5)
        if cpu_move == player_move:
            row, column = cpu_guess.player_attack()
            if cpu_guess.board[row][column] == ALREADY_GUESSED:
                pass
            elif cpu_guess.board[row][column] == HIT:
                pass
            elif player_board.board[row][column] == SHIP:
                print("C3PO: Sir, the enemy have hit one of our ships!\n")
                time.sleep(1.5)
                cpu_move += 1
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
                cpu_move += 1
                player_board.display_board()
                cpu_guess.cpu_attacks.append(1)
                time.sleep(1.5)


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
            exit()
            return False
        else:
            print(" ")
            print("Please enter Y or N")
            player_response = input("Enter Y or N: \n").upper()


def main():
    """
    Runs all functions and methods above to start new game.
    Shows start screen,
    Prompts user for their name.
    Creates four instances of board class.
    Populates and updates relevant boards.
    """
    start_screen()
    player_name = get_name()
    print(f"\nWelcome, Commander {player_name}, may the force be with us!\n")
    time.sleep(1)
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
