a_list = [0 for _ in range(21)]
S = 17
a_list[1], a_list[2] = S - 9, 9
for i in range(1, 10):
    a1 = a_list[2 * i] + 2 * (2 * i) - 1
    a2 = a_list[2 * i] - 2 * (2 * i) + 1
    b1 = S - a1
    b2 = S - a2
    if abs(a1 - b1) == 2 * (2 * i + 1) - 1:
        a_list[2 * i + 1] = a1
        a_list[2 * i + 2] = b1
    else:
        a_list[2 * i + 1] = a2
        a_list[2 * i + 2] = b2

Sum = 0
for i in range(1, 11):
    Sum += a_list[2 * i]
print(Sum)