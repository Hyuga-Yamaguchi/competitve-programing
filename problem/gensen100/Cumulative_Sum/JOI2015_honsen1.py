import numpy as np

n, m = map(int, input().split())
p = list(map(int , input().split()))
for i in range(m):
    p[i] = p[i] - 1
a = [None] * (n - 1); b = [None] * (n - 1); c = [None] * (n - 1)
for i in range(n - 1):
    A, B, C = map(int, input().split())
    a[i] = A; b[i] = B; c[i] = C

u = [0] * (n)
for i in range(m - 1):
    max_p = max(p[i + 1], p[i])
    min_p = min(p[i + 1], p[i])
    u[max_p] -= 1
    u[min_p] += 1
#print(u)

v = np.cumsum(u)
#print(v)

ans = 0
for i in range(n - 1):
    ans += min(a[i] * v[i], b[i] * v[i] + c[i])
print(ans)
