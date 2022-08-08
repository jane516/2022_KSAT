from sympy import *

x, a, b, c = symbols('x a b c')
fx = a * x * (x - b) * (x - c)
fx_1 = x * (x - b) * (x - c)
diff_fx = diff(fx, x)
diff_fx_1 = diff(fx_1, x)
gx = diff_fx.subs(x, 0) * x
gx_1 = diff_fx_1.subs(x, 0) * x

sol1 = solve(fx_1.subs(x, 12) - gx_1.subs(x, 12))
fx_1 = fx_1.subs(b, sol1[0][b])
diff_fx_1 = diff_fx_1.subs(b, sol1[0][b])

sol2 = solve(fx_1 - diff_fx_1)
diff_fx_1 = simplify(diff_fx_1)
print(fx_1, diff_fx_1)
