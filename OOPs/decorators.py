# Definition:
# Decorator ek function hota hai jo kisi dusre function ke behavior ko modify ya extend karta hai, bina us function ka code change kiye.

def extragreeting(fun):
    def wrapper():
        print("hello from ")
        fun
        print("thank you")

    return wrapper


@extragreeting
def greetings():
    print("good morning")

greetings()


# args //////////////////////

def addition(*args): # args me stars use krne pr hum multiple value ko use kr sakte hai  
    s = 0
    for i in args:
        s = s+i

    return s 

print(addition (20,30,40,50,))


# kwargs ye ek dictonary create krta hai or mera data ko return krta hia 

def info(**kwargs):
    return kwargs

print(info(name = "Niraj", age = 24 ,profession = "data scientist"))




#use or args 

def extragreeting(fun):
    def wrapper(*args, **kwargs):
        print("hello from ")
        fun(*args, **kwargs)
        print("thank you")

    return wrapper

@extragreeting
def addition(a,b,c):
    print(a+b+c)

addition(10,20,30,)



# Comprehension - One-liners : - 
# Definition:
# Comprehension ek short aur easy way hai lists, dictionaries, aur sets ko ek hi line me create karne ka.

# EX
a = 20  # i chck number is even ya odd

if a%2 ==0:
    print("even number ")

else:
    print("odd number ")




a = [10,20,30,40,50,60,70,80,90,54]

b = [ i for i in a if i%2 == 0]

# for i in range in a :
#     if i % 2 == 0:         hum ye sab skip kr sakte hai 
#         b.append()

print(b)


# Dict Comprehension 
squared = {x : x**2 for x in range(5)}


# set Comprehension

unique = {x%3 for x in range(10)}




# Lamda function///////////////////


def check (a):
    if a%2 == 0:
        print("even number ")

    else:
        print("odd number ")

check(12)


# in short line answer 

check = lambda x: "even number " if x % 2 ==0 else "old number"
print (check (12))

# add in two number add in one line 

def addition(a,b):
    print(a + b)

additio = lambda a,b: a+b
print(addition(10, 20 ))



#map (),filter(), zip()////////////////////////////////////////////////////////////////////////////////

# Map()
# Ex:-

a = [ "Niraj"," krish ", "Abhsishek ","rajan "]

lengths = list(map(len,a))
print(lengths)


# create a temprature 

temp_cel = [0,20,30,40]

def converter(a):
    far = (a*9/5) + 32
    return far

for i in temp_cel:
    print(converter(i))


temp_far = list(map(converter,temp_cel))
print(temp_far)


# Filter////////////////////

m = [35,80,80,12,60,49]

passed = list(filter(lambda x : x >= 40,m))

print(passed)


# zip /////////////// combine a multiple list

name = ['sarthak', 'niraj ','harsh',]

marks = [12 ,90,45,323]
result = list(zip(name, marks ))

print(result)















