import pygame
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width, height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
x = 0
y = 0
moveX = 1
moveY = 1
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameBoard.fill(white)
    pygame.draw.rect(gameBoard, red, [x, y, 50, 50])
    x += moveX
    y += moveY
    # y += 1

    if x > width - 50:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - 50:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.update()