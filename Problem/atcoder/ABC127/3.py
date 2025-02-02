import numpy as np

n, m = map(int, input().split())
l = [None] * m; r = [None] * m
for i in range(m):
    L, R = map(int, input().split())
    l[i] = L - 1; r[i] = R - 1

u = [0] * (n + 1)
for i in range(m):
    u[l[i]] += 1
    u[r[i] + 1] -= 1
new_u = np.cumsum(u)
#print(new_u)
ans = 0
for i in range(n + 1):
    if new_u[i] == m:
        ans += 1
print(ans)
