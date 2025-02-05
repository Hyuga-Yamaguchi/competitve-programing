"""部分和数え上げ問題"""
"""
n個の正の整数 a[0],a[1],…,a[n−1]と正の整数 Aが与えられる。
これらの整数から何個かの整数を選んで総和が Aになるようにする方法が何通りあるかを求めよ。
ただし、答えがとても大きくなる可能性があるので、1,000,000,009 で割った余りで出力せよ。

【制約】
・1≤n≤100
・1≤a[i]≤1000
・1≤A≤10000
"""

n, A = map(int, input().split())
a = list(map(int, input().split()))
COUNT = 20
dp = [[0] * (INF) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(COUNT):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        if j >= a[i]:
            dp[i + 1][j] = dp[i][j - a[i]] + dp[i][j]
print(dp)
print(dp[n][A])
