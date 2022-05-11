import random


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


nums = list(set())
while len(nums) != 2:
    X = random.randrange(10, 30, 5)
    if X != 25:
        nums.append(X)

d = random.randrange(20, 50, 10)
x, y = nums[0], nums[1]
z1, z2 = int(x * d // 60), int(y * d // 60)
l1 = d - random.randrange(2, z1, 1)
l2 = d - random.randrange(2, z2, 1)
분모 = 6
분자1 = random.randrange(1, 분모 - 1, 1)
분자2 = random.randrange(1, 분모 - 1, 1)
분모1, 분자1 = 분모 // gcd(분모, 분자1), 분자1 // gcd(분모, 분자1)
분모2, 분자2 = 분모 // gcd(분모, 분자2), 분자2 // gcd(분모, 분자2)

print(f'길이가 {d}cm 인 빨간 양초와 노란 양초가 있다. '
      f'두 양초에 불을 붙이고 {x}분 후에 빨간 양초의 길이를 재었더니 '
      f'{l1} {분자1}/{분모1}cm 였고, {y}분 후에 노란 양초의 길이를 재었더니 '
      f'{l2} {분자2}/{분모2}cm 였다. 두 양초에 불을 붙인 지 1시간이 되었을 때 '
      f'어떤 양초의 길이가 얼마나 더 짧은지 구하시오.')
