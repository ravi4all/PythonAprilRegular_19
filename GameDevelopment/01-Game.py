import pygame
pygame.init()

gameBoard = pygame.display.set_mode((1000,500))

# rgb - red, green, blue
# 0 - 255
white = 255,255,255
black = 0,0,0
red = 255,0,0
# color_1 = 120,200,210
gameBoard.fill(white)
pygame.display.update()