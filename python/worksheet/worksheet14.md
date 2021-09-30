# Worksheet 14

http://programarcadegames.com/index.php?chapter=libraries&lang=de

1. What is a Python library?
```
A Python library is a external code file from which you want to use the function from.

A collection of functions and/or classes that can be imported into a project.
```
2. What are some of the reasons why a programmer would want to create his/her own library file?
```
- easier to reuse function you may need for another programm
- working simultaneously
- you dont have to reinvent the wheel
- breaking the code in smaller parts to easier usage
- easily sharing
```
3. There are two ways to import library files in Python. Give an example of each.
```python
# import foo
from my_functions import *
 
foo()
```
```python
# Import the my_functions.py file
import my_functions
 
# Foo call that does work
my_functions.foo()
```
4. How do calls to functions and classes differ depending on how the library is imported?
```
You can differ them by their namespace
```
5. Can library files import other library files?
```
Yes 
```
6. What is a "namespace?"
```
The namespace is name from which you want to use the function from
```