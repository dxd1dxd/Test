import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 532))
# color name
PINK = (255, 175, 128)
GREEN = (0, 104, 55)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# coloring the background

screen.fill(PINK)
# creating Surface for draw bamboo
surf_one = pygame.Surface((650, 380))
surf_one.fill(PINK)

# creating a bamboo trunk

polygon(surf_one, GREEN, [(430, 8), (406, 84), (415, 87), (440, 10)])
aalines(surf_one, GREEN, True, [(430, 8), (406, 84), (416, 86), (441, 11)])
polygon(surf_one, GREEN, [(408, 96), (391, 151), (408, 157), (426, 102)])
aalines(surf_one, GREEN, True, [(408, 96), (391, 151), (409, 158), (427, 103)])
polygon(surf_one, GREEN, [(395, 167), (395, 263), (421, 263), (421, 167)])
polygon(surf_one, GREEN, [(395, 275), (395, 360), (421, 360), (421, 275)])

# creating bamboo leaves

surf = pygame.Surface((100, 100))
surf.fill(PINK)
ellipse(surf, GREEN, (0, 0, 10, 50))
ellipse(surf, GREEN, (30, 5, 10, 50))
ellipse(surf, GREEN, (50, 5, 10, 50))
ellipse(surf, GREEN, (70, 5, 10, 50))
ellipse(surf, GREEN, (90, 10, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 30), (490, 0))
arc(surf_one, GREEN, (438, 6, 344, 208), math.radians(100), math.radians(170), 2)

surf = pygame.Surface((100, 100))
surf.fill(PINK)
ellipse(surf, GREEN, (0, 5, 10, 50))
ellipse(surf, GREEN, (30, 5, 10, 50))
ellipse(surf, GREEN, (50, 5, 10, 50))
ellipse(surf, GREEN, (70, 5, 10, 50))
ellipse(surf, GREEN, (90, 5, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 160), (190, 0))
arc(surf_one, GREEN, (3, 42, 409, 375), math.radians(30), math.radians(95), 2)

surf = pygame.Surface((100, 100))
surf.fill(PINK)
ellipse(surf, GREEN, (0, 0, 10, 50))
ellipse(surf, GREEN, (30, 5, 10, 50))
ellipse(surf, GREEN, (50, 5, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 30), (460, 100))
arc(surf_one, GREEN, (415, 120, 176, 291), math.radians(80), math.radians(150), 2)

surf = pygame.Surface((60, 60))
surf.fill(PINK)
ellipse(surf, GREEN, (0, 0, 10, 50))
ellipse(surf, GREEN, (30, 5, 10, 50))
ellipse(surf, GREEN, (50, 5, 10, 50))
surf_one.blit(pygame.transform.rotate(surf, 160), (260, 160))
arc(surf_one, GREEN, (203, 161, 195, 181), math.radians(20), math.radians(115), 2)

screen.blit(surf_one, (0, 0))

# create new bamboo
surf_two = pygame.transform.scale(surf_one, (surf_one.get_width() // 3, surf_one.get_height() // 1.5))

surf_two.set_colorkey(PINK)
screen.blit(surf_two, (150, 150))

# creating a panda

surf_panda = pygame.Surface((300, 300))
surf_panda.fill(GREEN)
# creating body
ellipse(surf_panda, WHITE, (48, 45, 180, 111))
# creating ears
surf_ear_left = pygame.Surface((70, 30))
surf_ear_left.fill(GREEN)
rect(surf_ear_left, BLACK, (0, 1, 70, 30), border_top_left_radius = 50, border_top_right_radius = 30,
     border_bottom_left_radius = 0, border_bottom_right_radius = 10)
surf_panda.blit(pygame.transform.rotate(surf_ear_left, 40), (0, -2))

surf_ear_right = pygame.Surface.copy(surf_ear_left)
surf_panda.blit(pygame.transform.rotate(surf_ear_right, 320), (100, -2))

screen.blit(surf_panda, (432, 188))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
