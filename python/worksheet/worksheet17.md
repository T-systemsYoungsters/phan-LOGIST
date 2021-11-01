# Worksheet 17

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_17.php&lang=de

1. Write code to swap the values 25 and 40.
```python
my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]
```
```python
print(my_list)
temp = my_list[7]
my_list[7] = my_list[6]
my_list[6] = temp
print(my_list)
```
2. Write code to swap the values 2 and 27.
```python
my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]
```
```python
print(my_list)
temp = my_list[3]
my_list[3] = my_list[1]
my_list[1] = temp
print(my_list)
```
3. Why does the following code not work? Explain it, don't just list working code.
```python
my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
temp = my_list[0]
my_list[1] = my_list[0]
my_list[0] = temp
```
```python
because you put the temp variable back into the same position 
```
4. Show how the following numbers can be sorted using the selection sort. Show the numbers after each iteration of the outer loop, similar to what is shown in Figure 17.5. I am not looking for a copy of the code to do the sort.
```python
97   74    8   98   47   62   12   11    0   60
```
```python
[0, 74, 8, 98, 47, 62, 12, 11, 97, 60]
[0, 8, 74, 98, 47, 62, 12, 11, 97, 60]
[0, 8, 11, 98, 47, 62, 12, 74, 97, 60]
[0, 8, 11, 12, 47, 62, 98, 74, 97, 60]
[0, 8, 11, 12, 47, 62, 98, 74, 97, 60]
[0, 8, 11, 12, 47, 60, 98, 74, 97, 62]
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
```
5. Show how the following numbers can be sorted using the selection sort:
```python
74   92   18   47   40   58    0   36   29   25
```
```python
[0, 92, 18, 47, 40, 58, 74, 36, 29, 25]
[0, 18, 92, 47, 40, 58, 74, 36, 29, 25]
[0, 18, 25, 47, 40, 58, 74, 36, 29, 92]
[0, 18, 25, 29, 40, 58, 74, 36, 47, 92]
[0, 18, 25, 29, 36, 58, 74, 40, 47, 92]
[0, 18, 25, 29, 36, 40, 74, 58, 47, 92]
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]
```
6. Show how the following numbers can be sorted using the INSERTION sort. (Note: If you think the 0 gets immediately sorted into position, you are doing it wrong. Go back and re-read how this sort works.)
```python
74   92   18   47   40   58    0   36   29   25
```
```python
[74, 92, 18, 47, 40, 58, 0, 36, 29, 25]
[18, 74, 92, 47, 40, 58, 0, 36, 29, 25]
[18, 47, 74, 92, 40, 58, 0, 36, 29, 25]
[18, 40, 47, 74, 92, 58, 0, 36, 29, 25]
[18, 40, 47, 58, 74, 92, 0, 36, 29, 25]
[0, 18, 40, 47, 58, 74, 92, 36, 29, 25]
[0, 18, 36, 40, 47, 58, 74, 92, 29, 25]
[0, 18, 29, 36, 40, 47, 58, 74, 92, 25]
[0, 18, 25, 29, 36, 40, 47, 58, 74, 92]
```
7. Show how the following numbers can be sorted using the insertion sort:
```python
37   11   14   50   24    7   17   88   99    9
```
```python
[11, 37, 14, 50, 24, 7, 17, 88, 99, 9]
[11, 14, 37, 50, 24, 7, 17, 88, 99, 9]
[11, 14, 37, 50, 24, 7, 17, 88, 99, 9]
[11, 14, 24, 37, 50, 7, 17, 88, 99, 9]
[7, 11, 14, 24, 37, 50, 17, 88, 99, 9]
[7, 11, 14, 17, 24, 37, 50, 88, 99, 9]
[7, 11, 14, 17, 24, 37, 50, 88, 99, 9]
[7, 11, 14, 17, 24, 37, 50, 88, 99, 9]
[7, 9, 11, 14, 17, 24, 37, 50, 88, 99]
```
8. Explain what min_pos does in the selection sort.
```python
min_pos is the position of the smallest variable in the list. you will iterate from left to right looking for the smallest number. everytime you find a smaller number you will give this position to min_pos
```
9. Explain what cur_pos does in the selection sort.
```python
cur_pos is the position of the list. you want to put the second smallest number onto the second position in the list and so on
```
10. Explain what scan_pos does in the selection sort.
```python
scan_pos is the position which will iterate through the inner loop looking for the smallest number from the list part which isnt sorted yet
```
11. Explain what key_pos and key_value are in the insertion sort.
```python
key_pos marks the boundary between the sorted and unsorted portions of the list
key_value is value of variable which will be put in the sorted portion of the list 
every element larger than key_value will be moving 1 up in the list
```
12. Explain scan_pos in the insertion sort.
```python
scan_pos is looking for the position for the key_value
it will iterate from right to left of the sorted part
```
13. (5 pts) Look at the example sort program in the examples section here:
http://programarcadegames.com/python_examples/f.php?file=sorting_examples.py
Modify the sorts to print the number of times the inside loop is run, and the number of times the outside loop is run. Modify the program to work with a list of 100. Paste the code you used here. Run the program and list the numbers you got here. (Don't forget this part!)
```python
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
import random
 
 
def selection_sort(list):
    """ Sort a list using the selection sort """
 
    # Loop through the entire array
    for cur_pos in range(len(list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos
 
        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(list)):
 
            # Is this position smallest?
            if list[scan_pos] < list[min_pos]:
 
                # It is, mark this position as the smallest
                min_pos = scan_pos
 
        # Swap the two values
        temp = list[min_pos]
        list[min_pos] = list[cur_pos]
        list[cur_pos] = temp
 
 
def insertion_sort(list):
    """ Sort a list using the insertion sort """
 
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(list)):
 
        # Get the value of the element to insert
        key_value = list[key_pos]
 
        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1
 
        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1
 
        # Everything's been moved out of the way, insert
        # the key into the correct location
        list[scan_pos + 1] = key_value
 
 
# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(list):
    for item in list:
        print("{:3}".format(item), end="")
    print()
 
# Create two lists of the same random numbers
list1 = []
list2 = []
list_size = 10
for i in range(list_size):
    new_number = random.randrange(100)
    list1.append(new_number)
    list2.append(new_number)
 
# Print the original list
print_list(list1)
 
# Use the selection sort and print the result
print("Selection Sort")
selection_sort(list1)
print_list(list1)
 
# Use the insertion sort and print the result
print("Insertion Sort")
insertion_sort(list2)
print_list(list2)
```
```python
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
import random
import time
 
 
def selection_sort(list):
    """ Sort a list using the selection sort """
    inner = 0
    outer = 0
    # Loop through the entire array
    for cur_pos in range(len(list)):
        outer += 1
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos
 
        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(list)):
            inner += 1
            # Is this position smallest?
            if list[scan_pos] < list[min_pos]:
 
                # It is, mark this position as the smallest
                min_pos = scan_pos
 
        # Swap the two values
        temp = list[min_pos]
        list[min_pos] = list[cur_pos]
        list[cur_pos] = temp
    print("outside loop:", outer," inside loop:", inner)
 
 
def insertion_sort(list):
    """ Sort a list using the insertion sort """
    inner = 0
    outer = 0
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(list)):
        outer += 1
        # Get the value of the element to insert
        key_value = list[key_pos]
 
        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1
 
        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            inner += 1
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1
 
        # Everything's been moved out of the way, insert
        # the key into the correct location
        list[scan_pos + 1] = key_value
    print("outside loop:", outer," inside loop:", inner)
 
 
# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(list):
    for item in list:
        print("{:3}".format(item), end="")
    print()
 
# Create two lists of the same random numbers
list1 = []
list2 = []
list_size = 100
for i in range(list_size):
    new_number = random.randrange(100)
    list1.append(new_number)
    list2.append(new_number)
 
# Print the original list
print_list(list1)
 
# Use the selection sort and print the result
print("Selection Sort")
start = time.time()
selection_sort(list1)
end = time.time() - start
print(end,"seconds")
print_list(list1)
 
# Use the insertion sort and print the result
print("Insertion Sort")
start = time.time()
insertion_sort(list2)
end = time.time() - start
print(end,"seconds")
print_list(list2)
```
```python
9 54  2 82 96 54  2 37 73 64 54 83 67 65 70 53  5 13 14 72 99 23 18 19 89 30 99 70 40 44 77 84 14 97 37 49 15 44 82 97 97 30 31 71 64 46 27 51 92 46 49 86 32 95 36 91 38 96 67 75 36 60 22  7 75 58 22 51 24 52 56 32 29 55 24 73 27 29 25 34  3 49 69 13 68 79 91 76 47 87 74 44 38 15 63 48  6 67 34 41
Selection Sort
outside loop: 100  inside loop: 4950
0.000997781753540039 seconds
  2  2  3  5  6  7  9 13 13 14 14 15 15 18 19 22 22 23 24 24 25 27 27 29 29 30 30 31 32 32 34 34 36 36 37 37 38 38 40 41 44 44 44 46 46 47 48 49 49 49 51 51 52 53 54 54 54 55 56 58 60 63 64 64 65 67 67 67 68 69 70 70 71 72 73 73 74 75 75 76 77 79 82 82 83 84 86 87 89 91 91 92 95 96 96 97 97 97 99 99
Insertion Sort
outside loop: 99  inside loop: 2551
0.000997304916381836 seconds
  2  2  3  5  6  7  9 13 13 14 14 15 15 18 19 22 22 23 24 24 25 27 27 29 29 30 30 31 32 32 34 34 36 36 37 37 38 38 40 41 44 44 44 46 46 47 48 49 49 49 51 51 52 53 54 54 54 55 56 58 60 63 64 64 65 67 67 67 68 69 70 70 71 72 73 73 74 75 75 76 77 79 82 82 83 84 86 87 89 91 91 92 95 96 96 97 97 97 99 99
```