"""部分和数え上げ問題"""


n = int(input())
p = list(map(int, input().split()))

#print(p)

INF = 10000

dp = [[0] * (INF + 1) for _ in range(n + 1)]

dp[0][0] = 1

for i in range(n):
    for j in range(INF + 1):
        #整数a[i]を選ばない場合
        if j < p[i]:
            dp[i + 1][j] = dp[i][j]
        #整数a[i]を選ぶ場合
        else:
            dp[i + 1][j] = dp[i][j - p[i]] + dp[i][j]

#print(dp)

cnt = 0
for i in range(INF + 1):
    if dp[n][i] > 0:
        cnt += 1
print(cnt)
