from inheritance.bike import Bike


class Motorcycle(Bike):

    def __init__(self, color, wheels_number, bike_type, velocity, power):
        super().__init__(color, wheels_number, bike_type)
        self.velocity = velocity
        self.power = power

    def __str__(self):
        return super().__str__() + ' {} {}'.format(self.velocity, self.power)
