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
# Definition:
# Jab ek class dusri class ko inherit kare aur phir teesri class us child class ko inherit kare, to use Multilevel Inheritance kehte hain.
class BagFactory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("Your Bag Details:")
        print("Material:", self.material)
        print("Zips:", self.zips)
        print("Pockets:", self.pockets)


class Reebok(BagFactory):
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets)
        self.color = color

    def details(self):
        print("Color:", self.color)
        super().details()


class Campus(Reebok):
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets, color)


bag1 = BagFactory("Leather", 3, 4)
bag1.details()

print()

bag2 = Reebok("Polyester", 4, 2, "Black")
bag2.details()
        

# Multiple inheritance
# Definition:
# Jab ek child class ek se jyada parent classes ko inherit karti hai, use Multiple Inheritance kehte hain.

# Matlab ek class, multiple classes ke methods aur properties ko use kar sakti hai.

class Animal :
    def __init__(self,name):
        self.name = name 

class Humans :
    def __init__(self,id):
        self.id = id

class Robots(Humans, Animal):
    def __init__(self, id ,name):
        Humans.__init__(id)
        Animal.__init__(name)  #hum esko tab likhenge jab hum phle se hi inherit huya HOGA class robot me 
        
robo = Robots(12,"Niraj")






