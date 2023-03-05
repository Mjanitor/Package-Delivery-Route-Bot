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
    package1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, 1030, 21)
    print(package1)

    # Demo Hashmap
    hashmap1 = HashMap()
    hashmap1.print()

if __name__ == "__main__":
    main()
