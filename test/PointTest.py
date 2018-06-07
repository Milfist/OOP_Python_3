import unittest
from ..models.Point import Point


class PointTest(unittest.TestCase):

    def test_should_be_Quadrant_1_when_call_quadrant_with_point(self):
        self.assertEqual(Point(3, 2).quadrant(), 'Quadrant 1')

    def test_should_be_Quadrant_2_when_call_quadrant_with_point(self):
        self.assertEqual(Point(-5, 2).quadrant(), 'Quadrant 2')

    def test_should_be_Quadrant_3_when_call_quadrant_with_point(self):
        self.assertEqual(Point(-5, -5).quadrant(), 'Quadrant 3')

    def test_should_be_Quadrant_4_when_call_quadrant_with_point(self):
        self.assertEqual(Point(5, -2).quadrant(), 'Quadrant 4')

    def test_should_be_Origin_when_call_quadrant_with_point(self):
        self.assertEqual(Point().quadrant(), 'Origin')

    def test_should_be_vector_ok_when_call_vector_with_point(self):
        vector_a, vector_b = Point(5, 5).vector(2, 3)
        self.assertEqual(3, vector_a)
        self.assertEqual(2, vector_b)

    def test_should_be_distance_ok_when_call_distance_between_two_points(self):
        self.assertEqual(3.605551275463989, Point(2, 3).distance(5, 5))


if __name__ == '__main__':
    unittest.main()
