import random
x = random.randrange(6, 15)
y = random.randrange(4, 20)


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


print(f'어떤 자연수를 {x}(으)로 나누어야 할 것을 잘못하여 {x}을/룰 곱했더니 '
      f'{x * y}이/가 되었다. 바르게 계산 값을 분수로 나타내시오.')

분자, 분모 = y // gcd(x, y), x // gcd(x, y)

print(f'{분자}/{분모}')
