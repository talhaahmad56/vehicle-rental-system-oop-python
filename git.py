class Vehicle:
    def __init__(self,vehicle_id,brand,base_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.base_rate = base_rate

    def calculate_rent(self,days):
        return self.base_rate * days

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id} | Brand: {self.brand}"


class Car (Vehicle):
    def __init__(self, vehicle_id, brand,  base_rate,air_conditioned,):
        super().__init__(vehicle_id, brand, base_rate)
        self.air_conditioned = air_conditioned
    def calculate_rent(self,days):
        rent = super().calculate_rent(days)
        if self.air_conditioned:
            rent += rent * 0.20
        return rent   

class Bike (Vehicle):
    def __init__(self, vehicle_id, brand,  base_rate,engine_cc):
        super().__init__(vehicle_id, brand,  base_rate)
        self.engine_cc = engine_cc

    def calculate_rent(self,days):
        rent = super().calculate_rent(days)
        if self.engine_cc > 200:
            rent += 500 * days
        return rent
    
vehicles = []

while True:
    print("\n1. Add Car")
    print("2. Add Bike")
    print("3. Show All Rents")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vid = int(input("Enter vehicle ID: "))
        brand = input("Enter brand: ")
        rate = float(input("Enter base rate per day: "))
        ac = input("Air conditioned? (yes/no): ").lower() == "yes"

        car = Car(vid, brand, rate, ac)
        vehicles.append(car)
        print("Car added successfully!")

    elif choice == "2":
        vid = int(input("Enter vehicle ID: "))
        brand = input("Enter brand: ")
        rate = float(input("Enter base rate per day: "))
        cc = int(input("Enter engine CC: "))

        bike = Bike(vid, brand, rate, cc)
        vehicles.append(bike)
        print("Bike added successfully!")

    elif choice == "3":
        days = int(input("Enter number of rental days: "))
        if not vehicles:
            print("No vehicles added yet.")
        else:
            for v in vehicles:
                print(v)
                print("Total Rent:", v.calculate_rent(days))
                print("-" * 30)

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")
