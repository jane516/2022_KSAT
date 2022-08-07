a = [0 for _ in range(9)]
a[1] = 1
for i in range(2, 9):
    if a[i - 1] < 7:
        a[i] = 2 * a[i - 1]
    else:
        a[i] = a[i - 1] - 7
print(sum(a))