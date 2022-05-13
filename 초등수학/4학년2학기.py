import random

빨간끈 = random.randrange(10, 80)
노란끈 = random.randrange(15, 60)

Sum = 빨간끈 + 노란끈

print(f'희찬이는 선물을 포장하는 데 빨간 끈 {빨간끈}cm와 '
      f'노란 끈 {노란끈}cm를 사용했습니다. '
      f'희찬이가 사용한 끈은 모두 몇 m인지 소수로 나타내시오.')

result = Sum / 100

print(result)
