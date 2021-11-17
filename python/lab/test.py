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