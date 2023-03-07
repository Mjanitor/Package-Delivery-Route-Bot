from truck import *
from package import *
from hashmap import *
import csv

def main():
    # Demo Truck
    truck1 = Truck("Truck 1", 16, 18, [1, 2, 3, 4, 5], 0.0, "4001 South 700 East")

    # Demo Hashmap
    hashmap1 = HashMap()

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

    load_packages(packageList, hashmap1)
    hashmap1.print()
    cur_package = hashmap1.get("1").address
    print(cur_package)
    print(truck1.address)



    # Create Method to determine the distance between two addresses
    def find_distance(x, y):
        distance = distanceList[x][y]

        if distance == '':
            distance = distanceList[y][x]

        return distance

    print(find_distance(0, 14))

if __name__ == "__main__":
    main()
