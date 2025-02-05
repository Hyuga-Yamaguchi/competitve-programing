"""
最小個数部分和問題
"""
"""
問題 5:　最小個数部分和問題　
n個の正の整数 a[0],a[1],…,a[n−1]と正の整数Aが与えられる。
これらの整数から何個かの整数を選んで総和がAにする方法をすべて考えた時、
選ぶ整数の個数の最小値を求めよ。
Aにすることができない場合は -1 と出力せよ。

【制約】
・1≤n≤100
・1≤a[i]≤1000
・1≤A≤1000
"""

n, A = map(int, input().split())
a = list(map(int, input().split()))
COUNT = 20
INF = 10 ** 9
dp = [[INF] * (COUNT) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(COUNT):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        if j >= a[i]:
            dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
print(dp)
if dp[n][A] < INF:
    print(dp[n][A])
else:
    print(-1)
