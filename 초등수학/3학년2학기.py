import random
x, y = 1, 1
while True:
    if x % y != 0:
        break
    x = random.randrange(50, 100)
    y = random.randrange(6, 15)
print(f'지우개 {x}개가 있습니다. '
      f'이 지우개를 한 명에게 {y}개씩 나누어 준다면 '
      f'몇 명에게 나누어 줄 수 있고, 몇 개가 남습니까?')

result1, result2 = x // y, x % y

print(f'{result1}명, {result2}개')