n, k = map(int, input().split())
a, b = [], []
for i in range(k):
    A, B = map(int, input().split())
    a.append(A - 1); b.append(B - 1)
day = [-1] * n
for i in range(k):
    day[a[i]] = b[i]
#print(day)

dp = [[[0] * 3 for _ in range(3)] for _ in range(n)]

#dp初期化
if day[0] >= 0:
    for i in range(3):
        dp[0][day[0]][0] = 1
else:
    for i in range(3):
        dp[0][i][0] = 1
#print(dp)

#dp更新
for i in range(n - 1):
    for j in range(3):
        for k in range(3):
            if day[i + 1] >= 0:
                if dp[i][j][k] > 0:
                    if i == 0:
                        dp[i + 1][day[i + 1]][j] += dp[i][j][k]
                    else:
                        if not j == k == day[i + 1]:
                            dp[i + 1][day[i + 1]][j] += dp[i][j][k]
            else:
                if dp[i][j][k] > 0:
                    for l in range(3):
                        if i == 0:
                            dp[i + 1][l][j] += dp[i][j][k]
                        else:
                            if not j == k == l:
                                dp[i + 1][l][j] += dp[i][j][k]

#print(dp)
ans = 0
for i in range(3):
    for j in range(3):
        ans += dp[n - 1][i][j]
print(ans % 10000)
