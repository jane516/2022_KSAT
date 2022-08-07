import random
from sympy import *

while True:
    이익 = [random.randrange(21, 31) for _ in range(2)]
    a, b = 5 * max(이익), 5 * min(이익)
    c = 50 * random.randrange(1, 21)
    if (100 * c) / (a - b) == (100 * c) // (a - b):
        x = symbols('x')
        f1 = x * Rational(a, 100) - c
        f2 = x * Rational(b, 100)
        x = solve(f1 - f2)
        print(f'어떤 상품을 원가에 {a - 100}%의 이익을 붙여서 정가를 정하고, '
              f'정가에서 {c}원을 할인하여 판매하였더니 1개를 팔 때마다 '
              f'원가의 {b - 100}%의 이익을 얻었다. '
              f'이 상품의 원가를 k원이라 할 때, k의 값을 구하시오.')
        print(x[0])
        break
    else:
        continue