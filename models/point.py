import math


class Point:

    def __init__(self, axis_x=0, axis_y=0):
        self.axis_x = axis_x
        self.axis_y = axis_y

    def __str__(self):
        print('({}, {})'.format(self.axis_x, self.axis_y))

    def quadrant(self):
        r = ''
        if self.axis_x == 0 and self.axis_y == 0:
            r = 'Origin'
        elif self.axis_x > 0 and self.axis_y > 0:
            r = 'Quadrant 1'
        elif self.axis_x < 0 < self.axis_y:
            r = 'Quadrant 2'
        elif self.axis_x < 0 > self.axis_y:
            r = 'Quadrant 3'
        elif self.axis_x > 0 > self.axis_y:
            r = 'Quadrant 4'
        return r

    def vector(self, axis_x, axis_y):
        return self.axis_x - axis_x, self.axis_y - axis_y

    def distance(self, axis_x, axis_y):
        return math.sqrt((axis_x - self.axis_x) ** 2 + (axis_y - self.axis_y) ** 2)
