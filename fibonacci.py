"""
Fibonacciho posloupnost
Implementujte funkci fibonacci(n), která vrátí n-tý prvek Fibonacciho posloupnosti.
fibonacci(5) = 3

0,1,1,2,3,5,8 ...
"""
from functools import reduce


def fibonacci(n):
    if n < 0:
        return None
    a, b = 0, 1
    for i in range(3,n+1):
        a, b = b, a+b
    return b

def fibonacci2(n):
    if n < 0:
        return None
    return reduce(lambda a, b: (a[1], a[0]+a[1]),range(1,n),(0,1))[0]

# print(fibonacci2(10))
