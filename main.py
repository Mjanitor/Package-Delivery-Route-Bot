from truck import *
from package import *
from hashmap import *
import csv

def main():

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
    truck1 = Truck("Truck 1", 16, 18, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East")
    truck2 = Truck("Truck 2", 16, 18, [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East")
    truck3 = Truck("Truck 3", 16, 18, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East")

    load_packages(packageList, hashMap)

    # Main package delivery
    def package_delivery(truck):
        # Nearest Neighbor Algorithm
        mileage = truck.mileage
        undelivered = []
        hashMap.print()

        for package in truck.packages:
            undelivered.append(package)

        distance = 1000
        currentPackage = undelivered[0]
        curPackageAddress = addressList[get_address_index(hashMap.get(str(currentPackage)).address)][2]
        finalPackageAddress = None

        # Initial delivery
        mileage += float(find_distance(get_address_index(truck.address), get_address_index(curPackageAddress)))
        truck.address = curPackageAddress
        undelivered.pop(undelivered.index(currentPackage))

        # TODO: Find shortest package distance
        while len(undelivered) > 0:
            for package in undelivered:
                curPackageAddress = addressList[get_address_index(hashMap.get(str(package)).address)][2]
                tempDistance = float(find_distance(get_address_index(truck.address), get_address_index(curPackageAddress)))
                if tempDistance < distance:
                    distance = tempDistance
                    currentPackage = package
                    finalPackageAddress = curPackageAddress

            mileage += float(distance)
            #print(f"Final Package Number: {currentPackage}")
            #print(f"Final Truck Address: {truck.address}")
            truck.address = finalPackageAddress
            #print(f"Final Package Address: {finalPackageAddress}")
            #print(f"Current Mileage: {mileage}")
            #print("------------------------------------")
            undelivered.pop(undelivered.index(currentPackage))
            distance = 1000
            tempDistance = None
            currentPackage = None
            #print(f"{truck.name} undelivered Package Numbers: {undelivered}")

        truck.mileage = mileage

        # Accounting for the return home
        if truck == truck1:
            truck.mileage += float(find_distance(get_address_index(truck.address), get_address_index("4001 South 700 East")))

        return round(truck.mileage, 2)

    firstTrip = package_delivery(truck1)
    secondTrip = package_delivery(truck2)
    thirdTrip = package_delivery(truck3)

    print(f"Total Miles: {firstTrip + secondTrip + thirdTrip}")

if __name__ == "__main__":
    main()
