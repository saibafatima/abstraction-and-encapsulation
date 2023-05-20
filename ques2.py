# Q2. Differentiate between Abstraction and Encapsulation. Explain with an example.


definition = "Abstraction focuses on presenting essential features and functionalities while hiding unnecessary details."

definition2 = "Encapsulation is the practice of bundling data and related methods/functions into a single unit, typically called a class."


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

# Creating an instance of BankAccount
my_account = BankAccount("1234567890", 1000)

# Using the public methods to interact with the account
print("Account number:", my_account.get_account_number())
print("Balance:", my_account.get_balance())

my_account.deposit(500)
print("Balance after deposit:", my_account.get_balance())

my_account.withdraw(200)
print("Balance after withdrawal:", my_account.get_balance())

##here is the 2nd exapmle

from abc import ABC, abstractmethod

# Abstract class representing a Shape
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

# Concrete class representing a Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class representing a Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Main program
circle = Circle(5)
print("Area of the circle:", circle.calculate_area())
print("Perimeter of the circle:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Area of the rectangle:", rectangle.calculate_area())
print("Perimeter of the rectangle:", rectangle.calculate_perimeter())
