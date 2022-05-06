from sympy import *
a, d = symbols('a d')    # a : 초항, d : 공차
N_list = list(map(int, input().split()))    # 어떤 a_n을 사용할 건지
a1 = a + N_list[0] * d
a2 = a + N_list[1] * d
a3 = a + N_list[2] * d
a4 = a + N_list[3] * d    # 내가 구할 값
value1, value2 = map(int, input().split())    # 사용할 a_n들의 값
equation1 = a1 - value1
equation2 = a2 + a3 - value2
result = solve((equation1, equation2))    # 초항과 공차
X = a4.subs([(a, result[a]), (d, result[d])])
print(X)