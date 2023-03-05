class Package:
    def __init__(self, id, address, deadline, city, zip, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.status = status

    def __str__(self):
        return f"This package has an ID of {self.id} and is currently {self.status}.  It is being delivered to {self.address}, {self.city} {self.zip}.  It weighs {self.weight} Kilos " \
               f"and must be delivered by {self.deadline}."
    def check_location(self):
        print(f"Package {self.id} is currently {self.status}")