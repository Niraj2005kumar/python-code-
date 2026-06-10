



# seprate each digit of a number and print an a new number 

#step :- 1
a = 456

print(a%10)
a = a//10
print(a%10)
a = a//10
print(a%10)
a = a//10



#step :- 2

a = int(input("enter your number :- "))

while a > 0:
    print(a%10)
    a = a//10






# accept a number revers order 


a = int(input("enter your number "))

rev = 0

while a>0:
    rev = rev * 10 + a% 10
    a = a//10


print(rev)




# check if it i a palindrom 


a = int(input("enter a number :-"))
copy = a
rev = 0

while a>0:
    rev = rev *10 + a%10
    a = a//10

if rev == copy:
    print("it is a palindrom number ")

else:
    print("it is not a palindrom number ")
