size = input("Enter your pizza size (S, M, L): ")
bill = 0
if size =="s"or size =="S":
    bill = 150
    print("small pizza price is 150 rs")
elif size =="m"or size =="M":
    bill = 200
    print("medium pizza price is 200 rs")
else:
    bill = 250
    print("large pizza price is 250 rs")

add_pepperoni = input("Do you want to add pepperoni? Y or N: ")
if add_pepperoni == "y" or add_pepperoni == "Y":
    if size == "s"or size == "S":
        bill += 50
    else:
        bill += 100

extra_cheese = input("do you want to extra cheese? (Y/N): ")
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 20

print(f"Your final bill is {bill} rs")