"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class VehicleClass:
    fuel_type = "unleaded"

    def __init__(self, make: str, model: str, color: str, features: list):
        self.make = make
        self.model = model
        self.color = color
        self.features = features

    def get_info(self):
        return f"Fuel Type: {self.fuel_type}\nMake: {self.make}\nModel: {self.model}\nColor: {self.color}\nFeatures: {', '.join(self.features)}\n"

    def change_color(self, color: str):
        self.color = color



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class CarClass(VehicleClass):
    wheel_count = 4

    def __init__(self, make: str, model: str, color: str, features: list, type: str, engine: str):
        super().__init__(make, model, color, features)

        self.type = type
        self.engine = engine

    def honk(self):
        print("Honk! Honk!")

    def get_info(self):
        inharited_info = super().get_info()

        return inharited_info + f"Wheel Count: {self.wheel_count}\nType: {self.type}\nEngine: {self.engine}\n"



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    #print("TODO: Implement namespace demonstration")

    # Creating 2 objects
    car1 = CarClass("Toyota", "Camry", "Red", ["Heated Seats, A/C"], "Sedan", "V6")
    car2 = CarClass("Jeep", "Wrangler", "Black", ["Heated Seats, A/C"], "SUV", "V6")

    # Access class variable through class
    print(f"Class variable via the class: Wheel Count = {CarClass.wheel_count}")

    # Access class variable through object
    print(f"Class variable via the object: Wheel Count = {car1.wheel_count}")

    # Add an attribute
    car2.has_4_wheel_drive = True

    # Display object namespace
    print(f"Car1:\n{car1.__dict__}")
    print(f"Car2:\n{car2.__dict__}")

    # Display class namespace
    print(f"Child Class:\n{CarClass.__dict__}")
    print(f"Parent Class:\n{VehicleClass.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    #print("TODO: Implement shallow copy and deep copy demonstration")

    # Creates an original object.
    car1 = CarClass("Toyota", "Camry", "Red", ["Heated Seats, A/C"], "Sedan", "V6")

    # Creates a shallow copy.
    shallow_car = copy(car1)

    # Creates a deep copy.
    deep_car = deepcopy(car1)

    # Modifies the list in the original object to observe the differences in shallow and deep copies.
    car1.features.append("GPS")

    print(f"~~~~Original:\n{car1.get_info()}\n")

    # A copy of the original, but the features list is just a copy of the reference to the list.
    # Any change to the list is reflected in both since the list is not a new copy.
    print(f"~~~~Shallow copy:\n{shallow_car.get_info()}\n")

    # A complete new copy of everything from the original. Any changes to the list will not reflect on both.
    # The list in the deep copy is a separate list in memory.
    print(f"~~~~Deep Copy:\n{deep_car.get_info()}\n")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    #print("\nTODO: Create and test your parent object")

    #print("\nTODO: Create and test your child object")

    parent1 = VehicleClass("Jeep", "Wrangler", "Orange",["Heated Seats, A/C"])

    child1 = CarClass("Toyota", "Camry", "Red", ["Heated Seats, A/C"],"Sedan", "V6")

    print(parent1.get_info())

    print(child1.get_info())

    demonstrate_namespaces()

    demonstrate_copying()


if __name__ == "__main__":
    main()