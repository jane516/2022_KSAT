from sympy import *
from fractions import Fraction
x = symbols('x')
fx1 = (Fraction(2, 3))**(x+1) + Fraction(8, 3)
fx2 = (Fraction(2, 3))**(x+3) + 1
y, k = 0, 0
가로, 세로 = 1, 2
equation1 = fx2 + 세로
equation2 = fx1.subs(x, x + 가로)
result = solve(equation1 - equation2)
a = int(result[0])
y = Fraction(2, 3)**(a+3) + 1
k = y - 2 * a
print(k)
