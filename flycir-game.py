import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window width and height
window_width = 800
window_height = 600
screen_color = (0, 0, 0)
circle_color = (255, 0, 255)
circle_radius = 20
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flying Circle")
clock = pygame.time.Clock()

class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Create a circle object
c = Circle(circle_radius, 0, 0)

vx = 6
vy = 7

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(screen_color)
    c.move(vx, vy)

    if c.x > window_width or c.x < 0:
        vx = -vx
    if c.y > window_height or c.y < 0: 
        vy = -vy

    pygame.draw.circle(screen, circle_color, (c.x, c.y), c.radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()