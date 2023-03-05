from truck import *
from package import *
from hashmap import *
import csv

def main():
    # Demo Truck
    truck1 = Truck("Truck 1", 2)
    print(truck1)

    # Demo Package
    package1 = Package(1, "195 W Oakland Ave", 1030, "Salt Lake City", 84115, 21, "at the Hub")
    print(package1)
    package1.check_location()

    # Demo Hashmap
    hashmap1 = HashMap()
    hashmap1.print()

    #TODO: Open CSV Files

    #TODO: Load Package attributes from CSV files

    #TODO: Create Method to determine the distance between two addresses

if __name__ == "__main__":
    main()
