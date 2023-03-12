class Truck:
    def __init__(self, name, limit, speed, packages, mileage, address, departure_time):
        self.name = name
        self.limit = limit
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure_time = departure_time

    def __str__(self):
        return f"This truck has {self.packages} packages."
