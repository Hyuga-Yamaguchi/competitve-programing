"""部分和数え上げ問題(選べる個数がk個以内)"""

n, w, k = map(int, input().split())
a = list(map(int, input().split()))

INF = 10 ** 8

dp = [[INF] * 15 for _ in range(10)]

dp [0][0] = 0

for i in range(n):
    for j in range(w + 1):
        if j >= a[i]:
            dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

if dp[n][w] <= k:
    print("Yes")
else:
    print("No")
