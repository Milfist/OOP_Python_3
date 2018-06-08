from unittest import TestCase

from inheritance.car import Car
from inheritance.vehicle import Vehicle


class CarTest(TestCase):

    def setUp(self):
        self.car = Car('Blue', 4, 180, 2000)

    def test_should_be_ok_when_create_new_car(self):
        self.assertEqual('Blue', self.car.color)
        self.assertEqual(4, self.car.wheels_number)
        self.assertEqual(180, self.car.velocity)
        self.assertEqual(2000, self.car.power)
        self.assertIsInstance(self.car, Car)
        self.assertIsInstance(self.car, Vehicle)

    def test_should_be_ok_when_call_str(self):
        self.assertEqual('Blue 4 180 2000', self.car.__str__())

