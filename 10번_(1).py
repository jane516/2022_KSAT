from sympy import *

x = symbols('x')
a, b, c, d = symbols('a b c d')

fx = a * x**3 + b * x**2 + c * x + d
equation1 = fx.subs(x, 0)
d1 = solve(equation1)

fx = a * x**3 + b * x**2 + c * x + d1[0]
dfx = diff(fx, x)
l1 = dfx.subs(x, 0) * x + fx.subs(x, 0)
equation2 = l1.subs(x, 1) - 2
c1 = solve(equation2)

fx = a * x**3 + b * x**2 + c1[0] * x + d1[0]
dfx = diff(fx, x)
equation3 = dfx.subs(x, 1)
equation4 = fx.subs(x, 1) - 2
result = solve((equation3, equation4))

fx = result[a] * x**3 + result[b] * x**2 + c1[0] * x + d1[0]
dfx = diff(fx, x)
print(dfx.subs(x, 2))


