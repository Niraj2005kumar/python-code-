import random
com= random.randint(1,100)

while True:

    hum = int(input("guss your number "))

    if hum == com:
        print("congratulation you have won ")

    elif hum> com:
        print ("sorry wrong guss go lower ")

    elif hum < com:
        print("sorry wrong guess go higher !")