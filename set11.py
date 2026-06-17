# A set is a collection of unique elements where the order does not matter.
# set dont allow list jese chize
# l = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7]
# s = set (l)
# print(s)


# s = {1,2,3,4,5,6,} 

# s.add(60) #esme hum set me value ko add kr sakte hai 
# s.clear() #es commend se set clear ho jata hai
# s.discard(60) # es command se jo value ko hum hana cha rahe hai usko hata sakte hai 
# a=s.pop()
# print(s)




s1 = {10,20,30,40}
s2 = {30,40 }

# esse set se commen element ko nikalta hai
# print(s1.difference(s2))  

# shortcut 
# print(s1-s2)
 
# print(s1.difference_update()) #ess command se different to niklega lekin o different sath me save bhi ho jayega 
# #sortcut
# s2-=s1 
# print(s2)


# intersection  :- Intersection ka matlab hota hai do ya zyada sets ke common elements (jo elements sabhi sets me present ho).

# s1 &= s2
# print(s1)

# intersection_update() :- intersection_update() method set ko update kar deta hai aur sirf common elements ko hi rakhta hai.

# print(s1.intersection_update(s2))
  

#shortcut
# s1 & s2
# print(s1)

# issubset() in Python (Hinglish)
# issubset() method check karta hai ki ek set ke saare elements doosre set me present hain ya nahi.

# print(s2.issubset(s1))

# shortcut
# print(s1<=s2)


# or esme return true or false me output aata hai

# issuperset :- ye bhi same issubset ke jesa hi hia bas esme reverse ho jata hai 

# print(s1.issuperset(s2))
# shortcut

# print(s1>=s2)


# symmitric_difference :- symmetric_difference() method dono sets ke un elements ko return karta hai jo common nahi hote.

# print(s1.symmetric_difference(s2))

# shortcut
# print(s1^s2)


# union :- union() method do ya zyada sets ke sabhi unique elements ko ek naye set me combine karta hai.

print(s1.union(s2))

# shortcut
print(s1|s2)


