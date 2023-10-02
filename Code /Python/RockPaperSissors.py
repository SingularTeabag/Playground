"""This is here so Python stops yelling at me"""
print("Hello World")

print()

def startagain():
    """This, when true, will restart the game"""
    maingame()

def maingame():
    """The main game"""
    print("Rock Paper Sissors") 
    print()
    playerInput = input("What will you play? ")

maingame()
