

# Data Structure ek tarika hai data ko organize, store aur manage karne ka taaki data ko efficiently access aur modify kiya ja sake.

# Exam Answer (2 Marks)

# Data Structure is a method of organizing and storing data efficiently so that it can be accessed and modified easily. Examples are List, Tuple, Set, and Dictionary.


# Viva Question
# Q. Why do we use data structures?
# Ans: We use data structures to store, organize, process, and retrieve data efficiently. ✅


# there are four type of data structure 
# 1. list 
# 2. tuples
# 3. set 
# 4. dictionary


# list //////////////////////////

# a = [12,32,665,78,98,78]
# print(type(a))

# ordered nature you can access any element 
# a = [12,32,665,78,98,78]
# print(a[1])


# mutable nature :- you can change any value on your list 

l = [10,20,30,40]
l[1] = 20
print(l)


# Duplicates :- you can have duplicates value 

t = [1,1,1,2,2,2,3,3,3,3]


# traversing on list 

a = [10,20,30,40 , 20]

# traversing on values 

for i in a:
    print(i)


# traversing on index :- esme hum directily hum value ko acces kr sakte hai 

for i in range(0,len(a)):
    print(a[i])


a = [10,20,30,40]

a.append("60") # adds a value to the last sport
a.insert(2,30) # add value in the middle 
a.pop()
a.remove(30) #directly ek value ko provide kr sakte hai means I want remove the 30 then output is [10,20,40]
a.clear() #all elements are remove in the index 
a.sort()#sort the list in ascending order and return None matlab esme element ko decrease se increase krta hai 
a.sort(reverse=True)# esme increase se decrease ho jata hai 



print(a)

# Homogeneous Data Type ka matlab hota hai ki kisi data structure ke andar saare elements ek hi type ke ho.
# numbers = [10, 20, 30, 40]

# Heterogeneous Data Type:
# Agar alag-alag type ke elements ho to use heterogeneous data type kehte hain.
# data = [10, "Niraj", 3.14, True]


# LIST QUESTION/////////////////////////////


# Question :- print all position and neagative element separatly.

l = [3,5, -45,]

pos = []
neg = []

for i in l:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print(f"yore positive element is :-{pos}")
print(f"negative elements is :- {neg}")


# Question :- find the mean {average } of all element . 

l = [10,20,30,40]

sum = 0
for i in l:
    sum = sum +i

print(f"your average is {sum/ len(l)}")





# Question :- find the greatest element and print its index 

a = [ 20,40,82,40,56,50,7,45,99]

largest = a[0]
lowest = a[0]


for i in a:
    if i > largest:
        largest = i

    else:
        if i< lowest :
            lowest = i

print(f"your lowest value is {lowest}")
print(f"your largest value is {largest}")


# ye toh ese hi bana deiye the or humlogo ko index prnt krne ko bola gaya hai to ese liye niche wala code sahi hia index ko print krne ke liye 
# or uper wala code hai bas lowest or largest ko print krne ke liye diya gaya hai 


largest = a[0]
index = 0

for i in range(len(a)):
    if a[i] > largest :
        largest = a[0]
        index = i 

print(f"your largest value is {largest} at index is {index}")



# Qusetion :- find the second largest element 

a = [4,2,4,54,7,8,]
largest = a[0]
sec_largest = a[0]

for i in a:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i
    
print(sec_largest)



# check if the list is already sorted

a = [20,40,50,30,]

for i in range (len(a)-1):
    if a[i] > a[i+1]:
        print ("ypur list is not shorted ")
        break

else :
    print("your list is shorted")





