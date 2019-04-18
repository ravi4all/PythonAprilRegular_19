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
moveX = 0
moveY = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    gameBoard.fill(white)
    pygame.draw.rect(gameBoard, red, [x, y, 50, 50])
    x += moveX
    y += moveY
    # y += 1

    if x > width:
        x = -50
    elif x < -50:
        x = width
    elif y > height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()