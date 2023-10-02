"""This is here so Python stops yelling at me"""
import random
print("\nRock Paper Sissors")

print()

STR_TESTING = "This is a test"


def has_number(input_string):
    """Checks if a string has a digit in it"""
    return any(char.isdigit() for char in input_string)

def start_again():
    """This, when true, will restart the game"""
    player_action = input('Do you want to play again? ')
    player_action = player_action.lower()
    if player_action == "yes" or player_action == "y":
        main_game()

def main_game():
    """The main game"""
    player_input = input('What will you play? ')

    while has_number(player_input):
        print("You must chose Rock, Paper, or, Sissors!\n")
        player_input = input('What will you play? ')
        player_input = player_input.lower()

    while not(player_input == "rock" or player_input == "paper" or player_input == "sissors"):
        print("You must chose Rock, Paper, or, Sissors!\n")
        player_input = input('What will you play? ')
        player_input = player_input.lower()

    comp_move = random.randint(0,2)
    #0 - rock 1 - paper 2 - sissors 

    if player_input == "rock":
        if comp_move == 0:
            print("Computer plays rock \nTie!")
        elif comp_move == 1:
            print("Computer plays paper \nComputer wins!")
        else:
            print("Computer plays sissors \nYou Win!")
    elif player_input == "paper":
        if comp_move == 0:
            print("Computer plays rock \nYou Win!")
        elif comp_move == 1:
            print("computer plays paper \nTie!")
        else:
            print("Computer plays sissors \nComputer Wins!")
    else:
        if comp_move == 0:
            print("Computer plays rock \nComputer Wins!")
        elif comp_move == 1:
            print("Computer plays paper \nYou Win!")
        else:
            print("Computer plays sissors \nTie!")

    start_again()



main_game()
