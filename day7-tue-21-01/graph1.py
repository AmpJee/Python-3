import pygame
import sys


def f(x):
    return x

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

running = True
clock = pygame.time.Clock()

for x in range(0, 600):
    y = f(x)
    screen.set_at((x, 600 - y), (0, 0, 0))
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
sys.exit()
