n, m = map(int, input().split())
d = [None] * n
for i in range(n):
    d[i] = int(input())
c = [None] * m
for i in range(m):
    c[i] = int(input())

INF = 10 ** 9
dp = [[INF] * (n + 1) for _ in range(m)]
dp[0][0] = 0
dp[0][1] = d[0] * c[0]

for i in range(1, m):
    for j in range(n + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + d[j - 1] * c[i], dp[i - 1][j])
print(dp[m - 1][n])
