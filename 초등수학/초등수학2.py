import random
a = round(random.uniform(0, 1), 2)
b = random.randrange(100, 1000, 100)
result = int(a * b)
print(f'어느 프로야구 선수의 타율이 {a}일 때,'
      f' 이 선수는 {b}타수 중에서 안타를 {result}개 쳤다.')