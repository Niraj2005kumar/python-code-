# function :- A Function is a reusable block code with a name insided of writing the same logic 10 times 


# Example :- 

a = int(input("Enter a number :- "))
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a%10
    a = a//10

if copy == rev:
    print("pallindrome number ")

else:
    print("not a pallindrome number ")


def hello() : # create a function 
    print("hello")

hello()





# def palindrome_checker(a):
    
    copy = a 
    rev = 0

    while a > 0:
        rev = rev * 10 + a% 10 
        a= a//10

    if copy == rev:
        print (f"{copy} is a palindrom number")
    else:
        print(f"{copy} is not a palindrom number ")

palindrome_checker(121)
palindrome_checker(231)
palindrome_checker(654)


# parameter are the value you accept while calling the function 
# Arguments are the value you provide to parameters while callong the function



# there are three type of aguments//////////////////////

# 1. Positional Arguments:
#   "Arguments that are passed to a function in the same order as the parameters are defined are called positional arguments."

# Positional arguments wo arguments hote hain jo function call karte waqt same order (position) me pass kiye jaate hain jisme function define hua hota hai.


def multiply(a,b,c,d):
    print(a*b*c*d)

# multiply(4,5,78,65)


# Default Argument
# Default Argument wo argument hota hai jiske liye function define karte waqt pehle se hi ek value di jaati hai. Agar function call karte samay us argument ki value na di jaye, to default value use hoti hai.


# Default Arguments:
# "Arguments that are assigned a default value during function definition are called default arguments. If no value is passed during function call, the default value is used."

def addition (a,b,c =12):
    print(a+b+c)

addition(4,5,2)



# Keyword Arguments in Python

# Keyword Arguments me function call karte waqt parameter ka naam (keyword) likhkar value pass ki jaati hai.
# Keyword Arguments:
# "Arguments passed to a function by specifying the parameter names are called keyword arguments."

def subtraction(a,b):
    print(b-a)

subtraction(20,30)




