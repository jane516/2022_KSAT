from sympy import *

x, k = symbols('x k')
fx = x ** 3 + x ** 2
gx = - x ** 2 + k
S = integrate(fx - gx, (x, 0, 2))
print(solve(S, k)[0])