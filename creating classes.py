class Point:
    def draw(self):
        print('draw')

point = Point()
point(type(point))
print(isinstance(point, Point))