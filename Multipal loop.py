height = int(input("Enter your Height :- "))
bill = 0
if height>=3:
    print("you can ride the car")
    age = int(input("Enter your age : "))
    if age<12:
        bill = 150
        print("Ticket price is 150 rs")
    elif age<=18:
        bill = 250
        print("Ticket price is 250 rs:")
    else:
        bill = 500
        print("Ticket price is 500 rs")

    wants_photo = input("do you want to take photo ? Y or N :- ")
    if wants_photo == "y" or wants_photo == "n":
        bill += 50
        print("Photo price is 50 rs")
        print(f"Your total bill is {bill} rs")
else:
    print("can't ride the car")
print("Thank you for visiting our park")