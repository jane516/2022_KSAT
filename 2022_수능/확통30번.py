from fractions import Fraction
my_list = []
for i in range(6):
    if i + 2 * (5 - i) >= 7:
        my_list.append((i, 5 - i))


def Combination(n, r):
    if n-r < r:
        r = n - r
    분자 = 분모 = 1
    for i in range(0, r):
        분자 = 분자 * (n - i)
        분모 = 분모 * (r - i)
    return 분자 // 분모


All, Part = 0, 0
for i in range(len(my_list)):
    a, b = my_list[i][0], my_list[i][1]
    All += 2 ** a * Combination(5, a)
    if a >= 2:
        Part += 2 ** a * 3 * Combination(2, a - 2)


확률 = Fraction(Part, All)
p = 확률.denominator
q = 확률.numerator
print(p + q)