"""
巡回セールスマン問題
"""
"""
基本形は、
dp[S] := 全体集合{0, 1,..., n - 1}の部分集合Sについて、その中で順序を最適化した時の、Sの中での最小コスト
<漸化式>
dp[S] = min(i ∈ S | dp[S - {i}] + cost(S - {i}, i))
であり、cost(S - {i}, i)を計算できる必要がある。
しかし、S - {i}のうち、どの都市が最後だったかに依存してしまうため、このままでは一つに決まらない.
よって以下のようにDPテーブルを修正する

dp[S][v] := 全体集合{0, 1,..., n - 1}の部分集合Sについて、最後がvであると言う制約のもとで順序を最適化した時の、Sの中での最小コスト
<漸化式>
dp[S][v] := min(u ∈ S - {v} | dp[S - {v}][u] + dist[u][v])
Sの最後はvだとわかっているため、S - {v}の最後が何かで場合分けしている.
<初期値>
dp[1 << v][v] = 0
<最終的なコスト>
min(v | dp[(1 << n) - 1][v])
"""

import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
dist = [None] * n
for i in range(n):
    D = list(map(int, input().split()))
    dist[i] = D
print(dist)

dp = [[-1] * (n + 1) for _ in range((1 << n) + 1)]

def rec(bit, v):
    #既に探索済みだったらリターン
    if dp[bit][v] != -1:
        return dp[bit][v]

    #初期値
    if bit == 1 << v:
        dp[bit][v] = 0
        return dp[bit][v]

    #答えを格納する変数
    res = 10 ** 18

    #bitのvを除いたもの
    prev_bit = bit & ~(1 << v)

    #vを手前のノードとしてuを全探索
    for u in range(n):
        if not prev_bit & (1 << u):
            continue #uがprev_bitになかったらダメ

        #再帰的に探索
        if res > rec(prev_bit, u) + dist[u][v]:
            res = rec(prev_bit, u) + dist[u][v]

    dp[bit][v] = res
    print(dp)
    return dp[bit][v] #メモしながらリターン

res = 10 ** 18
for v in range(n):
    if res > rec((1 << n) - 1, v):
        res = rec((1 << n) - 1, v)
print(res)

"""Sample
3
0 5 2
5 0 4
2 4 0

4
0 8 7 3
8 0 9 1
7 9 0 4
3 1 4 0
"""
