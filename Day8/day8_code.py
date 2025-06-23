# Challenge:  Create a Car class with attributes and a display method

# Step 1: Define the class
class Car:
    # Step 2: Initialize the attributes using the constructor (__init__ method)
    def __init__(self, brand, model, color):
        self.brand = brand   
        self.model = model   
        self.color = color    

    # Step 3: Define a method to display car information
    def display(self):
        # Print the car details in a formatted way
        print(f"Here is the Car details: \nBrand - {self.brand} \nModel - {self.model} \nColor - {self.color}")

# Step 4: Create an object (instance) of the Car class
my_car = Car("Mercedes-Benz", "C-Class", "Obsidian Black")

# Step 5: Call the display method to show car details
my_car.display()

