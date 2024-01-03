class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"{self.make}, {self.model}, {self.year}")

    def compute_milage(self):
        pass

    def compute_towing(self):
        pass


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def compute_milage(self):
        ans = max(0, 30 - max(self.year - 2010, 0))
        print(f"milage: {ans} kmpl")

    def compute_towing(self):
        print(f"towing power 0 kg")


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def compute_milage(self):
        ans = max(0, 100 - max(self.year - 2010, 0))
        print(f"milage: {ans} kmpl")

    def compute_towing(self):
        ans = max(100, 100 + self.year - 2000)
        print(f"towing power {ans} kg")


class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def compute_milage(self):
        ans = max(0, 150 - max(self.year - 2010, 0))
        print(f"milage: {ans} kmpl")

    def compute_towing(self):
        ans = max(1000, 1000 + (self.year - 2000) * 10)
        print(f"towing power {ans} kg")


if __name__ == "__main__":
    motorcycle = Motorcycle('Honda', 'CB500X', 2023)
    motorcycle.print_info()
    motorcycle.compute_milage()
    motorcycle.compute_towing()

    car = Car("Nissan", "Micra", 2013)
    car.print_info()
    car.compute_milage()
    car.compute_towing()

    truck = Truck("Ford", "F150", 2010)
    truck.print_info()
    truck.compute_milage()
    truck.compute_towing()