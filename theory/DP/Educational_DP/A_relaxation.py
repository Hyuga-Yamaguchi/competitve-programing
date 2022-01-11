"""緩和を意識したDP
"""

n = int(input())
h = list(map(int, input().split()))
INF = 2 ** 60

#choose minimum関数を設定
#小さい方の値に更新する
def chmin(a, b):
    if a > b:
        a = b
    return a #pythonの場合は参照渡しができないので、aをreturnし、結果のタプルを返す

dp = [INF] * n

dp[0] = 0

for i in range(1, n):
    dp[i] = chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    if i > 1:
        dp[i] = chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))
    print(dp)

print(dp[-1])
