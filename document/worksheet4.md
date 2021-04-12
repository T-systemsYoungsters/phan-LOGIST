# Worksheet 4

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_04.php&lang=de </br>
﻿
1.
```python
for i in range(10): print("Done")
```
2.
```python
for i in range(20): 
	print("Red")
	print("Gold")
```
3.
```python
for i in range(50): print((i+1)*2)
```
other option
```python
for i in range(2,101,2): print(i)
```
4. 
```python
i=10
while i>=0: 
	print(i)
	i=i-1
print("Blast off")
```
5.
```python
print("This program takes three numbers and returns the sum.")
total = 0
 
for i in range(3):
    x = int (input("Enter a number: ")) # missing int
    total = total + x # +x instead of +i
print("The total is:", total) #total instead of x 
```
6. 
```python
import random
x = random.randrange(1,11)
print (x)
```
7.
```python
import random
x = random.random()*9+1
print (x)

```
8.
```python
print("Enter 7 numbers")
total = 0
pos = 0
neg = 0
zero = 0

for i in range(7):
    x = int(input("Enter a Number\n"))
    total = total + x
    if x < 0: neg = neg +1
    elif x > 0: pos =pos +1
    else : zero = zero +1
print("sum: ",total)
print("positive numbers: ",pos," negative numbers: ",neg," Zeros: ",zero) 
```

9.
```python
import random
head = 0
tail = 0
for i in range(50):
    x=random.randrange(0,2)
    if x==1:
        print("head")
        head = head+1
    else:
        print ("tail")
        tail = tail+1
print("heads: ",head," tails: ",tail)

```

10.
```python
import random
stop = False

print("Rock Scissor Paper Game")
while not stop:
    x = random.randrange(0,3)
    print("0 = Rock, 1 = Scissor, 2 = Paper")
    user = int(input("Enter a Number\n"))
    if user == 0: print("You choose Rock")
    elif user == 1: print ("You choose Scissor")
    else: print ("You choose Paper")
    if x == 0: print("Computer choose Rock")
    elif x == 1: print ("Computer choose Scissor")
    else: print ("Computer choose Paper")
    if x == user:
        print("It's a Draw")
    elif x == 0 and user == 1: print("Computer Wins!")
    elif x == 0 and user == 2: print("User Wins!")
    elif x == 1 and user == 0: print("User Wins!")
    elif x == 1 and user == 2: print("Computer Wins!")
    elif x == 2 and user == 0: print("Computer Wins!")
    elif x == 2 and user == 1: print("User Wins!")
    else:print("Error")
    
    a = input("Do you wanne stop? (y/n)")
    if a == "yes" or a == "y":
        stop = True
```
