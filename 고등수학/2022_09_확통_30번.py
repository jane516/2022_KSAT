import itertools


def comb(a, b):
    분모, 분자 = 1, 1
    for i in range(b):
        분모 *= (a - i)
    for j in range(b):
        분자 *= (b - j)
    return 분모 // 분자


S1 = comb(5, 2) * pow(2, 3)

list = [1, 2, 3]
cnt = 0
my_list = itertools.permutations(list, 3)
for i in my_list:
    check = 0
    for j in range(3):
        if list[j] == i[j]:
            check = 1
    if check == 0:
        cnt += 1

S2 = comb(5, 3) * cnt * pow(3, 2)
print(S1 + S2)