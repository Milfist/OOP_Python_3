from Python_3_OOP.models.Point import Point
from Python_3_OOP.models.Rectangle import Rectangle


def main():
    point_a = Point(2, 3)
    point_b = Point(5, 5)
    rectangle = Rectangle(point_a, point_b)

    print(point_a.quadrant())
    print(point_b.quadrant())

    vector_a, vector_b = point_a.vector(point_b.axis_x, point_b.axis_y)
    print('El vector resultante: ({}, {})'.format(vector_a, vector_b))

    vector_a, vector_b = point_b.vector(point_a.axis_x, point_a.axis_y)
    print('El vector resultante: ({}, {})'.format(vector_a, vector_b))

    print('La distancia entre los puntos es: {}'.format(point_a.distance(point_b.axis_x, point_b.axis_y)))


if __name__ == "__main__":
    main()
