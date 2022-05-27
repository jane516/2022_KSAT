import sys

from sympy import *
from fractions import Fraction
dic = {(1, 2): Fraction(5, 4)}


def IntegrateF(a, b):
    if (a, b) in dic:
        return dic[(a, b)]
    k = a * b + a**2
    c, d = a // 2, b // 2
    if (c, d) in dic:
        dic[(a, b)] = k - 4 * IntegrateF(c, d)
        return dic[(a, b)]
    return k - 4 * IntegrateF(c, d)


dic2 = {(1, 2): Fraction(5, 4)}


def IntegrateAllF(a, b):
    if (a, b) in dic:
        dic2[(a, b)] = IntegrateF(a, b)
        return dic2[(a, b)]
    else:
        c = b // 2
        dic2[(a, b)] = IntegrateAllF(a, c) + IntegrateF(c, b)
        return dic2[a, b]


x = symbols('x')
f = {1: 1}
g = {}
k = 0

while 2**k <= 8:
    a = 2 * f[2 ** k]
    g[2 ** k] = a
    k += 1
    f[2 ** k] = a


a, b = map(int, sys.stdin.readline().strip().split())
A = b * f[b] - a * f[a]
B = IntegrateAllF(a, b)
분수 = Fraction(A - B)
p = 분수.denominator   # 분모
q = 분수.numerator   # 분자
print(p + q)



