# Worksheet 19

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_19.php&lang=de

When answering these questions, remember that recursion is not simply ``repeating'' a task over and over. That could be done by a loop. A loop isn't recursion. Recursion is anything that is defined in terms of itself.

1. "To understand recursion, one must first understand recursion." Explain the joke. (Make sure to ask if you don't get this or the ones below.)
```python
you are basically recalling the joke over and over again as if it would be a recursiv function
```
2. Two mirrors face each other. Explain how their reflections demonstrate the property of recursion.
```python
each mirror is reflecting each other as if 2 function are calling each other over and over again
```
3. Explain how Multi-Level Marketing (MLM) uses recursion. If you don't know what MLM is, look it up. Also, pro-life tip: avoid MLM.
```python
MLM functions like a inheritance. Every new recruit inherit the function to recruit new people. So MLM will always trying to recruit new people
```
4. Explain how the "sweep" function in the classic minesweeper game could be done with recursion. If you don't know, ask!
```python
if you click on one of the field you will check every field around the one you click and depending if there is a bomb a not return a number of how many bombs there are also recall the click on the field if there is no bomb on the field next to it
```
5. Explain how finding your way out of a maze could be done with recursion.
```python
to be honest i dont know how 
i would assume always going back to an insection if get into a dead end
so i just google the solution 
and it seems you multiple steps and you recursive back to your first step
while the first step is always checking if you already out otherwise go in one direction until a dead a and change the direction. it is similar to the "wall following" method
```
6. Use the Chrome browser and create your own screenshot at:
http://juliamap.googlelabs.com
Use your mouse and mouse wheel to zoom into an interesting part of the fractal. Copy the URL and paste it here.
```
cant open the link safari. Have to check with chrome later
```
7. (5 pts) Write a recursive function f(n) that takes in a value n and returns the value for f, given the definition below. (If you are viewing this in a text file, the line below will look like gibberish. Go on-line or look in the book for the correctly formatted equation.)
```python
def f(n):
    if n==1:
        return 6
    if n>1:
        return 0.5 * f(n-1) +4
        
for y in range(1,11):    
    print(f(y))
```
8. (5 pts) Write recursive code that will print out the first 10 terms of the sequence below. (If you are viewing this in a text file, the line below will look like gibberish. Go on-line or look in the book for the correctly formatted equation.)
```python
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n>2:
        return f(n-1)+f(n-2)

for x in range(1,11):
    print(f(x))
```