
# So many type of dunder mathod in this program 
# dunder method ka use kr ke bhut sare chis ban sakte hai 

class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"hello my name is {self.name}"

obj = Animal("Lion")
obj2 = Animal("Giraffe")
print(obj) 



# Add the number in dunder method(Arthimatic method)

class number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

num1 = number(20)
num2 = number(30)

print(num1+num2)



# string method in dunder method 

class number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __eq__(self, value):
        return self.num == value.num
    
num1 = number(20)
num2 = number(30)

print(num1+num2)
print(num1 == num2)






