# Challenge - Extend Car into an ElectricCar subclass with battery capacity

class Car():
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display(self):
        print(f"Here is the Car details: \nBrand - {self.brand} \nModel - {self.model} \nColor - {self.color}")

# Subclass ElectricCar – inherits from Car and adds battery attribute
class ElectricCar(Car):
    def __init__(self, brand, model, color, battery_capacity):
        super().__init__(brand, model, color)  # Call the parent class constructor
        self.battery_capacity = battery_capacity  # New attribute for electric cars

    # Method overriding (Polymorphism) – redefine how display_info works for ElectricCar
    def display(self):
        super().display()  # Call the parent class display method
        print(f"Electric Car Details:\nBrand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nBattery Capacity: {self.battery_capacity} kWh")

# Create an instance of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S", "Red", 100)

# Call the display method to show electric car details
my_electric_car.display()



