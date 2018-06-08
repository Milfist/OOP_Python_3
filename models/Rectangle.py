from models.Point import Point


class Rectangle:

    base = 0.0
    height = 0.0

    def __init__(self, point_a=Point(), point_b=Point()):
        self.point_a = point_a
        self.point_b = point_b
        self.__base()
        self.__height()

    def __base(self):
        self.base = abs(self.point_b.axis_x - self.point_a.axis_x)

    def __height(self):
        self.height = abs(self.point_b.axis_y - self.point_a.axis_y)

    def area(self):
        return self.base * self.height
