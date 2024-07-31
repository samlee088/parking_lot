
import datetime
import math

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
            if r - l + 1 == size:
                # We found enough spots, park the vehicle
                for k in range(l, r + 1):
                    self.spots[k] = 1
                self.vehicle_map[vehicle] = [l,r]
                return True
            r += 1
        return False

    def remove_vehicle(self, vehicle):
        start, end = self.vehicle_map[vehicle]
        for i in range(start, end + 1):
            self.spots[i] = 0
        del self.vehicle_map[vehicle]
    
    def get_parking_spots(self):
        return self.spots
    
    def get_vehicle_spots(self, vehicle):
        return self.vehicle_map.get(vehicle)
    
class ParkingGarage:
    def __init__(self, floor_count, spots_per_floor):
        self.parking_floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]

    def park_vehicle(self, vehicle):
        for floor in self.parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False
    
    def remove_vehicle(self, vehicle):
        for floor in self.parking_floors:
            if floor.get_vehicle_spots(vehicle):
                floor.remove_vehicle(vehicle)
                return True
        return False
    

class ParkingSystem:
    def __init__(self, parkingGarage, hourlyRate):
        self.parkingGarage = parkingGarage
        self.hourlyRate = hourlyRate
        self.timeParked = {}

    def park_vehicle(self, driver):
        currentHour = datetime.datetime.now().hour
        isParked = self.parkingGarage.park_vehicle(driver.get_vehicle())
        if isParked:
            self.timeParked[driver.get_id()] = currentHour
        return isParked
    
    def remove_vehicle(self, driver):
        if driver.get_id() not in self.timeParked:
            return False
        currentHour = datetime.datetime.now().hour
        timeParked = math.ceil(currentHour - self.timeParked[driver.get_id()])
        driver.charge(timeParked * self.hourlyRate)

        del self.timeParked[driver.get_id()]
        return self.parkingGarage.remove_vehicle(driver.get_vehicle())
    
parkingGarage = ParkingGarage(3, 2)
parkingSystem = ParkingSystem(parkingGarage, 5)

driver1 = Driver(1, Car())
driver2 = Driver(2, Limo())
driver3 = Driver(3, SemiTruck())

print(parkingSystem.park_vehicle(driver1))      # true
print(parkingSystem.park_vehicle(driver2))      # true
print(parkingSystem.park_vehicle(driver3))      # false

print(parkingSystem.remove_vehicle(driver1))    # true
print(parkingSystem.remove_vehicle(driver2))    # true
print(parkingSystem.remove_vehicle(driver3))    # false