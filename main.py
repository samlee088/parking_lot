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

class ParkingFloor:
    def __init__(self, spot_count):
        self.spots = [0] * spot_count
        self.vehicle_map = {}

    def park_vehicle(self, vehicle):
        size = vehicle.get_spot_size()

        l,r = 0,0
        while r < len(self.spots):
            if self.spots[r] != 0:
                l = r +1
            if r - 1 + 1 == size:
                # We found enough spots, park the vehicle
                for k in range(l, r + 1):
                    self.spots[k] = 1
                self.vehicle_map[vehicle] = [l,r]
                return True
            r += 1
        return False