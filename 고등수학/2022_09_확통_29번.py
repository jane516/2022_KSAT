from fractions import Fraction

my_list = []


def factorial(n):
    result = 1
    for i in range(n):
        result *= (n - i)
    return result


for i in range(1, 4):
    for j in range(i, 7):
        for k in range(j, 7):
            for l in range(k, 7):
                if i + j + k + l == 11:
                    my_list.append([i, j, k, l])

result = Fraction(1, pow(6, 4))
Sum = 0

for arr in my_list:
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in arr:
        if dic[i]:
            dic[i] += 1
        else:
            dic[i] = 1
    분자 = factorial(4)
    분모 = 1
    for j in dic:
        분모 *= factorial(dic[j])
    Sum += 분자 // 분모
ans = result * Sum

print(ans.numerator + ans.denominator)