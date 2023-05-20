# Q5. Can we create an instance of an abstract class? Explain your answer.

a = "No, we cannot create an instance of an abstract class. An abstract class is designed to serve as a blueprint or a template for other classes to inherit from. It contains one or more abstract methods, which are declared but do not have any implementation."

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    abstractmethod
    def abstract_method(self):
        pass

# Attempting to create an instance of the abstract class
print(obj = AbstractClass())
# Output: TypeError: Can't instantiate abstract class AbstractClass with abstract methods abstract_method


