n ,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int ,input().split()))

#DPテーブルの設定
INF = 2 ** 32

la = len(a); lb = len(b)

dp = [[INF] * (lb + 1) for i in range(la + 1)]
dp[0][0] = 0

#DP操作
for i in range(la + 1):
    for j in range(lb + 1):
        #変更操作
        if i > 0 and j > 0:
            if a[i - 1] == b[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        #削除操作
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        #挿入操作
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
#print(dp)
print(dp[la][lb])
