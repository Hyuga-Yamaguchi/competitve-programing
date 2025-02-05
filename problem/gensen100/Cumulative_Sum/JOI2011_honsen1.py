import numpy as np
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())

s_j = [[0] * (n + 1) for _ in range(m + 1)]
s_o = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    S = input()
    for j in range(n):
        if S[j] == "J":
            s_j[i + 1][j + 1] = 1
        elif S[j] == "O":
            s_o[i + 1][j + 1] = 1
#print(s_j)

a, b, c, d = [None] * k, [None] * k, [None] * k, [None] * k
for i in range(k):
    A, B, C, D = map(int, input().split())
    a[i] = A; b[i] = B; c[i] = C; d[i] = D
#print(a, b, c, d)

J = np.cumsum(np.cumsum(s_j, axis = 1), axis = 0)
O = np.cumsum(np.cumsum(s_o, axis = 1), axis = 0)
#print(J)

for i in range(k):
    ans_j = J[c[i]][d[i]] - J[a[i] - 1][d[i]] - J[c[i]][b[i] - 1] + J[a[i] - 1][b[i] - 1]
    ans_o = O[c[i]][d[i]] - O[a[i] - 1][d[i]] - O[c[i]][b[i] - 1] + O[a[i] - 1][b[i] - 1]
    ans_i = (d[i] - b[i] + 1) * (c[i] - a[i] + 1) - ans_j - ans_o
    print(ans_j, ans_o, ans_i)
