import sympy
from sympy import *
from fractions import Fraction

m, x, y = symbols('m x y')
f = m * x - y + sympy.sqrt(5) * m
g = f.subs([(x, 0), (y, 2)])

기울기 = solve(pow(g, 2) - pow(2 * sympy.sqrt(pow(m, 2) + 1), 2))

for i in 기울기:
    if i != 0:
        m = i

f = m * x - y + sympy.sqrt(5) * m

dist = Fraction(abs(f.subs([(x, 0), (y, -7)])), sympy.sqrt(pow(m, 2) + 1))
R = sympy.sqrt(pow(7, 2) - pow(dist, 2))
cos = Fraction(dist, 7)

ans = pow(R, 2) * cos

print(ans.denominator + ans.numerator)