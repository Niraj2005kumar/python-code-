OOPs (Object-Oriented Programming) in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes. It helps make programs modular, reusable, and easier to maintain.


Question :- what is a class ?

a class is a blueprint for creating object 

ex:-  class Student:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def display(self):
                print(f"Name: {self.name}, Age: {self.age}")


Question :- what is encapsulation?

Data aur methods ko ek hi class ke andar rakhna aur data ko direct access se protect karna Encapsulation kehlata hai.


---->> matlab ki data ko safe rakhna or data ko koe bhi access na kr sakte apni class ke under 


ex:- 
class Bank:
    def __init__(self):
        self.__balance = 1000

    def show(self):
        print(self.__balance)

b = Bank()
b.show()

--> ATM me app balance dekh sakte ho lekin directly change nhi kr sakte ho 


Question:-  what  is Inheritance?
Encapsulation means restricting direct access to data and providing controlled access through methods.

--> Jab ek class dusri class ke properties aur methods ko use karti hai, use Inheritance kehte hain.

Question :- what is abstraction ?

Unnecessary details ko hide karke sirf important information dikhana Abstraction kehlata hai.

Real-Life Example: Car chalane ke liye aapko engine ke andar kya ho raha hai, yeh jaanne ki zarurat nahi hoti.
