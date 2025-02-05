"""部分和問題"""
"""
n個の正の整数 a[0],a[1],…,a[n−1]と正の整数 Aが与えられる。
これらの整数から何個かの整数を選んで総和が Aになるようにすることが可能か判定せよ。
可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。

【制約】
・1≤n≤100
・1≤a[i]≤1000
・1≤A≤10000
"""
n, A = map(int, input().split())
a = list(map(int, input().split()))

COUNT = 10 ** 6

dp = [[False] * (COUNT) for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(COUNT):
        if j < a[i]:
            dp[i + 1][j] = dp[i][j]
        if j >= a[i]:
            if dp[i][j - a[i]] or dp[i][j]:
                dp[i + 1][j] = True
#print(dp)
if dp[n][A]:
    print("Yes")
else:
    print("No")
