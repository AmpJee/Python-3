class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y


    def draw(self):
        print(f"{self.x}, {self.y}")
 

    def move(self):
        self.x += 1
        self.y += 1


if __name__ == "__main__":
    c = Circle(4, 5, 6)
    for i in range(4):
        c.move()
        c.draw()
        