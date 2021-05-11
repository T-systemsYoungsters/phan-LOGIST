# Lab 9
"""
Write a function called min3 that will take three numbers as parameters and return the smallest value. 
If more than one number tied for smallest, still return that smallest number. 
Use a proper if/elif/else chain. 
Once you've finished writing your function, copy/paste the following code and make sure that it runs against the function you created:
"""
def min3(x,y,z):
    if x <= y and x <= z:
        return x
    elif y <= z and y <= x:
        return y
    elif z <= x and z <= y:
        return z
    else:
        print("There is a mistake")

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

def box(height,width):
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print("")

box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

def find(list_x, key):
    for item in range(len(list_x)):
        if key == list_x[item]:
            print("found", key, "at position", item)

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
 
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

# 4. Write one program that has the following:
import random
def create_list(x):
    mylist=[]
    for item in range(x):
        mylist.append(random.randrange(1,7))
    return mylist

my_list = create_list(5)
print(my_list)

def count_list(list, key):
    count = 0
    for i in range(len(list)):
        if key == list[i]:
            count = count + 1
    return count

count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

def average_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return (sum / len(list))

avg = average_list([1,2,3])
print(avg)

new_list = create_list(10000)
for i in range(1,7):
    count = count_list(new_list, i)
    print(count)
print(average_list(new_list))    
    