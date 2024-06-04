import pygame 
   
backgroundColor = (11, 191, 32)  
screen = pygame.display.set_mode((500, 700)) 
pygame.display.set_caption('Blackjack')  
screen.fill(backgroundColor) 
pygame.display.flip() 
running = True
triggerLock1 = True
triggerLock2 = True
cardDeck = (1, 1)

def createDeck():
    return ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))

def printCard(x, y, suit, value):
    temp = 2

while running: 
    if (triggerLock1 == True and triggerLock2 == True):
        triggerLock2 = False
        cardDeck = createDeck()
    print cardDeck[2][3]
    for event in pygame.event.get():      
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()