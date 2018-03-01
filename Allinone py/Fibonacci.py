def fibo(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a
c = int(input("Enter Number : "))
for c in range(0, c):
    print(fibo(c))