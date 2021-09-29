# Worksheet 12
#
http://programarcadegames.com/worksheets/show_file.php?file=worksheet_12.php

1. What is the difference between a class and an object?
 
```python
#answer
class is the classification of an object 
while an object refers to an actual instances of the class
```
 
2. What is the difference between a function and a method?

```python
#answer
a method is a function inside a class, so the function are class specific
parameter self
```
 
3. Write code to create an instance of this class and set its attributes. Remember, don't store numbers as strings. Use 40 and not "40".
```python 
class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0
```

```python
#answer
my_dog = dog()
my_dog.age = 5
my_dog.name = "Wuff"
my_dog.weight = 9
```
     
4. Write code to create two different instances of this class
    and set attributes for both objects. While a phone number is a number, those
    should be stored as strings. So we can keep leading zeros and those dashes.
```python
class Person():
    def __init__(self):
        self.name = ""
        self.cell_phone = ""
        self.email = ""
```
```python
#answer
my_number = person()
my_number.name = "my"
my_number.cell_phone = "05342"
my_number.email = "eenr@re"

ur_number = person()
ur_number.name = "ur"
ur_number.cell_phone = "0425"
ur_number.email = "emi@r"
```
     
5. For the code below, write a class that has the appropriate class name and attributes that will allow the code to work.
```python
my_bird = Bird()
my_bird.color = "green"
my_bird.name = "Sunny"
my_bird.breed = "Sun Conure"
```
```python
#answer
class Bird():
    def __init__(self):
        self.color = ""
        self.name = ""
        self.breed = ""
```
     
6. Define a class that would represent a character in a simple 2D game. Include attributes for the position, name, and strength.
```python
#answer
class character():
    def __init__(self):
        self.name = ""
        self.strength = ""
        self.posX = 0
        self.posY = 0
```
 
7. The following code runs, but it is not correct. What did the programmer do wrong?
```python     
class Person():
    def __init__(self):
        self.name = ""
        self.money = 0
 
nancy = Person()
name = "Nancy"
money = 100
```
```python
#answer
nancy = Person()
nancy.name = "Nancy"
nancy.money = 100
```     
8. Take a look at the code. It does not run. What is the error that prevents it from running?
```python 
class Person():
    def __init__(self):
        self.name = ""
        self.money = 0
 
bob = Person()
print(bob.name, "has", money, "dollars.")
```
```python
#answer
print(bob.name, "has", bob.money, "dollars.")
```
9. Even with that error fixed, the program will not print out: 

```python 
Bob has 0 dollars. 
```

Instead it just prints out:

```python 
has 0 dollars. 
```
Why is this the case?

```python
#answer
because bob is only an object with an empty name und default money of zero. We have to give the object an actual name by 
bob.name = "bob"
```
 
10. Take pairs of the following items, and list some of the ``has-a`` relationships, and the ``is-a`` relationships between them. For example, if you were working with a different list, you might pull ``Dolphin`` and ``Mammal`` and then say ``Dolphin is a Mammal.`` Please don't use items that aren't on the list.
     
* Checking account
* Person
* Mortgage account
* Customer
* Withdraw
* Bank Account
* SSN
* Transaction
* Address
* Deposit
```python
#answer
Customer is a Person
Person has an Adress
...
```
     
11. In Python, how is an ``is-a`` relationship implemented? Give an example of how it is implemented.
```python
#answer
create a parent class like class Person() and then create a child class like class customer(Person)
the class customer will inherited the parents class
```
 
12. In Python, how is a ``has-a`` relationship implemented? Give an example of how it is implemented.
```python
#answer
Attributes of the classes are "has-a" relationship. class Person(): self.Name = "" 
```
 
13. How does this ``has-a`` relationship work if an object is allowed more than one item of a given type?
    
    For example, a Customer class might have an attribute for account. So a Customer
    ``has-a`` account. But what if a customer has two accounts? Or ten? How do you
    store any number of items? We learned this back in Chapter 7. How do we make an
    attribute that can hold more than one of a given type?
    (Ask if you aren't sure.)
     
```python
#answer
create a list with the function append 
```
```python
    (10 pts.) Section 2:

To answer the next four questions, create one program. In that program will be the answers for all four questions. Make sure the program runs, and then copy/paste from the program to answer each of the questions below.
 
You should have a program that starts with three class definitions, one each for the first three questions. Then code that will create instances of each class, and that will be the answer to the last problem.
```

14. Write code that defines a class named Animal:
     
    * Add an attribute for the animal name.
    * Add an eat() method for Animal that prints ``Munch munch.``
    * A make_noise() method for Animal that prints ``Grrr says [animal name].``
    * Add a constructor for the Animal class that prints ``An animal has been born.``
     
15. A class named Cat:
     
    * Make Animal the parent.
    * A make_noise() method for Cat that prints ``Meow says [animal name].``
    * A constructor for Cat that prints ``A cat has been born.``
    * Modify the constructor so it calls the parent constructor as well.
     
16. A class named Dog:
     
    * Make Animal the parent.
    * A make_noise() method for Dog that prints ``Bark says [animal name].``
    * A constructor for Dog that prints ``A dog has been born.``
    * Modify the constructor so it calls the parent constructor as well.
     
17. A main program with:
     
    * Code that creates a cat, two dogs, and an animal.
    * Sets the name for each animal.
    * Code that calls eat() and make_noise() for each animal. (Don't forget this!)
```python
#answer
class Animal():
    def __init__(self):
        self.name = ""
        print("An animal has been born")
    def eat(self):
        print("Munch Munch")
    def make_noise(self):
        print("Grrr says ",self.name,".")

class Cat(Animal):
    def __init__(self):
        print("A cat has been born.")
        super().__init__()
    def make_noise(self):
        print("Meow says ",self.name,".")

class Dog(Animal):
    def __init__(self):
        print("A dog has been born.")
        super().__init__()
    def make_noise(self):
        print("Bark says ",self.name,".")

meow = Cat()
barf = Dog()
wuff = Dog()
ieeee = Animal()

meow.name = "miau"
barf.name = "wau"
wuff.name = "ahu"
ieeee.name = "ia"

meow.eat()
meow.make_noise()
barf.eat()
barf.make_noise()
wuff.eat()
wuff.make_noise()
ieeee.eat()
ieeee.make_noise()
```