class Vehicle:

    def __init__(self, color, wheels_number):
        self.color = color
        self.wheels_number = wheels_number

    def __str__(self):
        return '{} {}'.format(self.color, self.wheels_number)
