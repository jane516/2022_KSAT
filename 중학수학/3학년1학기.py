from sympy import *
import random


while True:
    num_list = [random.randrange(-9, 10) for _ in range(4)]
    D = (num_list[3] + num_list[2])**2 - 4 * num_list[0] * num_list[1]
    if D > 0:
        a = random.randrange(2, 10)
        b, c, d, e = [i for i in num_list]
        x = symbols('x')
        fx = a * (x + b) * (x + c)
        fx = expand(fx)
        gx = a * (x + d) * (x + e)
        gx = expand(gx)

        hx = a * x ** 2 + gx.coeff(x) * x + fx.subs(x, 0)
        hx = factor(hx)
        print(factor(fx))
        print(factor(gx))
        print(hx)
        break
    else:
        continue