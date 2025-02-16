"""
有向閉路を持つ有向グラフに対して最短路を求めるアルゴリズム
始点sから到達できる負閉路が存在するならばその旨を報告し、
負閉路が存在しないならば各頂点uへの最短路を求めるアルゴリズム
"""
"""
・有向閉路を含むアルゴリズムでは、有効な辺緩和順序が不明
→「各辺に対して一通り緩和する(順序は不問)」という操作を、
　最短路長推定値d[v]が更新されなくなるまで反復する
(∵始点sから到達可能な負閉路を持たない場合には、
高々|v| - 1回の反復によって、d[v]の値が真の最短路長d*[v]に収束するため)
逆に、始点sから到達可能な負閉路をもつならば、|v|回目の反復時にある辺e = (u, v)が存在して、
辺eに関する緩和によってd[v]の値が更新される
"""
"""
計算量
O(|V||E|)
"""

"""
Sample
6 12 0
0 1 3
0 3 100
1 2 50
1 3 57
1 4 -4
2 3 -10
2 4 -5
2 5 100
3 1 -5
4 2 57
4 3 25
4 5 8
"""
#無限大を表す値
INF = 1 << 60

#緩和を実施する関数
def chmin(a, b):
    if a > b:
        return True
    else:
        return False

#頂点、辺数、始点
n, m, s = map(int, input().split())

#グラフ
#有向グラフ
g = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    g[a].append([b, w])
#print("g = " + str(g))

#ベルマン・フォード法
exist_negative_cycle = False #負閉路を持つかどうか
dist = [INF] * n
dist[s] = 0
for iter in range(n):
    update = False #更新が発生したかどうかを表すフラグ
    for v in range(n):
        if dist[v] == INF: #dist[v] = INFのときは、頂点vからの緩和を行わない
            continue
        for e in g[v]:
            #緩和処理を行い、更新されたらupdateをTrueにする
            e_to = e[0]; e_w = e[1]
            #print(e_to, e_w)
            if chmin(dist[e_to], dist[v] + e_w):
                dist[e_to] = min(dist[e_to], dist[v] + e_w)
                update = True
    #更新が行われなかったら、すでに最短経路が求められている
    if not update:
        break
    #n買い目の反復で更新が行われたならば、負閉路を持つ
    if iter == n - 1 and update:
        exist_negative_cycle = True

#結果出力
if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for v in range(n):
        if dist[v] < INF:
            print(dist[v])
        else:
            print("INF")
