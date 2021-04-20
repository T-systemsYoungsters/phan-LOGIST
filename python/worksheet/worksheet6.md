# Worksheet 6

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_06.php&lang=de

Extra Stuff from Chapter 6 Diamond of Numbers
```python
for row in range(1,9):
    for space in range(9-row): print("  ", end="")
    for column in range(1,row+1): 
        print(column, end=" ")
    for i in range(row,1,-1):print(i-1, end=" ")
    print()
for row in range(9): 
    for space in range(row): print("  ", end="")
    for column in range(9-row): print(column+1, end=" ")
    for i in range(8-row,0,-1): print(i, end=" ")
    print()
```

1. What does this program print out? (Remember: TWO answers. Your guess and the actual result. Label both.)
```python
#given code
x = 0
while x < 10:
    print(x)
    x = x + 2
#My answer left - Terminal output right
0                 0
2                 2
4                 4
6                 6 
8                 8
```
2. What does this program print out?
```python
#given code
x = 1
while x < 64:
    print(x)
    x = x * 2
#My answer left - Terminal output right
1                 1
2                 2
4                 4
8                 8 
16                16
32                32
```
3. Why is the ''and x >= 0'' not needed?
```python
#given code
x = 0
while x < 10 and x >= 0:
    print(x)
    x = x + 2
#because the starting value is 0 and this is already smaller than 10. Secondly x will get bigger in the while loop, so it will always be bigger than 0
```
4. What does this program print out? (0 pts) Explain. (1 pt)
```python
#given code
x = 5
while x >= 0:
    print(x)
    if x == "1":
        print("Blast off!")
    x = x - 1
#my answer
5
4
3
2
1
Blast off!
0
#when x gonna hit 1, then the programm will print out Blast off! but the while loop isnt finished, so it will countinue printing number until x smaller than 0
```
5. Fix the following code so it doesn't repeat forever, and keeps asking the user until he or she enters a number greater than zero: (2 pts)
```python
#given code
x = float(input("Enter a number greater than zero: "))
 
while x <= 0:
    print("Too small. Enter a number greater than zero: ")
#my answer
x = float(input("Enter a number greater than zero: "))
 
while x <= 0:
    x = float(input("Too small. Enter a number greater than zero: "))
```
6. Fix the following code:
```python
x = 10
 
while x < 0:
    print(x)
    x - 1
 
print("Blast-off")
#my answer
x = 10
 
while x > 0:
    print(x)
    x = x - 1
 
print("Blast-off")
```
7. What is wrong with this code? It runs but it has unnecessary code. Find all the unneeded code. Also, answer why it is not needed. (1 pt)
```python
i = 0
for i in range(10):
    print(i)
    i += 1
#my answer
for i in range(10):
    print(i)
#the for loop "for i in range(a,b,c):" needs 3 parameter a for starting value, b for end value, c for the increment. The default value for a is 0 and c is 1. b is a necessary value
```
8. Explain why the values printed for x are so different. (2 pts)
```python
# Sample 1
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1
print(x)
 
# Sample 2
x = 0
for i in range(10):
    x += 1
    for j in range(10):
        x += 1
print(x)
#my answer
#Sample 1 has to independent loops so is gonna loop 10 times and then x gonna loop 10 times agains in total 20
#Sample 2 has a loop in a loop. For each i loop, j will loop 10 times
```
