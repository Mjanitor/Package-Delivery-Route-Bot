# Truck Class
class Truck:
    def __init__(self, name, mileage, packages, location, time):
        self.name = name
        self.mileage = mileage
        self.packages = packages
        self.location = location
        self.time = time

    def __str__(self):
        return f"{self.name} and {self.packages}"
