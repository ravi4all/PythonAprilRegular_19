import pygame, random
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width, height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 0,0,255
green = 0,255,0
yellow = 255,255,0
pink = 0,255,255
color_1 = 255,0,255
colors = [blue,green,yellow,pink,color_1]

def score(count):
    msg = "Score : {}".format(count)
    font = pygame.font.SysFont(None, 30)
    text = font.render(msg, True, white)
    gameBoard.blit(text, (10,10))

def lifeCount(count):
    msg = "Chances Left : {}".format(count)
    font = pygame.font.SysFont(None, 30)
    text = font.render(msg, True, white)
    gameBoard.blit(text, (300, 10))

    font_2 = pygame.font.SysFont(None, 80)
    text_2 = font_2.render("Game Over", True, white)
    text_3 = font_2.render("Press SPACE to Restart", True, white)
    if count == 0:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game()

            gameBoard.blit(text_2, (400,200))
            gameBoard.blit(text_3, (200,300))
            pygame.display.update()

def game():
    x = 0
    y = 0
    moveX = 0

    barHeight, barWidth = 15, 120
    barX, barY = width // 2 - barWidth // 2, height - barHeight

    moveBallX = 0
    moveBallY = 0

    ballMoving = False
    ballOnBar = True

    ballRadius = 8

    brickList = []
    brickWidth = 100
    brickHeight = 25
    no_of_bricks = width // brickWidth
    for row in range(2,7):
        for col in range(no_of_bricks):
            brickList.append(pygame.Rect(101 * col, 30 * row, brickWidth, brickHeight))

    count = 0
    life = 3
    clock = pygame.time.Clock()
    FPS = 100

    randomBrick = random.choice(brickList)
    power_bar = pygame.Rect(randomBrick.x, randomBrick.y, randomBrick.width, randomBrick.height)
    power_bar_drop = 0
    while True:
        if ballOnBar:
            ballX, ballY = barX + barWidth // 2, barY - ballRadius

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 10
                elif event.key == pygame.K_LEFT:
                    moveX = -10
                elif event.key == pygame.K_SPACE:
                    ballMoving = True
                    ballOnBar = False
            elif event.type == pygame.KEYUP:
                moveX = 0

        gameBoard.fill(black)

        if ballMoving:
            moveBallX = -5
            moveBallY = -5
            ballMoving = False

        barX += moveX
        ballX += moveBallX
        ballY += moveBallY

        barRect = pygame.draw.rect(gameBoard, white,[barX, barY, barWidth, barHeight])
        pygame.draw.circle(gameBoard, yellow, [ballX, ballY], ballRadius)
        ballRect = pygame.Rect(ballX, ballY, 16,16)

        for i in range(len(brickList)):
            color = random.choice(colors)
            pygame.draw.rect(gameBoard, color, brickList[i])

        pygame.draw.rect(gameBoard, white, power_bar)

        if not ballOnBar and ballRect.colliderect(barRect):
            moveBallY = -5
            # moveBallX = -1

        if ballRect.colliderect(power_bar):
            power_bar_drop = 4

        power_bar.y += power_bar_drop

        if barRect.colliderect(power_bar):
            barWidth = 150
            # del power_bar

        for i in range(len(brickList)):
            if ballRect.colliderect(brickList[i]):
                moveBallY = 5
                count += 1
                del brickList[i]
                FPS += 2
                break

        if x > width - 50:
            moveX = -5
        elif x < 0:
            moveX = 5

        if ballX > width - 8:
            moveBallX = -5
        elif ballX < -8:
            moveBallX = 5
        elif ballY > height + height:
            ballOnBar = True
            moveBallY = 0
            moveBallX = 0
            life -= 1
        elif ballY < -8:
            moveBallY = 5

        score(count)
        lifeCount(life)

        pygame.display.update()
        clock.tick(FPS)

game()