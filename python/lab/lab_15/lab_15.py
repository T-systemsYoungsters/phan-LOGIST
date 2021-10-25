import os
import re
import time

# Changing working Directory to current Directory for the right files
path = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to split apart words in a string and return them as a list
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

# open dictionary.txt and append it to dictionary_list
file = open("dictionary.txt")
dictionary_list = []
for line in file:
    line = line.strip()
    dictionary_list.append(line)
file.close()

print(" --- Linear Search --- ")
start = time.time()
file2 = open("AliceInWonderLand200.txt")
# if you dont want to use enumerate you can use line_number as the index number 
line_number = 0
for index, line in enumerate(file2, start=1):
    words = split_line(line)
    line_number += 1
    for word in words:
        i = 0
        found = False
        while i < len(dictionary_list) and not found:
            if word.upper() == dictionary_list[i]:
                found = True
            i += 1
        
        if found == False and i >= len(dictionary_list):
            # instead of index you can also use line number
            print("Line", index, "possible misspelled word:", word)

file2.close()
end = time.time() - start
print(end,"seconds")
print(" --- Binary Search --- ")
start = time.time()
file2 = open("AliceInWonderLand200.txt")
# if you dont want to use enumerate you can use line_number as the index number 
line_number = 0
for index, line in enumerate(file2, start=1):
    words = split_line(line)
    line_number += 1
    for word in words:
        i = 0
        found = False
        lower_bound = 0
        upper_bound = len(dictionary_list)-1
        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2
     
            if dictionary_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True
        
        if found == False:
            # instead of index you can also use line number
            print("Line", index, "possible misspelled word:", word)

file2.close()
end = time.time() - start
print(end,"seconds")

start = time.time()
file2 = open("AliceInWonderLand200.txt")
# if you dont want to use enumerate you can use line_number as the index number 
line_number = 0
for index, line in enumerate(file2, start=1):
    words = split_line(line)
    line_number += 1
    for word in words:
        if word.upper() not in dictionary_list:
            print(word)
file2.close()
end = time.time() - start
print(end,"seconds")