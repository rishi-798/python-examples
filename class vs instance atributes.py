class Point:
    default_color = "red"


    def __init__(self, x, y, balls):
        self.x = x
        self.y = y
        self.balls = "dummy"

    def draw(self):
        print(f"Point({self.x}, {self.y})")

point = Point(1,2, "dummy")
point.draw()
print(point.x)
