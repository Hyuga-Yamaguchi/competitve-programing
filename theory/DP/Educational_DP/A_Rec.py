"""メモ化再帰でとく
"""

n = int(input())
h = list(map(int, input().split()))
INF = 2 ** 60

def chmin(a, b):
    if a > b:
        a = b
    return a

def rec(i):
    #DPの値が更新されていたらそのままリターン
    if dp[i] < INF:
        return dp[i]
    #ペースケース: 足場0のコストは0
    if i == 0:
        return 0

    #答えを出す変数をINFで初期化
    res = INF

    #足場 i - 1 からきた場合
    res = chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))

    #足場 i - 2 からきた場合
    if i > 1:
        res = chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    #メモ化しながら返す
    dp[i] = res
    return dp[i]

dp = [INF] * n

print(rec(n - 1))
