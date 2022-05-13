import random

d = random.randrange(100, 500)
h = random.randrange(1, 9)

print(f'한 시간에 {d}m씩 가는 거북이 있습니다. '
      f'이 거북이 쉬지 않고 {10 * h}시간 동안 갈 수 있는 거리는 '
      f'모두 몇 km입니까?')

result = d * (10 * h)

print(result)