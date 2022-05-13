from sympy import *
from fractions import Fraction
x = symbols('x')
기울기 = int(input())     # 직선의 기울기
p, q = map(int, input().split())     # 함수식 분자, 분모
c1p, c1q, c2p, c2q = map(int, input().split())     # 함수식 1, 2의 y축 평행 이동 분자, 분모
dx1, dx2 = map(int, input().split())     # 함수식 1, 2의 x축 평행 이동
fx1 = (Fraction(p, q))**(x+dx1) + Fraction(c1p, c1q)     # 함수식1
fx2 = (Fraction(p, q))**(x+dx2) + Fraction(c2p, c2q)     # 함수식2
y, k = 0, 0     # y, 직선의 방정식 y절편
가로, 세로 = map(int, input().split())     # 선분 PQ의 길이 = sqrt(가로**2 + 세로**2)
equation1 = fx1 + 세로
equation2 = fx2.subs(x, x + 가로)
result = solve(equation1 - equation2)     # 점 P를 평행 이동 - 점 Q = 0
a = int(result[0])
y = Fraction(p, q)**(a+dx1) + Fraction(c1p, c1q)     # 점 P를 함수식2에 대입
k = y - 기울기 * a     # 구하는 값
print(k)