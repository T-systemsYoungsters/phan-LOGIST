def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n>2:
        return f(n-1)+f(n-2)

for x in range(1,11):
    print(f(x))