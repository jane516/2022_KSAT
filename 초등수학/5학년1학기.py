import random
x = random.randrange(11, 50)
y = random.randrange(200, 500, 100)
print(f'{x}의 배수 중에서 {y}에 가장 가까운 수를 구하시오.')
result = min(x * (y // x), x * (y // x + 1))
print(result)
