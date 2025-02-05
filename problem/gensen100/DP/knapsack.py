"""ナップザック問題"""
"""
n個の品物があり、i番目の品物のそれぞれ重さと価値がweight[i],value[i] となっている (i=0,1,...,n−1)。
これらの品物から重さの総和が W を超えないように選んだときの、価値の総和の最大値を求めよ。

【制約】
・1≤n≤100
・weight[i],value[i] は整数
・1≤weight[i],value[i]≤1000
・ 1≤W≤10000
"""

n, W = map(int, input().split())

weight, value = [], []
for i in range(n):
    a, b = map(int, input().split())
    weight.append(a)
    value.append(b)

dp = [[0] * (W + 1) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(n):
    for j in range(W + 1):
        if j < weight[i]: #品物iを選ばない
            dp[i + 1][j] = dp[i][j]
        if j >= weight[i]: #品物iを選ぶ場合と選ばない場合の大きい方をとる
            dp[i + 1][j] = max(dp[i][j - weight[i]] + value[i], dp[i][j])
#print(dp)
print(dp[n][W])
