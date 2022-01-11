n, w = map(int, input().split())
value, weight = [], []
for i in range(n):
    a, b = map(int, input().split())
    value.append(a); weight.append(b)

dp = [[0] * (w + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(w + 1):
        if j < weight[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            #同じのを何度も使っていい時は、dp[i + 1][j] = dp[i + 1][j - w[i]] ・・・　とする
            dp[i + 1][j] = max(dp[i + 1][j - weight[i]] + value[i], dp[i][j])
#print(dp)
print(dp[n][w])
