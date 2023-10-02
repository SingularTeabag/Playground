"""This is here so Python stops yelling at me"""
print("Hello World")

print()

STR_TESTING = "This is a test"

def has_number(input_string):
    """Checks if a string has a digit in it"""
    return any(char.isdigit() for char in input_string)

def start_again():
    """This, when true, will restart the game"""
    main_game()

def main_game():
    """The main game"""
    print("Rock Paper Sissors")
    print()
    player_input = input('What will you play? ')
    while has_number(player_input):
        print("You must chose Rock, Paper, or, Sissors!\n")
        player_input = input('What will you play? ')
    while not(player_input == "rock" or player_input == "paper" or player_input == "sissors"):
        print("You must chose Rock, Paper, or, Sissors!\n")
        player_input = input('What will you play? ')

main_game()

print("why")
