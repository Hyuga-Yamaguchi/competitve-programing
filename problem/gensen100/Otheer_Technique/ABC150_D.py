from math import gcd
import copy
n, m = map(int, input().split())
a = list(map(int, input().split()))

def lcm(a, b):
    return a // gcd(a, b) * b

lis = [None] * n
for i in range(n):
    b = copy.copy(a[i])
    cnt = 0
    while b % 2 == 0:
        b = b // 2
        cnt += 1
    lis[i] = cnt
#print(lis)

c = a[0]
for i in range(n):
    c = lcm(c, a[i])
#print(c)

if len(set(lis)) == 1:
    print((2 * m // c + 1) // 2)
else:
    print(0)
