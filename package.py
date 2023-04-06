# Package Class

class Package:
    def __init__(self, id, delivery_address, delivery_city, delivery_zip, delivery_deadline, weight, departure_time, arrival_time):
        self.id = id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __str__(self):
        print(self.id)

    # Updating Package Status
    def getStatus(self, input_time):
        if self.arrival_time  <= input_time:
            return "Delivered"
        if self.arrival_time > input_time >= self.departure_time:
            return "En Route"
        else:
            return "At Hub"
