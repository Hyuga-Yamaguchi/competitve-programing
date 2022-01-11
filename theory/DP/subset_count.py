"""部分和数え上げ問題"""

n, w = map(int, input().split())
a = list(map(int, input().split()))

MOD = 10 ** 9 + 7

dp = [[0] * 10010 for _ in range(110)]

dp[0][0] = 1

for i in range(n):
    for j in range(w + 1):
        if j >= a[i]:
            dp[i + 1][j] = dp[i][j - a[i]] + dp[i][j] % MOD
        else:
            dp[i + 1][j] = dp[i][j] % MOD
print(dp[n][w])
