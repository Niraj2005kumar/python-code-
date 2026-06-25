# Definition:
# Abstraction ka matlab hai complex cheezon ki unnecessary details ko hide karna aur sirf important features ko user ko dikhana.

# User ko sirf zaruri functionalities dikhani hain.
# Andar ka implementation hidden rahta hai.

# Ek parent class me common methods define kar dete hain aur har child class un methods ko apne tareeke se implement karti hai.


# Exam Definition (2 Marks)

# Abstraction is the process of hiding implementation details and showing only the essential features to the user. In Python, abstraction is achieved using the abc module using abstract classes and abstract methods.


# EX:

from abc import ABC , abstractmethod

class enforce(ABC):
    @abstractmethod  # create a abstract class
    def enginestart():
        pass



class bike(enforce):
    def enginestart():
        pass

class car (enforce): 
    def enginestart():
        pass

class truck:
    pass 


obj1 = bike()
obj2 = car()
obj3 = truck()

# output nhi aayega 


