total = 0

question1 = input("Whats my name?: ")

if question1 == "Tom":
    print("Right!")
    total = total + 1
    print("+1")
else:
    print("No")
    print("+0")


question2 = input("How old am I?: ")

if question2 == "17":
    print("Correct!")
    total = total + 1
    print("+1")
else:
    print("Sadly no :(")
    print("+0")

question3 = input("Whats my favourite color?: ")

if question3 == "Yellow" or question3 == "yellow":
    print("Yes!")
    total = total + 1
    print("+1")
else:
    print("You will get the next one rigth!")
    print("+0")

question4 = input("Whats my favourite food?: ")

if question4 == "Pizza" or question4 == "pizza":
    print("Exactly!")
    total = total + 1
    print("+1")
else:
    print("Wrong")
    print("+0")


print("Your score was:" + str(total) + "/4")





    

    


