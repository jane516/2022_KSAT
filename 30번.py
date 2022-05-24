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


x = symbols('x')
f = {1: 1}
g = {}
k = 0

while 2**k <= 8:
    a = 2 * f[2 ** k]
    g[2 ** k] = a
    k += 1
    f[2 ** k] = a


a, b = 1, 8
A = b * f[b] - a * f[a]
B = IntegrateF(1, 2) + IntegrateF(2, 4) + IntegrateF(4, 8)
k = Fraction(A - B)
p = k.denominator
q = k.numerator
print(p + q)



