from unittest import TestCase

from inheritance.bike import Bike
from inheritance.motorcycle import Motorcycle
from inheritance.vehicle import Vehicle


class MotorcycleTest(TestCase):

    def setUp(self):
        self.motorcycle = Motorcycle('Green', 2, 'sport', 250, 1000)

    def test_should_be_ok_when_create_new_motorcycle(self):
        self.assertEqual('Green', self.motorcycle.color)
        self.assertEqual(2, self.motorcycle.wheels_number)
        self.assertEqual('sport', self.motorcycle.bike_type)
        self.assertEqual(250, self.motorcycle.velocity)
        self.assertEqual(1000, self.motorcycle.power)
        self.assertIsInstance(self.motorcycle, Motorcycle)
        self.assertIsInstance(self.motorcycle, Bike)
        self.assertIsInstance(self.motorcycle, Vehicle)

    def test_should_be_ok_when_motorcycle_str(self):
        self.assertEqual('Green 2 sport 250 1000', self.motorcycle.__str__())

    def tearDown(self):
        del self.motorcycle
