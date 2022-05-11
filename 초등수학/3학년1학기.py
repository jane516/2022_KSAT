import random
x = random.randrange(8, 20)
y = random.randrange(3, 8)
print(f'쌓기나무를 이용하여 상자 모양을 만들려고 합니다. '
      f'한 층을 만드는 데 쌓기나무가 {x}개씩 필요하다면 '
      f'{y}층짜리 상자 모양을 만드는 데 필요한 쌓기나무는 모두 몇 개입니까?')

result = x * y

print(result)