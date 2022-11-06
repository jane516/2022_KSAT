from sympy import *

x, k = symbols('x k')
fx_prime = 4 * x * (x - 4) * (x - k)
fx = integrate(fx_prime, x)
K = solve(fx.subs(x, 0) - fx.subs(x, 2))
fx = fx.subs(k, K[0])
result1 = fx.subs(x, 0) - fx.subs(x, 4)
result2 = fx.subs(x, -1) - fx.subs(x, 4)
print(result1 + result2)