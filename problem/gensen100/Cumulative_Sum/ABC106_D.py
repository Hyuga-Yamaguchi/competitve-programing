import numpy as np

n, m, Q = map(int, input().split())
l = [None] * m; r = [None] * m
for i in range(m):
     L, R = map(int, input().split())
     l[i] = L; r[i] = R
p = [None] * Q; q = [None] * Q
for i in range(Q):
    P, QQ = map(int, input().split())
    p[i] = P; q[i] = QQ

lis = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    lis[l[i]][r[i]] += 1
#print(lis)

u = np.cumsum(np.cumsum(lis, axis = 1), axis = 0)
#print(u)

for i in range(Q):
    ans = u[q[i]][q[i]] - u[q[i]][p[i] - 1] - u[p[i] - 1][q[i]] + u[p[i] - 1][p[i] - 1]
    print(ans)
