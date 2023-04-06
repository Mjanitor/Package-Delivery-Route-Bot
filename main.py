# Written by Mike Janitor, Student ID: 010769292

import Truck
from Package import *
import HashMap
import csv
from datetime import *

# Loads a csv file as a parameter and opens that file in a list format
def openCsvAsList(filepath):
    with open(filepath, encoding="utf-8-sig") as file:
        csv_list = []
        reader = csv.reader(file)
        for row in reader:
            csv_list.append(row)
        return csv_list

# Generates all packages for a given truck and inserts them into the given hashmap
def createPackages(hashMap, package_item_list, truck1, truck2):
    for package in package_item_list:

        id = package[0]
        address = package[1]
        city = package[2]
        zip = package[4]
        time = package[5]
        weight = package[6]

        # Manually adding package departure times depending on which truck it's loaded into
        if int(id) in truck1.packages:
            departure_time = timedelta(hours=8, minutes=0, seconds=0)
        elif int(id) in truck2.packages:
            departure_time = timedelta(hours=10, minutes=20, seconds=0)
        else:
            departure_time = timedelta(hours=9, minutes=5, seconds=0)

        arrival_time = timedelta(hours=0, minutes=0, seconds=0)

        # Constructor
        new_package = Package(id, address, city, zip, time, weight, departure_time, arrival_time)

        # Insertion
        hashMap.insert(id, new_package)

# Finds the distance (in miles) between two given addresses
def find_distance(address1, address2, address_list, distance_list):
    address1_index = 0
    address2_index = 0

    # Parsing address list and capturing the associated index if found
    for item in address_list:
        if item[2] == address1:
            address1_index = int(item[0])
        if item[2] == address2:
            address2_index = int(item[0])

    # Taking the indexes and matching them up in the distance list
    if distance_list[address1_index][address2_index] != '':
        distance = distance_list[address1_index][address2_index]
    elif distance_list[address2_index][address1_index] != '':
        distance = distance_list[address2_index][address1_index]
    else:
        distance = None

    return distance

def nearest_neighbor(truck, hash_table, address_list, distance_list, package_list):
    # Counter
    mileage = 0

    # Main nearest-neighbor loop
    while len(truck.packages) > 0:
        closest_distance = 1000.0
        for package in truck.packages:
            current_package = package  # temporary holder
            package = package_list[current_package - 1][0]
            package_object = hash_table.lookup(str(package))
            package_address = package_object.delivery_address
            temp_distance = float(find_distance(truck.location, package_address, address_list, distance_list))

            # Cuts off early if 0 mile distance is found
            if temp_distance == 0:
                final_package = current_package
                final_package_object = package_object
                final_address = package_address
                closest_distance = temp_distance
                break
            # If closer than the previous item, updates variables with current package attributes
            elif temp_distance < closest_distance:
                final_package = current_package
                final_package_object = package_object
                final_address = package_address
                closest_distance = temp_distance

        # Updating time based on 18mph speed
        travel_time = closest_distance / 18
        truck.time += timedelta(hours=travel_time)
        final_package_object.arrival_time = truck.time

        # Updating mileage with the captured distance
        mileage += closest_distance
        truck.location = final_address  # Updating the truck's location to the delivery address
        truck.packages.remove(final_package)  # Removing the package from the list to deliver

    return mileage

