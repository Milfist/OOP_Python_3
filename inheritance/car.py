from inheritance.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, color, wheels_number, velocity, power):
        super().__init__(color, wheels_number)
        self.velocity = velocity
        self.power = power

    def __str__(self):
        return super().__str__() + ' {} {}'.format(self.velocity, self.power)

