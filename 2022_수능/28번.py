from sympy import *
x, y = symbols('x y')
fx = 6 * pi * (x - 1)**2
dfx = diff(fx, x)
sol1 = solve(dfx)
f0 = fx.subs(x, 0)
f2 = fx.subs(x, 2)
fm = fx.subs(x, sol1[0])
M, m = max(f0, f2, fm), min(f0, f2, fm)
gy = 3 * y + 4 * cos(y)
dgy = diff(gy, y)
ddgy = diff(dgy, y)
sol2 = solve(dgy)
result = []
for i in sol2:
    if ddgy.subs(y, i) > 0:
        result.append(i)

