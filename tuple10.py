# A tuple is an ordered collection of elements, usually used in mathematics and programming.

# Ordered: the position of each element matters.
# Fixed-size (in many languages): tuples often have a predetermined number of elements.
# Can contain different types (in many programming languages).



# it is immutable list
# it is use tuple for data that should stay constant

a = ["monday", "tuesday",201,214]

tup = tuple(a)

print(tup[-1])

# it has immutable natural - yo can not change any value inside ypur tuple 

# means :- tuple ke under kisi bhi string ya value ko change nhi kr sakte hai 


# tuple method //////////////////////////////////

print(tup.index("tuesday")) # you can directly print in the string 

print(tup.count(201)) # esse value ko count karega or output me batayega ki kitni baar aa raha hai ye value 


