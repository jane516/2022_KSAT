n = int(input())     # 몇 항까지 구할지
a = [0 for _ in range(n + 1)]
a[1] = int(input())     # 초항 뭐로 할지
k, p, q = map(int, input().split())     # 범위, 계수, 상수항
for i in range(2, n + 1):
    if a[i - 1] < k:
        a[i] = p * a[i - 1]
    else:
        a[i] = a[i - 1] - q
print(sum(a))