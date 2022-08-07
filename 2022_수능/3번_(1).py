from sympy import *
a, d = symbols('a d')
a2 = a + d
a4 = a + 3 * d
a6 = a + 5 * d
a10 = a + 9 * d
equation1 = a2 - 6
equation2 = a4 + a6 - 36
result = solve((equation1, equation2))
X = a10.subs([(a, result[a]), (d, result[d])])
print(X)