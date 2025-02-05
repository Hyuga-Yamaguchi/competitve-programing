import numpy as np

n = int(input())
a = [None] * n; b = [None] * n
for i in range(n):
    A, B  = map(int, input().split())
    a[i] = A; b[i] = B

u = [0] * (10 ** 6 + 2)
for i in range(n):
    u[a[i]] += 1
    u[b[i] + 1] -= 1
lis = np.cumsum(u)
print(max(lis))
