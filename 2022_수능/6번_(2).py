from sympy import *
x = symbols('x')
a, b, c = map(int, input().split())     # 삼차식 계수
fx = a * x**3 + b * x**2 + c * x
dfx = diff(fx, x)     # 미분 하기
value = solve(dfx)     # 극댓값, 극솟값 찾기
Max = fx.subs(x, value[0])     # 극댓값
Min = fx.subs(x, value[1])     # 극솟값
print(Max - Min - 1)