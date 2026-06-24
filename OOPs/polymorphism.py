

# Definition:
# Polymorphism ka matlab hai "Many Forms" (Anek Roop).
# Jab same method/function different objects ke liye different behavior dikhata hai, use Polymorphism kehte hain.

def hello():
    print("how are you")



def hello():
    print("what are you doing")

print()


# first method ////////////////

class animal:
    def speak(self):
        print("Animal will not speak ")

class humans:
    def speak(self):
        print("we are human we can speak ")

obj = animal()
obj2 = humans()


obj.speak()
obj2.speak()




# type of polymorphism///////////////////////


# method overriding (we need inheri)

class Animal:
    a = 12
    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"your name is {self.name}")

class Humans(Animal):
    b = 12
    def info(self):
        print(f"your info is {self.name} and this is all we have")

obj = Humans("Harsh")

obj.info()


# when we are doing inheritance and parent and child classes have same method name so the child class method your override your parent class method 




# Method overloding//////////////
class hello :
    def speak(self,a):
        print(f"how are you ")

    def speak(self ,a,b):
        print("how are you  ")







    



    




