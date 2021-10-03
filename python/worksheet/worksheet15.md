#  Worksheet 15 

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_15.php&lang=de


### Answer the following, assuming a program uses the linear search:

1. If a list has n elements, in the best case how many elements would the computer need to check before it found the desired element?
```python
1 Element
```
2. If a list has n elements, in the worst case how many elements would the computer need to check before it found the desired element? (Remember, give your answer in terms of n.)
```python
n Elements
```
3. If a list has n elements, how many elements need to be checked to determine that the desired element does not exist in the list?
```python
n Elements
```
4. If a list has n elements, what would the average number of elements be that the computer would need to check before it found the desired element?
```python
n Elements assuming average number is also nearly as the worst case
```
5. (2 pts) Take the example linear search code and put it in a function called linear_search. Take in the list along with the desired element as parameters. Return the position of the element, or -1 if it was not found. Remember, RETURN the value. If your function has a print statement in it, you are doing it wrong. Once you've written the function, try it out with the following code to see if it works:
```python
# --- Put your definition for linear_search right below:
 
def linear_search(list, key):
    i = 0
    while i < len(list) and list[i] != key:
        i += 1
    if i < len(list):
        return i
    else: 
        return -1

# --- Now if the function works, all these tests should pass:
 
my_list = [4, 3, 2, 1, 5, 7, 6]
 
r = linear_search(my_list, 3)
if r == 1:
    print("Test A passed")
else:
    print("Test A failed. Expected 1 and got", r)
 
r = linear_search(my_list, 2)
if r == 2:
    print("Test B passed")
else:
    print("Test B failed. Expected 2 and got", r)
 
r = linear_search(my_list, 10)
if r == -1:
    print("Test C passed")
else:
    print("Test C failed. Expected -1 and got", r)
```

### Answer the following, assuming a program uses the binary search, and the search list is in order:
1. If a list has n elements, in the best case how many elements would the computer need to check before it found the desired element?
```python
1 Element
```
2. If a list has n elements, in the worst case how many elements would the computer need to check before it found the desired element?
```python
log base 2 from n Elements
```
3. If a list has n elements, how many elements need to be checked to determine that the desired element does not exist in the list?
```python
log base 2 from n Elements
```
4. If a list has n elements, what would the average number of elements be that the computer would need to check before it found the desired element?
```python
log base 2 from n Elements assuming average number is also nearly as the worst case
```
5. (2 pts.) Take the example binary search code and put it in a function named binary_search. Take in the list along with the desired element as parameters. Return the position of the element, or -1 if it was not found. Once you've written the function, try it out with the following code to see if it works:
```python
# --- Put your definition for binary_search right below:
 
def binary_search(list, key):
    lower_bound = 0
    upper_bound = len(list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound+upper_bound)//2
        if list[middle_pos] < key:
            lower_bound = middle_pos +1
        elif list[middle_pos] > key:
            upper_bound = middle_pos -1
        else:
            found = True

    if found:
        return middle_pos
    else: 
        return -1

# --- Now if the function works, all these tests should pass:
 
my_list = [0, 3, 5, 12, 18, 50, 70, 78]
 
r = binary_search(my_list, 3)
if r == 1:
    print("Test A passed")
else:
    print("Test A failed. Expected 1 and got", r)
 
r = binary_search(my_list, 5)
if r == 2:
    print("Test B passed")
else:
    print("Test B failed. Expected 2 and got", r)
 
r = binary_search(my_list, 10)
if r == -1:
    print("Test C passed")
else:
    print("Test C failed. Expected -1 and got", r)
```

6. (3 pts.) Does the following function correctly detect whether a list contains at least one positive element? (1 pt.) Write code to try it out. Explain why it does work or why it does not work. (1 pt.) Come up with working code. (1 pt.)
```python
def detect_positive(list):
    for element in list:
        if element > 0:
            return True
        else:
            return False
```
```python
No it doesnt work. It will only compare the first element and make the decision then. The mistake is in the 5 and 6 Line. The program will automaticly cancel the loop after the first element because of the return statement wether the first element is bigger than 0 or not

def detect_positive(list):
    for element in list:
        if element > 0:
            return True
    else:
        return False
```