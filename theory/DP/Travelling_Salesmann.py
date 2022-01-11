"""
巡回セールスマン問題
bit DP は、n個の要素の順列 (n!通り) としてありうるものの中から最適なものを求めたい場面使えるテクニック。
O(n!)→O(n * (2 ** n))まで削減
"""
"""
dp[S] := 全体集合 {0,1,…,n−1} の部分集合 SS について、
その中で順序を最適化したときの、Sの中での最小コスト
bit DP フレームワークでは、以下のような漸化式が成立することが多い:

dp[S] = min i∈S (dp[S - {i}] + cost(S \ {i}, i))
"""
"""
S についてその中で順序を最適化したときのコスト dp[S] を計算したいのですが、
その順序の最後の要素がなんだったかで場合分けします:
S の最後が i だったとき、S の最後の i を除いた部分集合についての最適解は dp[S - {i}] になります。
S - {i} に i を加えて増えるコストを cost(S \ {i}, i) とすると、
結局最小コストは dp[S - {i}] + cost(S - {i}, i) になります。

あとは i を i∈S の範囲で全部試してあげて、
総合的に一番コストが小さかったものを採用します。
以上をまとめると bit DP フレームワークは以下のように表せます:

＜bit DP 遷移式＞

dp[S] = min i∈S  (dp[S - {i}] + cost(S - {i}, i))
＜初期値＞

dp[0] = 0　(何もない初期状態)
＜最終的な最小コスト＞

dp[(1<<n) - 1]
"""

INF = 10 ** 9
n = int(input())
dist = [[None] * n for _ in range(n)]

#メモ化再帰
dp = [[None] * (n) for _ in range(1 << n)]
def rec(bit, v):
    #すでに探索済ならリターン
    if dp[bit][v] != -1:
        return dp[bit][v]

    #初期値
    if bit == (1 << v):
        dp[bit][v] = 0
        return dp[bit][v]

    #答えを格納する変数
    res = INF

    #bitのvを除いたもの
    prev_bit = bit & ~(1 << v)

    #vの手前のノードとしてuを全探索
    for u in range(n):
        if not prev_bit & (1 << u): #uがprev_bitになかったらダメ
            continue

        #再帰的に探索
        if res > rec(prev_bit, u) + dist[u][v]:
            res = rec(prev_bit, u) + dist[u][v]

    dp[bit][v] = res
    return dp[bit][v]

for i in range(n):
    c = list(map(int, input().split()))
    for j in range(n):
        dist[i][j] = c[j]

#テーブルを全て−１にしておく
for bit in range(1 << n):
    for v in range(n):
        dp[bit][v] = -1
#print(dp)

#探索
res = INF
for v in range(n):
    if res > rec((1 << n) - 1, v):
        res = rec((1 << n) - 1, v)
    print(v, dp)
print(res)
