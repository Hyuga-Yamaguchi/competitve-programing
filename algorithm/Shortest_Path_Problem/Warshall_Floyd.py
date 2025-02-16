"""
全点対間最短路問題(ワーシャルフロイド法)
=グラフの全頂点対間について最短路長を求める
"""
"""
ワーシャルフロイド法における動的計画法
dp[k][i][j]←頂点0, 1, ...., k - 1のみを中継頂点として通ってよいとした場合の、頂点iからjへの最短路長

・初期条件
dp[0][i][j] = 0 (i = j)
            = l(e) (辺e = (i, j)が存在する)
            = INF (それ以外)

・漸化式
  dp[k + 1][i][j](i = 0, 1, ,,,|V| - 1, j = 0, 1, ,,,,|V| - 1) =
　1.新たに使用できる頂点kを使用しない場合: dp[k][i][j]
  2.新たに使用できる頂点kを使用する場合: dp[k][i][k] + dp[k][k][j]

この２通りのうち、値が小さい方を採用する
dp[k + 1][i][j] = min(dp[k][i][j], dp[k][i][k] + dp[k][k][j])
"""
"""
Sample
6 9
0 1 3
0 2 5
1 2 4
1 3 12
2 3 9
2 4 4
3 5 2
4 3 7
4 5 8
"""
#無限大を表す値
INF = 1 << 60

#頂点数、辺数
n, m = map(int, input().split())

#dp配列
dp = [[INF] * n for _ in range(n)]

#dp初期条件
for e in range(m):
    a, b, w = map(int, input().split())
    dp[a][b] = w
for v in range(n):
    dp[v][v] = 0

#dp遷移(ワーシャルフロイド法)
for k in range(n):
    print("k = " + str(k))
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            print("dp = " + str(dp))

#結果出力
#もしdp[v][v] < 0なら負閉路が存在する
exist_negative_cycle = False
for v in range(n):
    if dp[v][v] < 0:
        exist_negative_cycle = True
if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for i in range(n):
        for j in range(n):
            if j:
                print(" ", end = "")
            if dp[i][j] < INF // 2:
                print(dp[i][j], end = "")
            else:
                print("INF", end = "")
        print("")
