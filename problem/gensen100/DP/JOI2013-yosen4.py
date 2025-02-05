d, n = map(int, input().split())
t = list(int(input()) for _ in range(d))
a, b, c = [None] * n, [None] * n, [None] * n
for i in range(n):
    A, B, C = map(int, input().split())
    a[i] = A; b[i] = B; c[i] = C

dp = [[-1] * n for _ in range(d)]
for i in range(n):
    if a[i] <= t[0] <= b[i]:
        dp[0][i] = c[i]
#print(dp)

for i in range(d - 1):
    for j in range(n):
        if dp[i][j] >= 0:
            if i == 0:
                for k in range(n):
                    if a[k] <= t[i + 1] <= b[k]:
                        dp[i + 1][k] = max(dp[i + 1][k], abs(c[k] - c[j]))
            else:
                for k in range(n):
                    if a[k] <= t[i + 1] <= b[k]:
                        dp[i + 1][k] = max(dp[i + 1][k], abs(c[k] - c[j]) + dp[i][j])
print(max(dp[d - 1]))
