from truck import *
from package import *
from hashmap import *
import csv

def main():

    # Importing Package CSV data
    with open("Resources/WGUPS Package File.csv", encoding='utf-8-sig') as csvfile:
        packageCSV = csv.reader(csvfile)
        packageList = list(packageCSV)
        print(packageList)

    print("----------------------------------------------------------------------------")

    # Importing Distance CSV data
    with open("Resources/WGUPS Distance Table.csv", encoding='utf-8-sig') as csvfile:
        distanceCSV = csv.reader(csvfile)
        distanceList = list(distanceCSV)
        print(distanceList)

    print("----------------------------------------------------------------------------")

    # Importing Address CSV data
    with open("Resources/Address Indices.csv", encoding='utf-8-sig') as csvfile:
        addressCSV = csv.reader(csvfile)
        addressList = list(addressCSV)
        print(addressList)

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

    print(find_distance(get_address_index("4001 South 700 East"), get_address_index("3575 W Valley Central Station bus Loop")))

    # Creating hash map
    hashMap = HashMap()

    # Creating Truck Objects
    truck1 = Truck("Truck 1", 16, 18, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East")
    truck2 = Truck("Truck 2", 16, 18, [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East")
    truck3 = Truck("Truck 3", 16, 18, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East")

    load_packages(packageList, hashMap)
    hashMap.print()
    cur_package = hashMap.get("1").address
    print(cur_package)
    print(truck1.address)

if __name__ == "__main__":
    main()
