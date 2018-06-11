from inheritance.vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, color, wheels_number, bike_type):
        super().__init__(color, wheels_number)
        self.bike_type = bike_type

    def __str__(self):
        return super().__str__() + ' {}'.format(self.bike_type)
