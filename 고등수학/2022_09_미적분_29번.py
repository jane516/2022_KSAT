from sympy import *

x, s, t = symbols('x s t')
fx = exp(x) + x
fx_prime = diff(fx, x)

kx = fx_prime * fx / (t - x)
t = solve(kx - 1, t)[0]
t_prime = diff(t, x)
gx_prime = diff(fx, x) / t_prime
a = solve(fx - 1, x)[0]

print(1 / gx_prime.subs(x, a))