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
"""
Write a function called box that will output boxes given a height and width. 
Once you've finished writing your function, copy and 
paste the following code after it and make sure it works with the function you wrote:
"""
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
"""
Write a function called find that will take a list of numbers, my_list, along with one other number, key. 
Have it search the list for the value contained in key. 
Each time your function finds the key value, print the array position of the key. 
You will need to juggle three variables, one for the list, one for the key, and one for the position of where you are in the list.
This code will look similar to the Chapter 7 code for iterating though a list using the range and len functions. 
Start with that code and modify the print to show each element and its position. 
Then instead of just printing each number, add an if statement to only print the ones we care about.
"""
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

"""
Write a function named create_list that takes in a list size and returns a list of random numbers from 1-6. i.e., 
calling create_list(5) should return 5 random numbers from 1-6. 
(Remember, Chapter 7 has code showing how to do something similar, creating a list out of five numbers the user enters. 
Here, you need to create random numbers rather than ask the user.)
Write a function called count_list that takes in a list and a number. 
Have the function return the number of times the specified number appears in the list.
To test, use this code against the function you wrote:
Write a function called average_list that returns the average of the list passed into it.
To test, use this code against the function you wrote:
"""

def average_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return (sum / len(list))

avg = average_list([1,2,3])
print(avg)

"""
Now that the functions have been created, use them all in a main program that will:
Create a list of 10,000 random numbers from 1 to 6. This should take one line of code. Use the function you created earlier in the lab.)
Print the count of 1 through 6. (That is, print the number of times 1 appears in the 10,000. And then do the same for 2-6.)
Print the average of all 10,000 random numbers.
"""

new_list = create_list(10000)
for i in range(1,7):
    count = count_list(new_list, i)
    print(count)
print(average_list(new_list))    
    