#wrong commit
import random
done = False
miles = 0
distant = -20
thirst = 0
tiredness = 0
drinks = 7

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")

while done == False:
    print("")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.\n")
    first = input("What to you want to do?\n")
    if first.upper() == "Q":
        done = True
    elif first.upper() == "E":
        print("Miles traveled: ", miles)
        print("Drinks in canteen: ", drinks)
        print("The natives are ", miles-distant," miles behind you")
    elif first.upper() == "D":
        tiredness = 0
        print("The Camel is happy")
        distant = distant + random.randrange(7,15)
    elif first.upper() == "C":
        far = random.randrange(10,21)
        miles = miles + far
        print("You traveled ",far," miles")
        thirst = thirst +1
        tiredness = tiredness + random.randrange(1,4)
        distant = distant + random.randrange(7,15)
    elif first.upper() == "B":
        far = random.randrange(5,13)
        miles = miles + far
        print("You traveled ",far," miles")
        thirst = thirst +1
        tiredness = tiredness + 1
        distant = distant + random.randrange(7,15)
    elif first.upper() == "A":
        if drinks == 0:
            print("There are no drinks left")
        else:
            drinks = drinks -1
            thirst = 0
    else:
        print("Invalid Input")


    if thirst > 6:
        print("You died of thirst!")
        done = True
    elif thirst > 4:
        print("You are thirsty.")
    if tiredness > 8:
        print("Your camel is dead.")
        done = True
    elif tiredness > 5:
        print("Your camel is getting tired.")
    if miles-distant <= 0:
        print("The natives caught you. You lost")
        done = True
    elif miles-distant < 15:
        print("The natives are getting close!")
    if miles >= 200 and done == False:
        print("You Won!")
        done = True
    if done == False:
        oasis = random.randrange(20)
        if oasis == 0:
            print("You have found an oasis! You refilled the canteen. You resetted your thirst and your camel got some rest.")
            tiredness = 0
            thirst = 0
            drinks = 7
