from sympy import *

x, z, k = symbols('x z k')

B = (0, 0, 1)
C = (x, 1, z)

x = 1 * tan(pi / 3)
z = sqrt(sqrt(6) ** 2 - x ** 2 - 1)

C1 = (x, 1, z)
C2 = (x, 1, z + 1)
D = (k * x, k, k * z + 1)

Sum = 0
for i in range(3):
    Sum += D[i] ** 2

fk = Sum - 6
Sol = solve(fk)
k1, k2 = Sol[0], Sol[1]
D1 = (k1 * x, k1, k1 * z + 1)
D2 = (k2 * x, k2, k2 * z + 1)

result1, result2 = 0, 0
for i in range(3):
    result1 += (D1[i] - B[i]) ** 2
    result2 += (D2[i] - B[i]) ** 2
print(min(result1, result2))