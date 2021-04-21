# Chapter 7

## Exercise

7.6 

Exercise: Starting with the following code:
```python
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
n = int(input("Enter a month number: "))
```
Print the three month abbreviation for the month number that the user enters. (Calculate the start position in the string, then use the info we just learned to print out the correct substring.)

```python
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
n = int(input("Enter a month number: "))

for i in range(3*n-3,n*3):
    output = months[i]
    print(output, end="")
```

# Worksheet 7

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_07.php&lang=de

1. List the four types of data we've covered, and give an example of each: </br>
```python
int --> interger numbers like 4; 6; -3 
float --> decimal numbers like 1.435; 3.5343; -12.432 
bool --> True or False 
str --> string of character like ["Hi", "Hello World"]
```

2. What does this code print out? For this and the following problems, make sure you understand WHY it prints what it does. You don't have to explain it, but if you don't understand why, make sure to ask. Otherwise you are wasting your time doing these.
```python
#given code
my_list = [5, 2, 6, 8, 101]
print(my_list[1])
print(my_list[4])
print(my_list[5])
#my answer
5
8
101
```
3. What does this code print out?
```python
#given code
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)
#my answer
5
2
6
8
101
```
4. What does this code print out?
```python
#given code
my_list1 = [5, 2, 6, 8, 101]
my_list2 = (5, 2, 6, 8, 101)
my_list1[3] = 10
print(my_list1)
my_list2[2] = 10 
print(my_list2)
#my answer
[5, 2, 10, 8, 101]
(5, 2, 6, 8, 101)
#actual answer
[5, 2, 10, 8, 101]
# line my_list2[2] = 10 gives an error
```
5. What does this code print out?
```python
#given code
my_list = [3 * 5]
print(my_list)
my_list = [3] * 5
print(my_list)
#my answer
[15]
[3, 3, 3, 3, 3]
```
6. What does this code print out?
```python
#given code
my_list = [5]
for i in range(5):
    my_list.append(i)
print(my_list)
#my answer
[5, 0, 1, 2, 3, 4]
```
7. What does this code print out?
```python
#given code
print(len("Hi"))
print(len("Hi there."))
print(len("Hi") + len("there."))
print(len("2"))
print(len(2))
#my answer
2
9
8
1
1 # Type Error 
```
8. What does this code print out?
```python
#given code
print("Simpson" + "College")
print("Simpson" + "College"[1])
print( ("Simpson" + "College")[1] )
#my answer
SimpsonCollege
SimpsonC
S
#actual answer
SimpsonCollege
Simpsono
i 
```
9. What does this code print out?
```python
#given code
word = "Simpson"
for letter in word:
    print(letter)
#my answer
S
i
m
p
s
o
n
```
10. What does this code print out?
```python
#given code
word = "Simpson"
for i in range(3):
    word += "College"
print(word)
#my answer
SimpsonCollegeCollegeCollege
```
11. What does this code print out?
```python
#given code
word = "Hi" * 3
print(word)
#my answer
HiHiHi
```
12. What does this code print out?
```python
#given code
my_text = "The quick brown fox jumped over the lazy dogs."
print("The 3rd spot is: " + my_text[3])
print("The -1 spot is: " + my_text[-1])
#my answer
The 3rd spot is: e
The -1 spot is: # Index Error
#actul answer
The 3rd spot is:  
The -1 spot is: .
```
13. What does this code print out?
```python
#given code
s = "0123456789"
print(s[1])
print(s[:3])
print(s[3:])
#my answer
1
012
3456789
```
14. Write a loop that will take in a list of five numbers from the user, adding each to an array. Then print the array. Try doing this without looking at the book.
```python
#my answer
list = []
for i in range(5):
    x = int(input("Please Enter your: "))
    list.append(x)
print(list)
```
15. Write a program that take an array like the following, and print the average. Use the len function, don't just use 15, because that won't work if the list size changes. (There is a sum function I haven't told you about. Don't use that. Sum the numbers individually as shown in the chapter.) (Also, a common mistake is to calculate the average each time through the loop to add the numbers. Finish adding the numbers before you divide.)
```python
#given code
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
#my answer
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

add = 0
for item in my_list:
    add = add + item
average = add / len(my_list)
print(average)
```