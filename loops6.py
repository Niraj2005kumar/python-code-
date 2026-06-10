

#   ////////////////////   FOR LOOP   ////////////////////////

#  the range() function 

#  range(stop)  # generates numbers from 0 to stop-1
#  range(start, stop)  # generates numbers from start to stop-1
#  range(start, stop, step)  # generates numbers from start to stop-1 with a step of step


# list(range(5))   #(0,1,2,3,4)
# list(range(1, 6))   #(1,2,3,4,5)
# list(range(1, 10, 2))   #(1,3,5,7,9)



#  #FOR LOOP WITH NUMBER ////////////////

#  range(10,20,1)
#  range(10,90,1)
# range(46)

# for i in range(1, 21, 1):
#     print(i)


#Question:- print a table of 5 using for loop and range function
# range(5, 50, 5)
#for i in range(5, 55, 5):
#     print(i)
    



# question////////////////////

# # # n = int(input("enter your number and print its table:-"))

# # # for i in range(n, (n * 10) + 1, n):
# # #     print(i)



# # #//////////////////// for loop with string///////////////



#   step 1:- user se ek number input karvaye

#  a = "student"

#  for i in a :
#      print((name)i)


#  step 2
#  for char in a :
#      print(char)


#  #step 3 

#  for i in range (len(a)) :
#      print(f"{a}:{a[i]}")




# #break condition and else 

# #break condition


#  for i in range(1, 11):
#      if i == 4:
#        break
#      print(i)


# #continue condition
# for i in range (1 , 11 ):
#     if i == 4 or i == 7 or i == 9:
#         continue 
#     print(i)


#else bas break ke sath chalta hai or agar else chal raha hia to break nhi chalega or agar break chal raha hai to else nahi chalega 


# for i in range(1, 11):
#     if i == 6:
#         break 
#     print(i)
# else :
#     print ("loop completed successfully")





#Question 

# # 1. print hello world n times 

# n = int(input("enter the number of times you want to print hello world:-"))
# for i in range(n):
#     print("hello world")



# 2. print naatural number from 1 to n

# n = int(input("tell your number "))
# for i in range(1, n+1):
#     print(i)




#3. print n to 1 in reverse order

# n = int(input("enter your number "))
# for i in range(n, 0, -1):
#     print(i)




# 4. print the multiple table of n

# n = int(input("enter your number "))
# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")


# 5. question 



# n = int(input("till where you want your sum :- "))
# s = 0

# for i in range(1, n+1):
#     s = s + i
#     print(s)



# question :- print factoril number




# n = int(input("till your number :-"))
# s = 1   #because jab koe aadmi n se 0 ko multiplay karega o uska return value zero hi aayega 

# for i in range (1, n+1):
#     s = s * i
#     print(s)


# Question :- print sum of all even and odd number in a seprate 



# n= int(input("please tell your number :-"))
# oddsum = 0
# evensum = 0

# for i in range(1, n+1):
#     if i % 2 ==0 :
#         evensum = evensum + i
#     else :
#         oddsum = oddsum + i

# print(f"your even sum is {evensum} and odd sum is {oddsum}")




#Question : find a factor///////////////////////


# n = int(input("tell your number :-"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)



# Question :- check if a number is perfect (sum of factors + the number itself)\\\\\\\\\\


n = int(input("tell your number "))
for i in range(1, n):    # + 1 es liye nhi likhe kyu ki mujhe khud ka number nahi chahiye agra n +1 rhata to jan user input 12 deta to compiler 12 ko bhi print kr deta hai 
    if n % i == 0 :
        print (i)


        # factor half number tk hi chalta hai 
        # user input 12 diya hai to 6 tk hi rint karega and user agar 50 deta hai to 25 tk hi print karega 




# Question :- check if a number is perfect (sum of factors + the number itself)\\\\\\\\\\


n= int(input("tell your number :- "))
s=0
for i in range(1, n):
    if n % i == 0:
        s = s+i

if s == n:
    print("prefect number ")

else :
    print ("it is a not perfect number ")




# Question :- check it is a prime number 

n = int(input("enter your number"))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count = count + 1

if count == 2:
        print("prime number ")
else :
        print("composite number")





# reverse order for staring ////////////////////////////

a = "python"
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

print(rev)




a = "python"
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

if rev == a:
    print("yes palindrome")
else:
     print("no not a palindrom")





# Question :- count letter digit and special symbol in a string


a = "p@#yn26at>&i5ve"

char = 0
spchar = 0
digits = 0

for i in a:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        char = char + 1
    else:
        spchar=spchar+1

print(f"characters{char}, special characters - {spchar}, digits -{digits}")

#this is inbuilds function




a = "p@#yn26at>&i5ve"

char = 0
spchar = 0
digits = 0

for i in a:
    if (ord(i)>=65 and ord(i)<= 90) or (ord(i)>=97 and ord(i)<= 122):
        char += 1
    elif ord(i)>= 48 and ord(i)<=90:
        digits +=1
    else:
        spchar= spchar + 1

print(f"characters{char}, special characters - {spchar}, digits -{digits}")


