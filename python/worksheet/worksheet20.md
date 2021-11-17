# Worksheet 20

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_20.php&lang=de

1. format the first to prints
```python
score = 41237
highscore = 1023407
 
print("Score:      " + str(score) )
print("High score: " + str(highscore) )

print("Score:      {:9,}".format(score))
print("High score: {:9,}".format(highscore))
```
2. Create a program that loops from 1 to 20 and lists the decimal equivalent of their inverse. Use print formatting to exactly match the following output:
```python
1/1  = 1.0
1/2  = 0.5
1/3  = 0.333
1/4  = 0.25
1/5  = 0.2
1/6  = 0.167
1/7  = 0.143
1/8  = 0.125
1/9  = 0.111
1/10 = 0.1
1/11 = 0.0909
1/12 = 0.0833
1/13 = 0.0769
1/14 = 0.0714
1/15 = 0.0667
1/16 = 0.0625
1/17 = 0.0588
1/18 = 0.0556
1/19 = 0.0526
1/20 = 0.05
```
```python
for x in range(1,21):
    print("1/{:<2} = {:.4}".format(x, 1/x))
```
3. (3 pts) Write a recursive function that will calculate the Fibonacci series, and use output formatting. Your result should look like:
```python
1 -          1
 2 -          1
 3 -          2
 4 -          3
 5 -          5
 6 -          8
 7 -         13
 8 -         21
 9 -         34
10 -         55
11 -         89
12 -        144
13 -        233
14 -        377
15 -        610
16 -        987
17 -      1,597
18 -      2,584
19 -      4,181
20 -      6,765
21 -     10,946
22 -     17,711
23 -     28,657
24 -     46,368
25 -     75,025
26 -    121,393
27 -    196,418
28 -    317,811
29 -    514,229
30 -    832,040
31 -  1,346,269
32 -  2,178,309
33 -  3,524,578
34 -  5,702,887
35 -  9,227,465
```
```python
def f(n):
    if n > 2:
        return f(n-1)+f(n-2)
    elif n == 2 or n == 1:
        return 1
for x in range(1,36):
    print("{:2} - {:9,}".format(x, f(x)))
```
4. (1 pt) Why does the problem above run so slow? How could it be made to run faster? Ask if you aren't sure.
```python
# because is recalling itself over and over again 
def f(n):
    fn1 = 0
    fn2 = 1
    for x in range(1,n):
        n = fn1 + fn2
        fn1 = fn2
        fn2 = n
    return n
for x in range(1,36):
    print("{:2} - {:9,}".format(x, f(x)))
```