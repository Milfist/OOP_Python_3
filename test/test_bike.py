from unittest import TestCase

from inheritance.bike import Bike
from inheritance.vehicle import Vehicle


class BikeTest(TestCase):

    def setUp(self):
        self.bike = Bike('Green', 2, 'sport')

    def test_should_be_ok_when_create_new_bike(self):
        self.assertEqual('Green', self.bike.color)
        self.assertEqual(2, self.bike.wheels_number)
        self.assertEqual('sport', self.bike.bike_type)
        self.assertIsInstance(self.bike, Bike)
        self.assertIsInstance(self.bike, Vehicle)

    def test_should_be_ok_when_bike_str(self):
        self.assertEqual('Green 2 sport', self.bike.__str__())
