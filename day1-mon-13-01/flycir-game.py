import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the window width and height
window_width = 800
window_height = 600
screen_color = (0, 0, 0)
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flying Circle")
clock = pygame.time.Clock()

class Circle:
    def __init__(self, radius, x, y, vx, vy, circle_color = (255, 0, 255)):
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.circle_color = circle_color

    def draw(self):
        pygame.draw.circle(screen, self.circle_color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > window_width or self.x < 0:
            self.vx = -self.vx
        if self.y > window_height or self.y < 0: 
            self.vy = -self.vy
        for i in circle_group:
            if i != self:
                if (self.x+self.radius) > (i.x-i.radius) and (self.x-self.radius) < (i.x+i.radius) and (self.y+self.radius) > (i.y-i.radius) and (self.y-self.radius) < (i.y+i.radius):
                    if self.x > i.x:
                        self.vx = -self.vx
                        self.x += 2
                    else:
                        self.vx = -self.vx
                        self.x -= 2
                    if self.y > i.y:
                        self.vy = -self.vy
                        self.y += 2
                    else:
                        self.vy = -self.vy
                        self.y -= 2


# Create a circle object
#number_of_circles = int(input("Enter the number of circles: "))
number_of_circles = 20
circle_group = []
for i in range(number_of_circles):
    radius = random.randint(5, 45)
    x = random.randint(0, window_width)
    y = random.randint(0, window_height)
    vx = random.randint(1, 5)
    vy = random.randint(1, 5)
    circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    c = Circle(radius, x, y, vx, vy, circle_color)
    circle_group.append(c)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(screen_color)
    
    for i in circle_group:
        i.move()
        i.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()