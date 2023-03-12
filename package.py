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
        self.delivery_time = None

    def __str__(self):
        return f"This package has an ID of {self.id} and is currently {self.status}.  It is being delivered to {self.address}, {self.city}, {self.state} {self.zip}.  It weighs {self.weight} Kilos " \
               f"and must be delivered by {self.deadline}."
    def update_delivery_status(self, current_time):
        if self.delivery_time < current_time:
            self.status = "Delivered"
        elif self.delivery_time > current_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"