from sympy import *

x, a, p, q = symbols('x a p q')

x1 = 3 * a - (2 * a + 2)
a = solve(2 * a - 3 * a - x1)[0]

fx = x ** 2 + p * x + q
fx_prime = diff(fx, x)

gx = ln(fx + fx_prime + 1)

equation1 = gx.subs(x, 3 - x) - gx.subs(x, 3 + x)
equation2 = gx.subs(x, 4) - ln(5)

sol = solve((equation1, equation2), dict=True)

fx = fx.subs(p, sol[0][p])
fx = fx.subs(q, sol[0][q])
fx_prime = diff(fx, x)
gx = ln(fx + fx_prime + 1)

result = expand_log(integrate((fx_prime + 2 * a) * gx, (x, 3, 5)))
m, nlog = result.args
n, log = nlog.args

print(m + n)