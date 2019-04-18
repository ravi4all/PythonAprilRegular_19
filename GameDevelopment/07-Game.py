import pygame, random
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width, height))

img = pygame.image.load("assets/frog.png")
sound_1 = pygame.mixer.Sound("assets/point.wav")

white = 255,255,255
black = 0,0,0
red = 255,0,0
x = 0
y = 0
moveX = 0
moveY = 0

x1 = random.randint(0, width - 50)
y1 = random.randint(0, height - 50)

snakeWidth = 50
snakeLength = 1
snakeList = []

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(gameBoard, red, [snakeList[i][0],
                                          snakeList[i][1], 50,50])

def score(counter):
    msg = "Score : {}".format(counter)
    font = pygame.font.SysFont(None, 30)
    text = font.render(msg, True, black)
    gameBoard.blit(text, (10,10))

FPS = 100
clock = pygame.time.Clock()

counter = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 5
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -5
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 5
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -5
                moveX = 0

    gameBoard.fill(white)
    rect_1 = pygame.draw.rect(gameBoard, red, [x, y, snakeWidth, 50])
    # rect_2 = pygame.draw.rect(gameBoard, black, [x1, y1, 50, 50])
    rect_2 = pygame.Rect(x1, y1, 50, 50)
    gameBoard.blit(img, (x1, y1))
    x += moveX
    y += moveY
    # y += 1

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)
    snakeList.append(snakeHead)

    snake(snakeList)

    if len(snakeList) > snakeLength:
        del snakeList[0]

    if rect_2.colliderect(rect_1):
        x1 = random.randint(0, width - 50)
        y1 = random.randint(0, height - 50)
        # snakeWidth += 10
        sound_1.play()
        snakeLength += 10
        FPS += 5
        counter += 1

    score(counter)

    if x > width:
        x = -50
    elif x < -50:
        x = width
    elif y > height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()
    clock.tick(FPS)