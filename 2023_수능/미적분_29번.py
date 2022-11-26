from sympy import *

x, a, b, c = symbols('x a b c')

b, c = 1, - 6

fx = a * exp(2 * x) + b * exp(x) + c

a1 = solve(fx.subs(x, log(2)))[0]

fx = fx.subs(a, a1)
fx_prime = diff(fx)

x1 = log(2)
x2 = solve(fx - 14)[1]

result = simplify(integrate(x * fx_prime, (x, x1, x2)))
result = expand(result)

p, qlog2 = result.args
q, log2 = qlog2.args

print(p + q)