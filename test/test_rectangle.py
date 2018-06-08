import unittest
from models.Point import Point
from models.Rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def setUp(self):
        mock_point_a = Point(2, 3)
        mock_point_b = Point(5, 5)
        self.mock_rectangle = Rectangle(mock_point_a, mock_point_b)

    def test_should_be_ok_when_create_empty_rectangle(self):
        rectangle = Rectangle()
        self.assertEquals(rectangle.base, 0)
        self.assertEquals(rectangle.height, 0)
        self.assertEquals(rectangle.area(), 0)

    def test_should_be_base_when_get_base(self):
        self.assertEqual(3, self.mock_rectangle.base)

    def test_should_be_base_when_get_height(self):
        self.assertEqual(2, self.mock_rectangle.height)

    def test_should_be_area_when_call_get_area(self):
        self.assertEqual(6, self.mock_rectangle.area())


if __name__ == '__main__':
    unittest.main()