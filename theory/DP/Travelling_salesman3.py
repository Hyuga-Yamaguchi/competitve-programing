"""
配るDP
"""
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


n = int(input())
dist = [None] * n
for i in range(n):
    D = list(map(int, input().split()))
    dist[i] = D
print(dist)

INF = 10 ** 9

dp = [[INF] * (n + 1) for _ in range((1 << n))]
#各始点の初期値を0にする
for i in range(n):
    if i != 0:
        dp[(1 << i)][i] = 0

for S in range(1 << n): #S:= {0, 1,..., n - 1}の部分集合
    for v in range(n): #v:= 各点　ただし、部分集合(S)に追加する要素(当然、探索するときはSには含まれない)
        for u in range(n): #u:=各点　ただし、部分集合(S)の最後の要素(当然、探索するときはSに含まれる)
            if S != 0 and not (S & (1 << u)):
                continue
                # 部分集合Sについて、Sがから集合ではなく、
                #最後の要素をuで探索し、それを含まない場合は、何もしない
            if (S & (1 << v)) == 0:
                #部分集合Sに対して、それを含んでいない要素vを決める
                #u->始点,v->終点となる
                if v != u:
                    #u->vに経路がある場合は、それを探索するとコストが最大化するので、探索しない
                    #部分集合Sにvを追加したものので、Sの最終要素がvのものは、
                    #現時点の値と(部分集合Sで始点uの値+u->vのコスト)の最小値をとる
                    dp[S | (1 << v)][v] = min(dp[S | (1 << v)][v], dp[S][u] + dist[u][v])
                # else:
                #     print("v == u",S, v, u)


print(dp)

ans = INF + 1
for i in range(n + 1):
    ans = min(ans, dp[(1 << n) - 1][i])
print(ans)

"""Sample
Input =
3
0 5 2
5 0 4
2 4 0
Output =
6

Input =
4
0 8 7 3
8 0 9 1
7 9 0 4
3 1 4 0
Output =
11

"""
