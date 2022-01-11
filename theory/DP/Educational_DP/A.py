n = int(input())
h = list(map(int, input().split()))
INF = 10 ** 5

#配列DPを定義
dp = [INF] * n
#print(dp)

#初期条件
dp[0] = 0
#print(dp)

#ループ
for i in range(1, n):
    if i == 1:
        dp[i] = abs(h[i] - h[i - 1])
    else:
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

#print(dp)
print(dp[-1])
