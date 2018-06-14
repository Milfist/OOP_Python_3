from unittest import TestCase

from inheritance.car import Car
from inheritance.vehicle import Vehicle
from inheritance.van import Van


class VanTest(TestCase):

    def setUp(self):
        self.van = Van('Blue', 4, 180, 2000, 3500)

    def test_should_be_ok_when_create_new_van(self):
        self.assertEqual('Blue', self.van.color)
        self.assertEqual(4, self.van.wheels_number)
        self.assertEqual(180, self.van.velocity)
        self.assertEqual(2000, self.van.power)
        self.assertEqual(3500, self.van.charge)
        self.assertIsInstance(self.van, Van)
        self.assertIsInstance(self.van, Car)
        self.assertIsInstance(self.van, Vehicle)

    def test_should_be_ok_when_call_str(self):
        self.assertEqual('Blue 4 180 2000 3500', self.van.__str__())

    def tearDown(self):
        del self.van
