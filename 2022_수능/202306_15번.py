from fractions import Fraction


def 수열(a, k):
    if a <= 0:
        return a + Fraction(1, k + 1)
    else:
        return a - Fraction(1, k)


Sum = 0
k = 1
while k < 23:
    a = 0
    for start in range(21):
        a = 수열(a, k)
    if a == 0:
        Sum += k
    k += 1
print(Sum)
