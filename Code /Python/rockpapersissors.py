"""This is here so Python stops yelling at me"""
print("Hello World")

print()

STR_TESTING = "This is a test"

def startagain():
    """This, when true, will restart the game"""
    maingame()

def maingame():
    """The main game"""
    print("Rock Paper Sissors")
    print()
    playerinput = input("What will you play? ")
    if isinstance(playerinput) != isinstance(STR_TESTING):
        print("no")

