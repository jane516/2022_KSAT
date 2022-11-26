from sympy import *
from fractions import Fraction

x, a, b, c, d = symbols('x a b c d')

fx = a * pow(x, 3) + b * pow(x, 2) + c * x + d
gx = exp(sin(pi * x)) - 1

fx_prime = diff(fx, x)
gx_prime = diff(gx)

c1 = solve(fx_prime.subs(x, 0))[0]
fx = fx.subs(c, c1)

d1 = solve(fx.subs(x, 0) - 8)[0]
fx = fx.subs(d, d1)
fx_prime = diff(fx, x)

equation1 = fx.subs(x, 3) - Fraction(1, 2)
equation2 = fx_prime.subs(x, 3)

a1 = solve((equation1, equation2), dict=True)[0][a]
b1 = solve((equation1, equation2), dict=True)[0][b]

fx = fx.subs({a: a1, b: b1})

result = fx.subs(x, 2).denominator + fx.subs(x, 2).numerator

print(result)
