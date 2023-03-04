class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight

    def __str__(self):
        return f"This package has an ID of {self.id}.  It is being delivered to {self.address}, {self.city}, {self.state} {self.zip}.  It weighs {self.weight} Kilos " \
               f"and must be delivered by {self.deadline}."