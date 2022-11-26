from sympy import *


def f(x):
    return pow(3, x + 2)


def g(x):
    return log(x + 4, 2)


min = g(0)
max = f(0)
Sum = 0

for i in range(min + 1, max):
    Sum += i

print(Sum)