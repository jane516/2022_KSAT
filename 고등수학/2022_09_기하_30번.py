from fractions import Fraction

import sympy

R = 2 * Fraction(1, 2) * sympy.sqrt(3) * 2

ans = 2 * R * Fraction(21, 36) * 2 * sympy.sqrt(3) * Fraction(1, 3)

p, q = ans.denominator, ans.numerator
print(p + q)
