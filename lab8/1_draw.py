import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((400, 400))

center = [200, 200]
radius = 100

screen.fill((200, 200, 200))
circle(screen, (255, 255, 0), center, radius)
circle(screen, (0, 0, 0), center, radius, width=1)

rect(screen, (0, 0, 0), (center[0] - radius//2, center[1]+radius//2, radius, radius//5))

circle(screen, (255, 0, 0), (center[0]-radius//2, center[1]-radius//4), radius//4.5)
circle(screen, (0, 0, 0), (center[0]-radius//2, center[1]-radius//4), radius//4.5, width=1)
circle(screen, (0, 0, 0), (center[0]-radius//2, center[1]-radius//4), radius//11)

circle(screen, (255, 0, 0), (center[0]+radius//2, center[1]-radius//4), radius//6)
circle(screen, (0, 0, 0), (center[0]+radius//2, center[1]-radius//4), radius//6, width=1)
circle(screen, (0, 0, 0), (center[0]+radius//2, center[1]-radius//4), radius//13)

rect(screen, (0, 0, 0), (center[0] - radius, center[1] - radius, radius, radius//5))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
