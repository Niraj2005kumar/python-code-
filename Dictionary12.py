# Dictionary ek mutable (changeable) data type hai jo data ko key-value pairs me store karta hai.

# d = {10:100,20:200,30:300,40:400}

#vanilla python :- eska matlab ye hota hia ki value or key ko direct access kr raha hu 

# d[50] = 500 #create a new key value pair
# print(d[30]) #300 - reading a value 
# d[10] = 100 #update a key value that already exist
# print(d)
#

# methods approach :- 
d = {10:100,20:200,30:300,40:400}

# d.clear()
# print(d)

q = d.fromkeys([10,20,30,40],50)
print(q)




