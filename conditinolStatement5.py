# # #conditional statement
# # #Conditional Statement ka use kisi condition ko check karne ke liye kiya jata hai. Agar condition True ho to ek block execute hota hai, warna dusra.



 age = int(input("enter your age :-"))
 if age >= 18 :
    print("you can vote in election")

 else :
    print("you cannot vote in election ")





# # ruppes = int(input("enter your amount:-"))
# # if ruppes == 100 :
# #     print ("i can buy a phone")

# # elif ruppes == 500 :
# #     print("i can buy a watch")             #es condition me limit lag jata hai ki esse jayda ka saman nhi kharid sakta hai

# # elif ruppes == 600 :
# #     print("i can buy a pen")

# # else :
# #     print("i cannot buy anything")





# # # QUESTION :-  user se do number input karvaye aur unme se bada number print karvaye

# # greater = int(input("enter a number"))
# # lower = int(input("enter a number"))
# # if greater > lower:
# #     print(f"{greater} is greater than {lower}")

# # elif lower > greater:
# #     print(f"{lower} is greater than {greater}")
# # else : 

# #     print("both are equal")


# # # question :- user se ek number input karvaye aur check karega ki greater number hai ya nahi agar hai to good morning sir print karega warna good morning madam print karega

# # greater = int(input("enter first number "))
# # if greater == 20:
# #     print("good morning sir")

# # else : 
# #     print("good morning madam")



# # # Question :- user se unka gender input karvaye aur check karega ki user


# # gen = input("please tell your gemder in (M/F) :-")
# # if gen == "m" or gen == "M":
# #     print("M")
# # elif gen == "f" or gen == "F" : #agar use esme small f de diya ya small m deya or capital m de diya to bhi esme condition true ho jaye`ga to ye dono condition me se koi bhi condition true hone par M print karega 
# #     print("F")
# # else :
# #     print("invalid input")


# # question :- user se ek number input karvaye aur check karega ki number even hai ya odd hai

# a = int(input("enter a number:- "))
# if a%2 == 0 :
#     print("even number")
# else :
#     print("odd number")


# # Querstion:- 

# name = input("enter your name:- ")
# age = int(input("enter your age:-"))
# if age >=18 :
#     print(f"hello {name} you can vote in election")
# else:
#     print(f"hello {name} you cannot vote in election and you eligible for vote after {18-age} years")


#\|||||||||||||\\\\\\\\\\\\\\\\\\|||||||||

#leap year kaise check karte hai
# A leap year is a year with 366 days instead of 365. An extra day is added to February, making it 29 days long.

# A year is a leap year if:

# It is divisible by 4, and
# If it is divisible by 100, it must also be divisible by 400.

# Examples:

# 2024 → Leap year (divisible by 4)
# 2025 → Not a leap year
# 1900 → Not a leap year (divisible by 100 but not 400)
# 2000 → Leap year (divisible by 400)

# The rule can be summarized as:



#Question:- user se ek year input karvaye aur check karega ki year leap year hai ya nahi
year = int(input("enter a year:- "))
if year%4 == 0 and year%100 != 0 or year%400 == 0 : #esme pehle ye check karega ki year 4 se divisible hai ya nahi aur 100 se divisible nahi hai ya phir 400 se divisible hai ya nahi
    print(f"{year} is a leap year")
elif  year%100 != 0 and year%4 == 0 :
    print(f"{year} is a leap year")
else :
    print(f"{year} is not a leap year")





#Question :- user se unka temperature input karvaye aur check karega ki weather kaisa hai

temp = int(input("enter your temperature :- "))
if temp >= 0 and temp<=20 :
    print("weather is very cold")
elif temp >= 21 and temp <= 30 :
        print("weather is cold")
elif temp >= 31 and temp <= 40 :
        print("weather is hot") 
else :
        print("weather is very hot")    
