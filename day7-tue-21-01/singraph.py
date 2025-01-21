import pygame
import sys
import math

def f(x):
    return math.sin(x)

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

running = True
clock = pygame.time.Clock()

center_x = 300
center_y = 300
scale_x = 100
scale_y = 100
prev_x = -math.pi
prev_y = f(prev_x)

for x in range(0, 600):
    x = -math.pi + 2 * math.pi * x / 600
    y = f(x)
    pygame.draw.line(screen, (0, 0, 0), 
                    (center_x + x * scale_x, center_y - y * scale_y), 
                    (center_x + prev_x * scale_x, center_y - prev_y * scale_y))
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
