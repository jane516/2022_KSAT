from sympy import *
x, a, b = symbols('x a b')
fx = x
gx = x * fx + a * x + b
dfx = diff(fx, x)
dgx = diff(gx, x)
a = solve(dfx.subs(x, 1) - dgx.subs(x, 0))
b = solve(fx.subs(x, 1) - gx.subs(x, 0))
gx = x * fx + a[0] * x + b[0]
result = integrate(gx, (x, 0, 1))
print(60 * result)