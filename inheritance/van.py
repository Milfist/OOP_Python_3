from inheritance.car import Car


class Van(Car):

    def __init__(self, color, wheels_number, velocity, power, charge):
        super().__init__(color, wheels_number, velocity, power)
        self.charge = charge

    def __str__(self):
        return super().__str__() + ' {}'.format(self.charge)
