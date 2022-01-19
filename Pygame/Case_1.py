import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((300, 300))
#coloring the background
rect(screen, (210, 214, 255), (0, 0, 300, 300))
#creating a face
circle(screen, (255, 249, 48), (150, 150), 98)
circle(screen, (0, 0, 0), (150, 150), 100, 2)
#creating a mouth
rect(screen, (0, 0, 0), (90, 200, 120, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()