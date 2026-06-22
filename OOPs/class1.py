
# create a class

# class car:
    # a = 12 # atteribute ,,,, matlab ki class ke under attribute hota hai

    # def hello(): #function define inside a class ///// maqtlab ki class ke under method hota hai (method )
        # print("how are you")

# first you can access attributes and then 
#method after accessing the class
# print(car.a) #accessing attributes 

# car.hello() #accessing method


# object create 

# class bags:
#     name = "niraj"


#     def details():
#         print("hello this is a company who create bags")
# reebok = bags() #this is a object 
# campus = bags()

# print(reebok.name)
# print(campus.name)


# Constructure : - Constructor ek special method hai jo object create hote hi automatically call ho jata hai.

# class Bags:
#     def __init__(self, material, zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets 

# reebok = Bags("leather",3,2)
# campus = Bags("polyster",2,4)



# print(reebok.material)
# print(campus.material)
        


# constructure attribute and method

class Animal:
    a = 12
    
    def __init__(self,name):
        self.name = name #object/instance attribute

    def hello(self): #instance/ object method   .... capture the location of object 
        print(f"how are you  my name is {self.name} ")

    @classmethod
    def details(cls): #class method ... captures location class 
        print(f"how are you my name is {cls.a}")

obj = Animal("lion")

obj.details()



         















