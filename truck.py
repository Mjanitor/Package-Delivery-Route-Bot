class Truck:
    def __init__(self, name, packages):
        self.name = name
        self.packages = packages

    def __str__(self):
        return f"This truck has {self.packages} packages."
