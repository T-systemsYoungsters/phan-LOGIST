# Chapter 9

## Exercise
```python
# Example 1
def a():
    print("A")
 
def b():
    print("B")
 
def c():
    print("C")
 
a()
# my answer
A
```
```python
# Example 2
def a():
    b()
    print("A")
 
def b():
    c()
    print("B")
 
def c():
    print("C")
 
a()
# my answer
C
B
A
```
```python
# Example 3
def a():
    print("A")
    b()
 
def b():
    print("B")
    c()
 
def c():
    print("C")
 
a()
# my answer
A
B
C
```
```python
# Example 4
def a():
    print("A start")
    b()
    print("A end")
 
def b():
    print("B start")
    c()
    print("B end")
 
def c():
    print("C start and end")
 
a()
# my answer
A start
B start
C start and end
B end
A end
```
```python
# Example 5
def a(x):
    print("A start, x =",x)
    b(x + 1)
    print("A end, x =",x)
 
def b(x):
    print("B start, x =",x)
    c(x + 1)
    print("B end, x =",x)
 
def c(x):
    print("C start and end, x =",x)
 
a(5)
# my answer
A start, x = 5
B start, x = 6
C start and end, x = 7
B end, x = 6
A end, x = 5
```
```python
# Example 6
def a(x):
    x = x + 1
 
x = 3
a(x)
 
print(x)
# my answer
3
```
```python
# Example 7
def a(x):
    x = x + 1
    return x
 
x = 3
a(x)
 
print(x)
# my answer
3
```
```python
# Example 8
def a(x):
    x = x + 1
    return x
 
x = 3
x = a(x)
 
print(x)
# my answer
4
```
```python
# Example 9
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)
 
x = 10
y = 20
a(y, x)
# my answer
21 11
```
```python
# Example 10
def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y
 
x = 10
y = 20
z = a(x, y)
 
print(z)
# my answer
Error double return
# actual answer
11
```
```python
# Example 11
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y
 
x = 10
y = 20
z = a(x, y)
 
print(z)
# my answer
[11, 21]
# actual answer
(11, 21)
```
```python
# Example 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y
 
x = 10
y = 20
x2, y2 = a(x, y) # Most computer languages don't support this
 
print(x2)
print(y2)
# my answer
(11, 21)
(11, 21)
# actual answer
11
21
```
```python
# Example 13
def a(my_data):
    print("function a, my_data =  ", my_data)
    my_data = 20
    print("function a, my_data =  ", my_data)
 
my_data = 10
 
print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)
# my answer
global scope, my_data = 10
function a, my_data =   10
function a, my_data =   20
global scope, my_data = 10
```
```python
# Example 14
def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)
 
my_list = [5, 2, 4]
 
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)
# my answer
global scope, list = [5, 2, 4]
function a, list =   [5, 2, 4]
function a, list =   [10, 20, 30]
global scope, list = [5, 2, 4]
```
```python
# Example 15
# New concept!
# Covered in more detail in Chapter 12
def a(my_list):
    print("function a, list =  ", my_list)
    my_list[0] = 1000
    print("function a, list =  ", my_list)
 
my_list = [5, 2, 4]
 
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)
# my answer
global scope, list = [5, 2, 4]
function a, list =   [5, 2, 4]
function a, list =   [1000, 2, 4]
global scope, list = [5, 2, 4]
# actual answer
global scope, list = [5, 2, 4]
function a, list =   [5, 2, 4]
function a, list =   [1000, 2, 4]
global scope, list = [1000, 2, 4]
```
```python
"""
This is a sample text-only game that demonstrates the use of functions.
The game is called "Mudball" and the players take turns lobbing mudballs
at each other until someone gets hit.
"""
 
import math
import random
 
 
def print_instructions():
    """ This function prints the instructions. """
 
    # You can use the triple-quote string in a print statement to
    # print multiple lines.
    print("""
Welcome to Mudball! The idea is to hit the other player with a mudball.
Enter your angle (in degrees) and the amount of PSI to charge your gun
with.
        """)
 
 
def calculate_distance(psi, angle_in_degrees):
    """ Calculate the distance the mudball flies. """
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance
 
 
def get_user_input(name):
    """ Get the user input for psi and angle. Return as a list of two
    numbers. """
    # Later on in the 'exceptions' chapter, we will learn how to modify
    # this code to not crash the game if the user types in something that
    # isn't a valid number.
    psi = float(input(name + " charge the gun with how many psi? "))
    angle = float(input(name + " move the gun at what angle? "))
    return psi, angle
 
 
def get_player_names():
    """ Get a list of names from the players. """
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True
 
    print()
    return players
 
 
def process_player_turn(player_name, distance_apart):
    """ The code runs the turn for each player.
    If it returns False, keep going with the game.
    If it returns True, someone has won, so stop. """
    psi, angle = get_user_input(player_name)
 
    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart
 
    # By looking ahead to the chapter on print formatting, these
    # lines could be made to print the numbers is a nice formatted
    # manner.
    if difference > 1:
        print("You went", difference, "yards too far!")
    elif difference < -1:
        print("You were", difference * -1, "yards too short!")
    else:
        print("Hit!", player_name, "wins!")
        return True
 
    print()
    return False
 
 
def main():
    """ Main program. """
 
    # Get the game started.
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)
 
    # Keep looking until someone wins
    done = False
    while not done:
        # Loop for each player
        for player_name in player_names:
            # Process their turn
            done = process_player_turn(player_name, distance_apart)
            # If someone won, 'break' out of this loop and end the game.
            if done:
                break
 
if __name__ == "__main__":
    main()
```
# Worksheet 9

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_09.php&lang=de

