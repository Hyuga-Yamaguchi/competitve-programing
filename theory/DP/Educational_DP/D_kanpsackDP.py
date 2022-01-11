n, W = map(int, input().split())
wv = list(list(map(int, input().split())) for _ in range(n))

weight = []
value = []
for i in range(n):
    weight.append(wv[i][0])
    value.append(wv[i][1])

def chmax(a, b):
    if a < b:
        a = b
    return a

#DPテーブル定義
dp = [[0] * (W + 1) for _ in range(n + 1)]
#print(dp)

for i in range(n):
    for w in range(W + 1):
        #i番目の品物を選ぶとき
        if w - weight[i] >= 0:
            dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
        #i番目の品物を選ばない時
        dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])

print(dp[n][W])
