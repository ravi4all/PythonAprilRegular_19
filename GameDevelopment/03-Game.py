import pygame
pygame.init()

gameBoard = pygame.display.set_mode((1000,500))

white = 255,255,255
black = 0,0,0
red = 255,0,0
gameBoard.fill(white)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen, color, [x,y,w,h]
    pygame.draw.rect(gameBoard, red, [0,0,50,50])

    # screen, color, [x,y], radius
    pygame.draw.circle(gameBoard, red, [100,100],80)

    pygame.display.update()