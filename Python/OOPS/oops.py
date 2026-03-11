class Vehicles:
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price= price

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.__price)

v1 = Vehicles("Suzuki","Baleno",2020,500000)
print("Vehicle Info:")
v1.display_info()

# task-2

def get_price(self):
    return self.__price

def set_price(self, price):
    return self.__price

v1.set_price(550000)
print("Updated Price:", v1.get_price())

# task-3

class Car(Vehicles):
    def __init__(self, brand, model, year, price, num_doors):
        super().__init__(brand, model, year, price)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print("Number of Doors:", self.num_doors)

# task-4

class Bike(Vehicles):
    def display_info(self):
        print("Bike Brand:", self.brand)
        print("Bike Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.get_price())

b1 = Bike("Yamaha","R15",2021,150000)
B2 = Bike("HERO","SPLENDOR",2022,80000)

Vehicles = [b1, B2]

for vehicle in Vehicles:
    vehicle.display_info()
    print()

# task-5

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    print("Area of Rectangle:", Rectangle(5, 3).area())
    
# task-6

class Vehicle:

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price

    def calculate_discount(self, percentage, additional_discount=0):
        discount = self.__price * (percentage / 100)
        final_price = self.__price - discount - additional_discount
        return final_price


v3 = Vehicle("Tesla", "Model 3", 2024, 4000000)

print("Discounted Price (10%):", v3.calculate_discount(10))
print("Discounted Price (10% + 1000):", v3.calculate_discount(10, 1000))

# Task 7

class Vehicle:

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def save_to_file(self):
        filename = f"{self.brand}_{self.model}.txt"

        with open(filename, "w") as file:
            file.write(f"Brand: {self.brand}\n")
            file.write(f"Model: {self.model}\n")
            file.write(f"Year: {self.year}\n")
            file.write(f"Price: {self.price}\n")

        print("Vehicle data saved to", filename)


v4 = Vehicle("Hyundai", "Verna", 2023, 1500000)
v4.save_to_file()

# Task 8

class Library:

    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print("-", book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("You borrowed:", book)
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned:", book)

    

    
