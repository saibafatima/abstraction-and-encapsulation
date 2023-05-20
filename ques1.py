# Q1. What is Abstraction in OOps? Explain with an example.

definition = "Abstraction in object-oriented programming (OOP) is a concept that focuses on capturing the essential characteristics and behavior of an object while hiding unnecessary details. It allows us to create complex systems by breaking them down into manageable and modular components."


from abc import ABC, abstractmethod

# Abstract class representing a Vehicle
class Vehicle(ABC):

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

# Concrete class representing a Car
class Car(Vehicle):

    def accelerate(self):
        print("Car is accelerating.")

    def brake(self):
        print("Car is braking.")

# Main program
my_car = Car()
print(my_car.accelerate())
print(my_car.brake())

