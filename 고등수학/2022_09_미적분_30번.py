from sympy import *

x = symbols('x')
fx_prime = 4 * pow(x, 2) * (x + 3)
fx = integrate(fx_prime)

t = fx - fx.subs(x, 0)
ans = integrate(fx_prime/pow(t, 2), (x, 1, 2))
print(ans.numerator + ans.denominator)