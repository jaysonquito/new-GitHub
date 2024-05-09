import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREN_HEIGHT))

player = pygame.Rect((300,250,50,50))

run = True
while run:

    pygame.draw.rect(screen, (255, 0 ,0), player)

