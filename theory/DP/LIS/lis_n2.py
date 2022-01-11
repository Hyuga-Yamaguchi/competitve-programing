a = [1, 3, 5, 2, 4, 6]
n = len(a)

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n - 1):
    for j in range(n):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if a[i + 1] > a[j]:
            dp[i + 1][i + 1] = max(dp[i + 1][i + 1], dp[i][j] + 1)
print(dp)
