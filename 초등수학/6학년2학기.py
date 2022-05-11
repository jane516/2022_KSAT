import random
nums1 = list(set())
nums2 = list(set())
while len(nums1) != 2:
    nums1.append(random.randrange(1, 15))
while len(nums2) != 2:
    nums2.append(random.randrange(1, 15))
nums1.sort()
nums2.sort()


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


S분자 = nums1[0] * nums2[0]
S분모 = nums1[1] * nums2[1]
가로분자 = nums1[0] // gcd(nums1[0], nums1[1])
가로분모 = nums1[1] // gcd(nums1[0], nums1[1])
S분자, S분모 = S분자 // gcd(S분자, S분모), S분모 // gcd(S분자, S분모)

print(f'넓이가 {S분자}/{S분모} m^2인 직사각형의 가로의 길이가 {가로분자}/{가로분모}m라면, '
      f'세로의 길이는 몇 m입니까?')
print(f'{nums2[0] // gcd(nums2[0], nums2[1])}/{nums2[1] // gcd(nums2[0], nums2[1])}')