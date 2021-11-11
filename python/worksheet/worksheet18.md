# Worksheet 18

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_18.php&lang=de

1. (6 pts) Define the following terms in your own words. Don't just copy/paste from the book:
- Exception
- Exception Handling
- Try block
- Catch block
- Unhandled exception
- Throw
```python
Exception: irregular flow in programm code or data error
Exception Handling: is how to deal with the exception 
Try Block: the part which one you want to test for the exception
Catch Block: the Exception you expect and how you handle them
Unhandled exception: An Exception that never get catched resulting in ending the programm flow
Throw: Detecting a Exception and creating exception Object
```
2. Show how to modify the following code so that an error is printed if the number conversion is not successful. Modify this code, don't just copy the example from the text. Do NOT ask again if the conversion is unsuccessful.
```python
user_input_string = input("Enter a number:")
user_value = int(user_input_string)
```
```python
try:
    user_input_string = input("Enter a number:")
    user_value = int(user_input_string)
except:
    print("wrong input")
```
3. What will the following code output? Predict, and then run the code to see if you are correct. Write your prediction here and if you are right. If you aren't, make sure you understand why. (Make sure to write both the prediction, and the actual results. No credit will be given if you just list the results or the prediction. If the program raises an error, list that fact for this and the next problem as well.)
```python
x = 5
y = 0
print("A")
try:
    print("B")
    a = x / y
    print("C")
except:
    print("D")
print("E")
print(a)
```
```python
# Prediction Output
A
B
D
# actual Output
A
B
D
E
Error a not defined 

I thought that after the exception the programm will break. Instead it moved on and a new Error accured variable was never defined because the code exclude the line through a exception handling. 

```
4. What will the following code output? Predict, and then run the code to see if you are correct. Write your prediction here and if you are right. If you aren't, make sure you understand why.
```python
x = 5
y = 10
print("A")
try:
    print("B")
    a = x / y
    print("C")
except:
    print("D")
print("E")
print(a)
```
```python
# Prediction Output
A
B
C
E
0.5
# Actual Output
A
B
C
E
0.5
```
