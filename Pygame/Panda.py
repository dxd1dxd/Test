import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 532))
#coloring the background
rect(screen, (255, 175, 128), (0, 0, 800, 532))

#criating

polygon(screen,(0, 104, 55), [(430, 8), (406, 84), (415, 87), (440, 10)])
polygon(screen,(0, 104, 55), [(408, 96), (391, 151), (408, 157), (426, 102)])
polygon(screen,(0, 104, 55), [(395, 167), (395, 263), (421, 263), (421, 167)])
polygon(screen,(0, 104, 55), [(395, 275), (395, 360), (421, 360), (421, 275)])















pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()