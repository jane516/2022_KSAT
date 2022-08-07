from sympy import *
from fractions import Fraction
dic = {(1, 2): Fraction(5, 4)}


def IntegrateF(a, b):
    global dic
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


print(IntegrateAllF(1, 4))
print(IntegrateAllF(1, 8))