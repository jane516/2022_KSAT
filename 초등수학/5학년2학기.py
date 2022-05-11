import random
x = round(random.uniform(0, 1), 2)


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


분자, 분모 = int(x * 100), 100
GCD = gcd(분모, 분자)

print('소수를 기약분수로 나타내시오.')
print(f'{x}')
print(f'{분자 // GCD}/{분모 // GCD}')