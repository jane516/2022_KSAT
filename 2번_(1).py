from sympy import *
x = symbols('x')
fx = x**3 + 3*x**2 + x - 1
dfx = diff(fx, x)
result = dfx.subs(x, 1)
print(result)