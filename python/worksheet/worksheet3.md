# Worksheet 3

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_03.php&lang=de

1. no idea what is missing. Maybe print("Done") at the end </br>
2. </br>
```python
number = float(input("Number: "))
if number < 0: 
print("The number ist negative") 
elif number == 0: 
   print("The number is Zero") 
else: 
   print("The number is positive")
```
3. </br>
```python
number = float(input("Number: ")) 
if number >= -10 and number <= 10: 
  print("Success") 
```
4. You cant see the answer option because the program will work sequential from top to bottom. You have to anwser first before seeing the options</br>
5. 	</br>
```python
x = input() #oder x = 4
if x >= 0:
  print("x is positive.")
else:
  print("x is not positive.")
```
6.   Cant find the third mistake	</br>
```python
x = input("Enter a number: ")
if x == 3: 
  print("You entered 3")
```
7. </br>
```python
answer = input("What is the name of Dr. Bunsen Honeydew's assistant? ") 
if answer == "Beaker": 
  print("Correct!") 
else: 
  print("Incorrect! It is Beaker.") 
```
8. The computer will set the value for "Glad" as  true so it will always print the text no matter what. To correct it </br>
```python
if x == "Happy" or x == "Glad":
```
9. </br>
```python
x=5
y=false
z=true
Buzz
```
10. </br>
```python
x = 5
y = 10
z = 10
print(x < y) #true
print(y < z) #false
print(x == 5) #true
print(not x == 5) #false
print(x != 5) #false
print(not x != 5) #true
print(x == "5") #false
print(5 == x + 0.00000000001) #false
print(x == 5 and y == 10) #true
print(x == 5 and y == 5) #false
print(x == 5 or y == 5) #true
```
11. </br>
```python
print("3" == "3") #true 
print(" 3" == "3") #false 
print(3 < 4) #true 
print(3 < 10) #true 
print("3" < "4") #true 
print("3" < "10") #"FALSE" pls give me an explanation. i guess python can compare strings as numbers when they have the same length right?
print( (2 == 2) == "True" ) #false 
print( (2 == 2) == True ) #true 
print(3 < "3") #error comparing 2 different data types 
```
12. </br>
```python
print("Welcome to Oregon Trail!") 
print("A. Banker") 
print("B. Carpenter") 
print("C. Farmer") 
user_input = input("What is your occupation? ") 
if user_input == "A" or user_input == "Banker": 
  money = 100 
elif user_input == "B" or user_input == "Carpenter": 
  money = 70 
elif user_input == "C" or user_input == "Farmer":
  money = 50
else:
  print("You didn't pick one of the occupation")
print("Great! you will start the game with", money, "dollars.") 
```
﻿
