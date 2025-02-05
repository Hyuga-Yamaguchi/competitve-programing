"""
K個以内部分和問題
"""
"""
n個の正の整数 a[0],a[1],…,a[n−1]と正の整数Aが与えられる。
これらの整数からK個以内の整数を選んで総和がAになるようにすることが可能か判定せよ。
可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。

【制約】
・1≤K≤n≤500
・1≤a[i]≤1000
・1≤A≤10000
"""
n, A, k = map(int, input().split())
a = list(map(int, input().split()))
COUNT = A + 1
INF = 10 ** 9
dp = [[INF] * (COUNT) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(COUNT):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        if j >= a[i]:
            dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
#print(dp)
if dp[n][A] <= k:
    print("Yes")
else:
    print("No")
