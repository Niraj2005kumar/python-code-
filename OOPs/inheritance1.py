# it works between class 

# benefits of using inheritance is 
# 1. code reusable 
# 2. organize structure 
# 3. easy to maintain and extand

# ex:- 

class Animal: # parent class
    a = 12
    def __init__(self, name ):
        self.name = name 

    def details(self):
        print(f"hello your name is {self.name}")

class Humans(Animal):# child class
    pass

obj = Animal("loin")
obj2 = Humans("Harsh")


obj2.details()
print(obj2.a)

#your child class object has all the powers to access the attributes and methods and parent class


# constructor in inheritance

#miltilevel inheritance 
class BagFactory:
    def __int__(self, material, zips , pockets):
        self.material = material
        self.zips = zips 
        self.pockets = pockets
    
    def details(self):
        print("Your Bag Details:")
        print("Material:", self.material)
        print("Zips:", self.zips)
        print("Pockets:", self.pockets)

class Reebok(BagFactory):  # reebock bagfactory jo in harit kr raha hai 
    def __int__(self, material, zips, pockets,color):
        super().__int__(material, zips, pockets)
        self.color = color
    
    def details(self):
        print("color:",self.color)
        return super().details()

class Campus(Reebok)   :
    def __init__(self, material ,zips , color ,):
        super().__init__(material ,zips , color)
        
bag1 = BagFactory("Leather", 3, 4)
bag1.details()

print()

bag2 = Reebok("polyster",4,2)
bag2.details 


        
