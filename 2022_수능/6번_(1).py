from sympy import *
x = symbols('x')
fx = 2 * x**3 - 3 * x**2 - 12 * x
dfx = diff(fx, x)
value = solve(dfx)
Max = fx.subs(x, value[0])
Min = fx.subs(x, value[1])
print(Max - Min - 1)