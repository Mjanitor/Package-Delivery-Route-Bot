class Package:
    def __init__(self, id, address, deadline, city, state, zip, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return f"This package has an ID of {self.id} and is currently {self.status}.  It is being delivered to {self.address}, {self.city}, {self.state} {self.zip}.  It weighs {self.weight} Kilos " \
               f"and must be delivered by {self.deadline}."

    def update_delivery_status(self, lookup_time):
        if self.delivery_time < lookup_time:
            self.status = "Delivered"
        elif self.departure_time > lookup_time:
            self.status = "At Hub"
        else:
            self.status = "En Route"