from sympy import *
from fractions import Fraction

x, a, b, gx = symbols('x a b gx')

fx = x ** 3 + a * x ** 2 + b * x - 3
fx_prime = diff(fx, x)
f_1 = fx.subs(x, 1)

fx_prime_gx1 = cancel((fx - f_1) / (x - 1))
fx_prime_gx2 = fx_prime.subs(x, gx)

gx = solve(fx_prime_gx1 - fx_prime_gx2, gx)[1]

x1 = solve(gx.diff(x), x)[0]
a1 = solve(gx.subs(x, x1) - Fraction(5, 2))[0]

gx = gx.subs(a, a1)
fx = fx.subs(a, a1)

g_1 = gx.subs(x, 1)
b1 = solve(fx.subs(x, g_1) - 6, b)[0]

fx = fx.subs(b, b1)

print(fx.subs(x, 4))