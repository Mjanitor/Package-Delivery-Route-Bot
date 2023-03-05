from truck import *
from package import *
from hashmap import *
import csv

def main():
    # Demo Truck
    truck1 = Truck("Truck 1")

    # Demo Package
    package1 = Package(1, "195 W Oakland Ave", 1030, "Salt Lake City", 84115, 21, "at the Hub")

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

    #TODO: Load Package attributes from CSV files

    #TODO: Create Method to determine the distance between two addresses

if __name__ == "__main__":
    main()
