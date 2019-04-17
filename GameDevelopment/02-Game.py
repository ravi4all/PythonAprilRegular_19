import pygame
pygame.init()

gameBoard = pygame.display.set_mode((1000,500))

white = 255,255,255
black = 0,0,0
red = 255,0,0
gameBoard.fill(white)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # quit pygame
            pygame.quit()
            # quit python
            quit()

    pygame.display.update()