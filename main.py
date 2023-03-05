from truck import *
from package import *
from hashmap import *

def main():
    print("Hello World!")
    print("Doggies are fun")
    print("Cats are too")
    print("Betelgeuse")

    for x in range(5):
        print(x)

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

if __name__ == "__main__":
    main()
