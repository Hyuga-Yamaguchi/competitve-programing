"""配るDPで記載
"""

n = int(input())
h = list(map(int, input().split()))
INF = 2 ** 60

def chmin(a, b):
    if a > b:
        a = b
    return a

dp = [INF] * n
dp[0] = 0

for i in range(n):
    if i + 1 < n:
        dp[i + 1] = chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    if i + 2 < n:
        dp[i + 2] = chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))
print(dp[-1])
