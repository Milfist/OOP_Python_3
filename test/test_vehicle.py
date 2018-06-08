from unittest import TestCase

from inheritance.vehicle import Vehicle


class VehicleTest(TestCase):

    def setUp(self):
        self.vehicle = Vehicle('Blue', 4)

    def test_should_be_ok_when_create_new_vehicle(self):
        self.assertEqual('Blue', self.vehicle.color)
        self.assertEqual(4, self.vehicle.wheels_number)
        self.assertIsInstance(self.vehicle, Vehicle)

    def test_should_be_ok_when_call_str_function(self):
        self.assertEqual('Blue 4', self.vehicle.__str__())
