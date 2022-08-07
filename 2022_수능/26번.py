from sympy import *
x = symbols('x')
fx = (x**2 + 2 * x) / (x**3 + 3 * x**2 + 1)
result = integrate(fx, (x, 0, 1))
print(result)