import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 532))
#coloring the background

rect(screen, (255, 175, 128), (0, 0, 800, 532))

#creating a bamboo trunk

polygon(screen, (0, 104, 55), [(430, 8), (406, 84), (415, 87), (440, 10)])
aalines(screen, (0, 104, 55), True, [(430, 8), (406, 84), (416, 86), (441, 11)])
polygon(screen, (0, 104, 55), [(408, 96), (391, 151), (408, 157), (426, 102)])
aalines(screen, (0, 104, 55), True, [(408, 96), (391, 151), (409, 158), (427, 103)])
polygon(screen, (0, 104, 55), [(395, 167), (395, 263), (421, 263), (421, 167)])
polygon(screen, (0, 104, 55), [(395, 275), (395, 360), (421, 360), (421, 275)])

#creating bamboo branches
arc(screen, (0, 104, 55), (438, 6, 344, 208), math.radians(100), math.radians(170), 2)
arc(screen, (0, 104, 55), (415, 120, 176, 291), math.radians(80), math.radians(150), 2)
arc(screen, (0, 104, 55), (203, 161, 195, 181), math.radians(20), math.radians(115), 2)
arc(screen, (0, 104, 55), (3, 42, 409, 375), math.radians(30), math.radians(95), 2)












pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()