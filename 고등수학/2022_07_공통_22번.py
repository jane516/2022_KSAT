from sympy import *
from fractions import Fraction

x, a, b, c = symbols('x a b c')
fx = x * (x - b) * (x - c)
diff_fx = diff(fx, x)
gx = diff_fx.subs(x, 0) * x

sol1 = solve(fx.subs(x, 12) - gx.subs(x, 12))
fx = fx.subs(b, sol1[0][b])
gx = gx.subs(b, sol1[0][b])
diff_fx = diff(fx, x)
diff_gx = diff(gx, x)

kx = (fx + gx) / x - diff_fx - diff_gx
k = solve(kx)[0][x]
sol3 = solve((diff_fx + diff_gx).subs(x, k))
fx = a * fx.subs(c, sol3[1])
gx = a * gx.subs(c, sol3[1])
hx_1 = fx + gx
hx_2 = fx - gx
sol4 = solve(hx_1.subs(x, 3) + Fraction(9, 2))
fx = fx.subs(a, sol4[0])
gx = gx.subs(a, sol4[0])
hx = []
for i in [6, 11]:
    if fx.subs(x, i) < 0:
        hx.append(- 1 * fx.subs(x, i) + gx.subs(x, i))
    else:
        hx.append(fx.subs(x, i) + gx.subs(x, i))
result = k * (hx[0] - hx[1])
print(simplify(result))