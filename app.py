from models.point import Point
from models.rectangle import Rectangle


def main():
    point_a = Point(2, 3)
    point_b = Point(5, 5)

    print('El punto a es:')
    point_a.__str__()

    print('El punto b es:')
    point_b.__str__()

    print('El punto a se encuentra en: {}'.format(point_a.quadrant()))
    print('El punto b se encuentra en: {}'.format(point_b.quadrant()))

    vector_a, vector_b = point_a.vector(point_b.axis_x, point_b.axis_y)
    print('El vector resultante: ({}, {})'.format(vector_a, vector_b))

    vector_a, vector_b = point_b.vector(point_a.axis_x, point_a.axis_y)
    print('El vector resultante: ({}, {})'.format(vector_a, vector_b))

    print('La distancia entre los puntos es: {}'.format(point_a.distance(point_b.axis_x, point_b.axis_y)))

    rectangle = Rectangle(point_a, point_b)

    print('La base del rectangulo es {}'.format(rectangle.base))
    print('La altura del rectangulo es {}'.format(rectangle.height))
    print('El area del rectangulo es igual a {}'.format(rectangle.area()))


if __name__ == "__main__":
    main()