# Main Loop
# Generates all necessary truck objects, creates the Hash Table, loads them with packages,
# generates the total mileage
def main():
    total_mileage = 0
    # Manually loading the trucks
    # 8:00am
    truck1 = Truck.Truck("Truck 1", 0, [2, 4, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34], "4001 South 700 East",
                         timedelta(hours=8, minutes=0, seconds=0))
    # Wrong Address, 10:20am
    truck2 = Truck.Truck("Truck 2", 0, [3, 8, 9, 10, 11, 12, 17, 18, 21, 22, 23, 36, 38], "4001 South 700 East",
                         timedelta(hours=10, minutes=20, seconds=0))
    # 9:05am
    truck3 = Truck.Truck("Truck 3", 0, [1, 6, 24, 25, 26, 27, 28, 32, 33, 35, 37, 39, 40], "4001 South 700 East",
                         timedelta(hours=9, minutes=5, seconds=0))

    # Loading CSV data
    address_list = openCsvAsList("Resources\Address Indices.csv")
    package_list = openCsvAsList("Resources\WGUPS Package File.csv")
    distance_list = openCsvAsList("Resources\WGUPS Distance Table.csv")

    # Creating Hash Table
    hash_table = HashMap.HashMap()

    # Generating packages for each Truck
    createPackages(hash_table, package_list, truck1, truck2)

    # Algorithm x 3 = mileage
    # Adding Truck 1 mileage
    total_mileage += nearest_neighbor(truck1, hash_table, address_list, distance_list, package_list)
    # Driving Truck 1 home so driver can drive Truck 3
    total_mileage += float(find_distance(truck1.location, "4001 South 700 East", address_list, distance_list))
    # Adding Truck 2 mileage
    total_mileage += nearest_neighbor(truck2, hash_table, address_list, distance_list, package_list)
    # Adding Truck 3 mileage
    total_mileage += nearest_neighbor(truck3, hash_table, address_list, distance_list, package_list)

    # Interface loop
    while True:
        # Making it pretty
        print("Welcome to WGUPS package locator!")
        input_time = input("Please enter a time to check package status (format - 0930) - (Type 'X' to exit): ")

        # Quit condition
        if input_time.lower() == "X".lower():
            break

        # Looping for correct formatting
        while len(input_time) != 4 or not input_time.isnumeric():
            print("Wrong format, please try again.")
            input_time = input("Please enter a time to check package status (format - 0930): ")

        # Slicing the input time for timedelta format
        delivery_hour = int(input_time[:2])
        delivery_min = int(input_time[2:])
        input_time = timedelta(hours=delivery_hour, minutes=delivery_min)

        # Solo or all?
        amount = input("Would you like to check the status of all packages or just one? "
                       "Type 'solo' or 'all': ")

        # Printing all packages
        if amount.lower() == "all".lower():
            print(f"Lookup Time: {input_time}")
            print("-------------------------------------------------------------------------------------"
                  "----------------------------")
            print(f"ID || Delivery Address || Delivery City ||  ZIP || "
                  f"Weight || Departure Time || Delivery Time || Deadline || Status")
            print("-------------------------------------------------------------------------------------"
                  "----------------------------")
            for package in range(1, 41):
                # Printing status
                package = hash_table.lookup(str(package))
                package_status = Package.getStatus(package, input_time)

                # Changing colors based on delivery status
                if package_status == "Delivered":
                    print(f"\033[0;32m {package.id} || {package.delivery_address} || {package.delivery_city} || {package.delivery_zip} || "
                          f"{package.weight} kilograms || {package.departure_time} || {package.arrival_time} || {package.delivery_deadline} || {package_status}")
                elif package_status == "En Route":
                    print(f"\033[1;33m {package.id} || {package.delivery_address} || {package.delivery_city} || {package.delivery_zip} || "
                          f"{package.weight} kilograms || {package.departure_time} || {package.arrival_time} || {package.delivery_deadline} || {package_status}")
                else:
                    print(f"\033[0;31m {package.id} || {package.delivery_address} || {package.delivery_city} || {package.delivery_zip} || "
                          f"{package.weight} kilograms || {package.departure_time} || {package.arrival_time} || {package.delivery_deadline} || {package_status}")

            # Total miles
            print("\033[0m-------------------------------------------------------------------------------------"
                  "----------------------------")
            print(f"Total miles driven: {total_mileage} miles")
            print("\n")

        # Printing solo package
        elif amount.lower() == "solo".lower():
            package_id = input("Please enter a package ID: ")

            print(f"Lookup Time: {input_time}")
            print("-------------------------------------------------------------------------------------"
                  "----------------------------")
            print(f"ID || Delivery Address || Delivery City ||  ZIP || "
                  f"Weight || Departure Time || Delivery Time || Deadline || Status")
            print("-------------------------------------------------------------------------------------"
                  "----------------------------")

            # Printing status
            package = hash_table.lookup(str(package_id))
            package_status = Package.getStatus(hash_table.lookup(package_id), input_time)

            # Changing colors based on delivery status
            if package_status == "Delivered":
                print(
                    f"\033[0;32m {package.id} || {package.delivery_address} || {package.delivery_city} || {package.delivery_zip} || "
                    f"{package.weight} kilograms || {package.departure_time} || {package.arrival_time} || {package.delivery_deadline} || {package_status}")
            elif package_status == "En Route":
                print(
                    f"\033[1;33m {package.id} || {package.delivery_address} || {package.delivery_city} || {package.delivery_zip} || "
                    f"{package.weight} kilograms || {package.departure_time} || {package.arrival_time} || {package.delivery_deadline} || {package_status}")
            else:
                print(
                    f"\033[0;31m {package.id} || {package.delivery_address} || {package.delivery_city} || {package.delivery_zip} || "
                    f"{package.weight} kilograms || {package.departure_time} || {package.arrival_time} || {package.delivery_deadline} || {package_status}")

            # Total miles
            print("\033[0m-------------------------------------------------------------------------------------"
                  "----------------------------")
            print(f"Total miles driven: {total_mileage} miles")
            print("\n")

        # Formatting not recognized
        else:
            print("Sorry, I didn't understand that, please try again.\n")

if __name__ == '__main__':
    main()
