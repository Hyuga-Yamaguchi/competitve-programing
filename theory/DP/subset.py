"""部分和問題(DP)"""

n, w = map(int, input().split())
a = list(map(int, input().split()))

#i個目まで選んだときの和の総和がj

dp = [[False] * (w + 1) for _ in range(n + 1)]

dp[0][0] = True

for i in range(n):
    for j in range(w + 1):
        if dp[i][j] == True:
            dp[i + 1][j] = True
        if j >= a[i]:
            if dp[i][j - a[i]] == True:
                dp[i + 1][j] = True
print(dp[n][w])