## Part a
1. Block 1
```python
for i in range(5):
    print(i + 1)
#guess
1
2
3
4
5
#actual
```
2. Block 2
```python
for i in range(5):
    print(i)
    i = i + 1
#guess 
0
1
2
3
4
#actual
```
3. Block 3
```python
x = 0
for i in range(5):
    x += 1
print(x)
#guess
5
#actual
```
4. Block 4
```python
x = 0
for i in range(5):
    for j in range(5):
        x += 1
print(x)
#guess
25
#actual
```
5. Block 5
```python
for i in range(5):
    for j in range(5):
        print(i, j)
#guess
0 0
0 1
0 2
...
4 3
4 4
#actual
```
6. Block 6
```python
for i in range(5):
    for j in range(5):
        print("*", end="")
        print()
#guess
************************
#actual
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
```
7. Block 7
```python
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
#guess
*****
*****
*****
*****
*****
#actual
```
8. Block 8
```python
for i in range(5):
    for j in range(5):
        print("*", end="")
print()
#guess
************************
#actual
```
9. Block 9
```python
# This is supposed to sum a list of numbers
# What is the mistake here?
my_list = [5, 8, 10, 4, 5]
i = 0
for i in my_list:
    i = i + my_list[i]
print(i)
#guess
i in the for loop will be overwritten. Use another global variable
#actual
```
10. Block 10
```python
for i in range(5):
    x = 0
    for j in range(5):
        x += 1
print(x)
#guess
5
#actual
```
11. Block 11
```python
import random
play_again = "y"
while play_again == "y":
    for i in range(5):
        print(random.randrange(2), end="")
    print()
    play_again = input("Play again? ")
print("Bye!")
#guess
it will print 5 numbers(1 or 0) next to each other out and will ask again, if you want to do it again 
#actual
```
12. Block 12
```python
def f1(x):
    print(x)
y = 3
f1(y)
#guess
3
#actual
```
13. Block 13
```python
def f2(x):
    x = x + 1
    print(x)
y = 3
f2(y)
print(y)
#guess
4
3
#actual
```
14. Block 14
```python
def f3(x):
    x = x + 1
    print(x)
x = 3
f3(x)
print(x)
#guess
4
3
#actual
```
15. Block 15
```python
def f4(x):
    z = x + 1
    print(z)
x = 3
f4(x)
print(z)
#guess
Error z not defined
#actual
```
16. Block 16
```python
def foo(x):
    x = x + 1
    print("x=", x)
 
x = 10
print("x=", x)
foo(x)
print("x=", x)
#guess
x= 10
x= 11
x= 10
#actual
```
17. Block 17
```python
def f():
    print("f start")
    g()
    h()
    print("f end")
 
def g():
    print("g start")
    h()
    print("g end")
 
def h():
    print("h")
f()
#guess
f start
g start
h
g end
h
f end
#actual
```
18. Block 18
```python
def foo():
    x = 3
    print("foo has been called")
 
x = 10
print("x=", x)
foo()
print("x=", x)
#guess
x= 10
foo has been called
x= 10
#actual
```
19. Block 19
```python
def a(x):
    print("a", x)
    x = x + 1
    print("a", x)
 
x = 1
print("main", x)
a(x)
print("main", x)
 
def b(y):
    print("b", y[1])
    y[1] = y[1] + 1
    print("b", y[1])
 
y=[123, 5]
print("main", y[1])
b(y)
print("main", y[1])
 
def c(y):
    print("c", y[1])
    y = [101, 102]
    print("c", y[1])
 
y = [123, 5]
print("main", y[1])
c(y)
print("main", y[1])
#guess
main 1
a 1
a 2
main 1
main 5
b 5
b 6
main 6
main 5
c 5
c 102
main 5
#actual
```
## Part b
### correcting code
1. Correct the following code: (Don't let it print out the word ``None'')
```python
# given
def sum(a, b, c):
    print(a + b + c)
 
print(sum(10, 11, 12))
# guess
def sum(a, b, c):
    return(a + b + c)
 
print(sum(10, 11, 12))
```
2. Correct the following code: (x should increase by one, but it doesn't.)
```python
#given
def increase(x):
    return x + 1
 
x = 10
print("X is", x, " I will now increase x." )
increase(x)
print("X is now", x)
#guess
def increase(x):
    return x + 1
 
x = 10
print("X is", x, " I will now increase x." )
x = increase(x)
print("X is now", x)
```
3. Correct the following code:
```python
#given
def print_hello:
    print("Hello")
 
print_hello()
#guess
def print_hello():
    print("Hello")
 
print_hello()
```
4. Correct the following code:
```python
#given
def count_to_ten():
    for i in range[10]:
        print(i)
 
count_to_ten()
#guess
def count_to_ten():
    for i in range(11):
        print(i)
 
count_to_ten()
```
5. Correct the following code:
```python
#given
def sum_list(list):
    for i in list:
        sum = i
        return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))
#guess
def sum_list(list):
    summ = 0
    for i in list:
        summ = summ + i
    return summ
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))
```
6. Correct the following code: (This almost reverses the string. What is wrong?)
```python
#given
def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))
#guess
def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[text_length -1 -i]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))
```
7. Correct the following code:
```python
#given
def get_user_choice():
    while True:
        command = input("Command: ")
        if command = f or command = m or command = s or command = d or command = q:
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)
#guess
def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)
```
## Part c
```python
# 1. Write a function that prints out ``Hello World.''

def print_hello():
    print("Hello World.")

# 2. Write code that will call the function in the prior problem.

def print_hello():
    print("Hello World.")
print_hello()

# 3. Write a function that prints out ``Hello Bob'', and will take a parameter to let the caller specify the name. Do not put an input statement inside the function! Use a parameter.

def print_name(x):
    print("Hello ", x)

#4. Write code that will call the function in the prior problem.
print_name("Bob")

#5. Write a function that will take two numbers as parameters (not as input from the user) and print their product (i.e. multiply them).
def prod(x,y):
    print(x * y)

#6. Write code that will call the prior function.
prod(4,2)

#7. Write a function that takes in two parameters. The first parameter will be a string named phrase. The second parameter will be a number named count. Print phrase to the screen count times. (e.g., the function takes in "Hello" and 5, then prints "Hello" five times.)
def cop(x, y):
    for i in range(y):
        print(x)

#8. Write code to call the previous function.
cop("Hello", 5)

#9. Write code for a function that takes in a number, and returns the square of that number. (I'm not asking for the square root, but the number squared.) Note, this function should RETURN the answer, not print it out.
def pro(x):
    return x*x

#10. Write code to call the function above and print the output.
print(pro(5))

#11.
"""Write a function that takes three numbers as parameters, and returns the centrifugal force. The formula for centrifugal force is:
F=m(v^2/r)
F is force, m is mass, r is radius, and v is angular velocity."""
def cen_force(m,v,r):
    return (m*(v*v/r))

#12.Write code to call the function above and display the result.
print(cen_force(4,2,5))

#13. Write a function that takes a list of numbers as a parameter, and prints out each number individually using a for loop.
def read_list(x):
    for item in range(len(x)):
        print(x[item])
```