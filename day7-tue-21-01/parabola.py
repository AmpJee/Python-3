import pygame
import sys


def f(x):
    return x**2

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

running = True
clock = pygame.time.Clock()

center_x = 300
center_y = 600
height = 4
scale = 600 / height
prev_x = -2
prev_y = f(prev_x)

for x in range(0, 600):
    x = -2 + 4 * x / 600
    y = f(x)
    pygame.draw.line(screen, (0, 0, 0), 
                    (center_x + x * scale, center_y - y * scale), 
                    (center_x + prev_x * scale, center_y - prev_y * scale))
    prev_x = x
    prev_y = y
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
sys.exit()
