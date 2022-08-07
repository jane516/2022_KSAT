from sympy import *
x = symbols('x')
a, b, c, d = map(int, input().split())    # 계수
fx = a * x**3 + b * x**2 + c * x + d    # 원함수
dfx = diff(fx, x)    # 미분한 함수
k = int(input())    # 대입할 값
result = dfx.subs(x, k)
print(result)