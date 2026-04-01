import os

class Vehicle:
    def __init__(self, owner, number, service_date, cost):
        self.owner = owner
        self.number = number
        self.service_date = service_date
        self.cost = cost

    def __str__(self):
        return f"Owner: {self.owner}  Vehicle No: {self.number}  Date: {self.service_date}  Cost: {self.cost}"


class VehicleService:
    def __init__(self, filename="vehicle.txt"):
        self.filename = filename
        self.vehicles = []
        self.load_vehicle()

    def load_vehicle(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        owner, number, date, cost = data
                        self.vehicles.append(Vehicle(owner, number, date, cost))

    def save_vehicle_details(self):
        with open(self.filename, "w") as file:
            for v in self.vehicles:
                file.write(f"{v.owner},{v.number},{v.service_date},{v.cost}\n")

    def add_vehicle(self):
        owner = input("Enter owner name: ")
        number = input("Enter vehicle number: ")
        service = input("Enter service date: ")
        cost = input("Enter service cost: ")

        for v in self.vehicles:
            if v.number == number:
                print("Vehicle already exists\n")
                return

        self.vehicles.append(Vehicle(owner, number, service, cost))
        self.save_vehicle_details()
        print("Details saved successfully\n")

    def view_details(self):
        if not self.vehicles:
            print("No vehicle records found\n")
        else:
            for v in self.vehicles:
                print(v)
            print()

    def search_vehicle(self):
        vehicle_no = input("Enter vehicle number: ")
        found = False

        for v in self.vehicles:
            if vehicle_no in v.number:
                print(v)
                found = True

        if not found:
            print("Vehicle record not found\n")

    def update_detail(self):
        vehicle_no = input("Enter vehicle number: ")

        for c in self.vehicles:
            if c.number == vehicle_no:
                new_owner = input(f"New owner ({c.owner}): ") or c.owner
                new_number = input(f"New number ({c.number}): ") or c.number
                new_date = input(f"New date ({c.service_date}): ") or c.service_date
                new_cost = input(f"New cost ({c.cost}): ") or c.cost

                c.owner, c.number, c.service_date, c.cost = new_owner, new_number, new_date, new_cost
                self.save_vehicle_details()
                print("Updated successfully\n")
                return

        print("Record not found\n")

    def delete_record(self):
        vehicle_no = input("Enter vehicle number: ")

        for c in self.vehicles:
            if c.number == vehicle_no:
                self.vehicles.remove(c)
                self.save_vehicle_details()
                print("Deleted successfully\n")
                return

        print("Vehicle not found\n")


def main():
    veh = VehicleService()

    while True:
        print("=== Vehicle Service Record System ===")
        print("1. Add vehicle")
        print("2. View all details")
        print("3. Search vehicle")
        print("4. Update vehicle details")
        print("5. Delete vehicle")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            veh.add_vehicle()
        elif choice == "2":
            veh.view_details()
        elif choice == "3":
            veh.search_vehicle()
        elif choice == "4":
            veh.update_detail()
        elif choice == "5":
            veh.delete_record()
        elif choice == "6":
            print("Exit")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()