class Truck:
    def __init__(self, name, limit, speed, packages, mileage, address):
        self.name = name
        self.limit = limit
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.address = address

    def __str__(self):
        return f"This truck has {self.packages} packages."
