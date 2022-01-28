import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 532))
# coloring the background

screen.fill((0, 0, 0))
# creating Surface for draw bamboo
surf_one = pygame.Surface((450, 380))
surf_one.fill((255, 175, 128))

# creating a bamboo trunk

polygon(surf_one, (0, 104, 55), [(430, 8), (406, 84), (415, 87), (440, 10)])
aalines(surf_one, (0, 104, 55), True, [(430, 8), (406, 84), (416, 86), (441, 11)])
polygon(surf_one, (0, 104, 55), [(408, 96), (391, 151), (408, 157), (426, 102)])
aalines(surf_one, (0, 104, 55), True, [(408, 96), (391, 151), (409, 158), (427, 103)])
polygon(surf_one, (0, 104, 55), [(395, 167), (395, 263), (421, 263), (421, 167)])
polygon(surf_one, (0, 104, 55), [(395, 275), (395, 360), (421, 360), (421, 275)])

# creating bamboo branches
# arc(screen, (0, 104, 55), (438, 6, 344, 208), math.radians(100), math.radians(170), 2)
# arc(screen, (0, 104, 55), (415, 120, 176, 291), math.radians(80), math.radians(150), 2)
#arc(screen, (0, 104, 55), (203, 161, 195, 181), math.radians(20), math.radians(115), 2)
# arc(screen, (0, 104, 55), (3, 42, 409, 375), math.radians(30), math.radians(95), 2)

# creating bamboo leaves

surf = pygame.Surface((100, 100))
surf.fill((255, 175, 128))
ellipse(surf, (0, 104, 55), (0, 0, 10, 50))
ellipse(surf, (0, 104, 55), (30, 5, 10, 50))
ellipse(surf, (0, 104, 55), (50, 5, 10, 50))
ellipse(surf, (0, 104, 55), (70, 5, 10, 50))
ellipse(surf, (0, 104, 55), (90, 10, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 30), (490, 0))
arc(surf_one, (0, 104, 55), (438, 6, 344, 208), math.radians(100), math.radians(170), 2)

surf = pygame.Surface((100, 100))
surf.fill((255, 175, 128))
ellipse(surf, (0, 104, 55), (0, 5, 10, 50))
ellipse(surf, (0, 104, 55), (30, 5, 10, 50))
ellipse(surf, (0, 104, 55), (50, 5, 10, 50))
ellipse(surf, (0, 104, 55), (70, 5, 10, 50))
ellipse(surf, (0, 104, 55), (90, 5, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 160), (190, 0))
arc(surf_one, (0, 104, 55), (3, 42, 409, 375), math.radians(30), math.radians(95), 2)

surf = pygame.Surface((100, 100))
surf.fill((255, 175, 128))
ellipse(surf, (0, 104, 55), (0, 0, 10, 50))
ellipse(surf, (0, 104, 55), (30, 5, 10, 50))
ellipse(surf, (0, 104, 55), (50, 5, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 30), (460, 100))
arc(surf_one, (0, 104, 55), (415, 120, 176, 291), math.radians(80), math.radians(150), 2)

surf = pygame.Surface((60, 60))
surf.fill((255, 175, 128))
ellipse(surf, (0, 104, 55), (0, 0, 10, 50))
ellipse(surf, (0, 104, 55), (30, 5, 10, 50))
ellipse(surf, (0, 104, 55), (50, 5, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 160), (260, 160))
arc(surf_one, (0, 104, 55), (203, 161, 195, 181), math.radians(20), math.radians(115), 2)

screen.blit(surf_one, (200, 0))




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
