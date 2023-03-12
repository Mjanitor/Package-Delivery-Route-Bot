import datetime

from truck import *
from package import *
from hashmap import *
import csv
import datetime

# Importing Package CSV data
with open("Resources/WGUPS Package File.csv", encoding='utf-8-sig') as csvfile:
    packageCSV = csv.reader(csvfile)
    packageList = list(packageCSV)

# Importing Distance CSV data
with open("Resources/WGUPS Distance Table.csv", encoding='utf-8-sig') as csvfile:
    distanceCSV = csv.reader(csvfile)
    distanceList = list(distanceCSV)

# Importing Address CSV data
with open("Resources/Address Indices.csv", encoding='utf-8-sig') as csvfile:
    addressCSV = csv.reader(csvfile)
    addressList = list(addressCSV)

# Reading CSV files to create packages with data, then adding them to the Hash Map
def load_packages(file_name, hash_table):
    for package in file_name:
        ID = package[0]
        address = package[1]
        city = package[2]
        state = package[3]
        zip = package[4]
        deadline = package[5]
        weight = package[6]
        status = "at the Hub"

        # Creating a new package object
        package = Package(ID, address, city, state, zip, deadline, weight, status)

        # Adding ethe new package
        hash_table.add(ID, package)

# Turning addresses into indices for distance calculation
def get_address_index(address):
    for entry in addressList:
        if entry[2] == address:
            return int(entry[0])

# Create Method to determine the distance between two addresses
def find_distance(x, y):
    distance = distanceList[x][y]

    # Flips the lookup index in case of empty distance value
    if distance == '':
        distance = distanceList[y][x]

    return distance

# Creating hash map
hashMap = HashMap()

# Creating Truck Objects
truck1 = Truck("Truck 1", 16, 18, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck2 = Truck("Truck 2", 16, 18, [3, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck3 = Truck("Truck 3", 16, 18, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

load_packages(packageList, hashMap)

# Main package delivery
def package_delivery(truck):
    # Nearest Neighbor Algorithm
    mileage = truck.mileage
    undelivered = []

    for package in truck.packages:
        undelivered.append(package)
        hashMap.get(str(package)).departure_time = truck.time

    current_package = undelivered[0]
    cur_package_address = addressList[get_address_index(hashMap.get(str(current_package)).address)][2]
    final_package_address = None
    distance = float(find_distance(get_address_index(truck.address), get_address_index(cur_package_address)))

    # Initial delivery
    truck.time += datetime.timedelta(hours=distance / 18)
    hashMap.get(str(current_package)).delivery_time = truck.time
    mileage += distance
    truck.address = cur_package_address
    undelivered.pop(undelivered.index(current_package))

    # Find the shortest package distance
    while len(undelivered) > 0:
        for package in undelivered:
            cur_package_address = addressList[get_address_index(hashMap.get(str(package)).address)][2]
            temp_distance = float(find_distance(get_address_index(truck.address), get_address_index(cur_package_address)))
            if temp_distance < distance:
                distance = temp_distance
                current_package = package
                final_package_address = cur_package_address

        # Updating tracking information
        truck.time += datetime.timedelta(hours=distance / 18)
        hashMap.get(str(current_package)).delivery_time = truck.time
        print(hashMap.get(str(current_package)).status)
        mileage += float(distance)
        truck.address = final_package_address
        undelivered.pop(undelivered.index(current_package))
        distance = 1000
        current_package = None

    truck.mileage = mileage

    # Accounting for first truck's return home
    if truck == truck1:
        truck.mileage += float(find_distance(get_address_index(truck.address), get_address_index("4001 South 700 East")))

    return round(truck.mileage, 2)

first_trip = package_delivery(truck1)
second_trip = package_delivery(truck2)
third_trip = package_delivery(truck3)

print(f"Total Miles: {first_trip + second_trip + third_trip}")

class Main:
    print("Welcome to the WGUPS Status Interface!")
    print("Here, you can check the status of any package at any time")
    time = input("Enter a time after 8AM (format: 08:00:00) to check the status of a package \n Type 'X' to exit. \n")
    if time.lower() == "x":
        exit()
    else:
        (h, m, s) = time.split(':')
        selection = input("Would you like all packages or just one?  If one, type 'solo': ")
        if selection == "solo":
            package_ID = input("Please enter the Package ID you would like to search: ")
            lookup_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            lookup_package = hashMap.get(str(package_ID))
            lookup_package.update_delivery_status(lookup_time)
            print(f"Departure Time: {lookup_package.departure_time}")
            print(f"Delivery Time: {lookup_package.delivery_time}")
            print(f"Package ID: {package_ID}, Status: {lookup_package.status}")
        else:
            #TODO: Implement all package statuses
            pass
