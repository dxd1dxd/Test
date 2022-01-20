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
rect(screen, (0, 0, 0), (95, 200, 110, 20))
#creating eyes
circle(screen, ('#ff0000'), (100, 120), 20)
circle(screen, (0, 0, 0), (100, 120), 22, 2)
circle(screen, (0, 0, 0), (100, 120), 10)

circle(screen, ('#ff0000'), (200, 120), 15)
circle(screen, (0, 0, 0), (200, 120), 17, 2)
circle(screen, (0, 0, 0), (200, 120), 7)

#creating eyebrows
polygon(screen, (0, 0, 0), [(50, 50), (40, 60), (130, 110), (140, 100)])
polygon(screen, (0, 0, 0), [(170, 110), (160, 100), (230, 70), (240, 80)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()