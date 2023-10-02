"""This needs to be here so python doesnt yell at me"""

print("Hello World")

def startagain():
    """it starts the game again."""
    maingame()

def maingame():
    """This is the main code of the game."""
    print("Rock Paper Sissors")
    print()
    playerinput = input("What will you play? ")

    playerinput = playerinput.lower()



print()
maingame()
