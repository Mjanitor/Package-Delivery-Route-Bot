class Truck:
    def __init__(self, name):
        self.name = name
        self.packages = []

    def __str__(self):
        return f"This truck has {self.packages} packages."
