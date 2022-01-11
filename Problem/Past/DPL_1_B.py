N, W = map(int, input().split())
vw = list(list(map(int, input().split())) for _ in range(N))
value, weight = [], []
for i in range(N):
    value.append(vw[i][0])
    weight.append(vw[i][1])

dp = [[0] * (W + 1) for i in range(N + 1)]

for i in range(N):
    for w in range(W + 1):
        #品物を選ぶ場合
        if w - weight[i] >= 0:
            dp[i + 1][w] = max(dp[i][w], dp[i][w - weight[i]] + value[i])
        #品物を選ばない場合
        else:
            dp[i + 1][w] = max(dp[i][w], dp[i][w])
#print(dp)
print(dp[N][W])
