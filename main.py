""" OOP python application for a parking lot system design """


class Vehicle:
    """ size """
    def __init__(self, spot_size):
        self.spot_size = spot_size

    def get_spot_size(self):
        return self.spot_size
    


class Driver:

    def __init__(self, id, vehicle):
        self.id = id
        self.vehicle = vehicle
        self.payment_due = 0
    
    def get_vehicle(self):
        return self.vehicle

    def get_id(self):
        return self.id
    
    def charge(self, amount):
        self.payment_due += amount

class Car(Vehicle):
    def __init__(self):
        super().__init__(1)

class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)

class SemiTruck(Vehicle):
    def __init__(self):
        super().__init__(3)

