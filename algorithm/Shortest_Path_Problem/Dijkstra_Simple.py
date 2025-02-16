"""
単純なダイクストラ法
密グラフ(|E| = 0(|V| ** 2))に使用(O(|V| ** 2))
(|E|:= 辺の数,|V|:=頂点の数)
"""
"""
全ての辺が非負のときに使用可能
"""
"""
Sample
6 9 0
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
'''
sample2
8 11 0
0 1 1
0 2 2
0 3 3
0 4 4
0 5 5
1 6 100
2 6 98
3 6 96
4 6 94
5 6 92
6 7 100
'''
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

#ダイクストラ法
def dijkstra_simple(s, n): #s：始点,n:ノード数
    used = [False] * n
    dist = [INF] * n
    dist[s] = 0
    for iter in range(n):
        #使用済みでない頂点のうち、dist値が最小の頂点を探す
        min_dist = INF
        min_v = -1
        for v in range(n):
            if not used[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v
                print("min_v = " + str(min_v))
        #もしそのような頂点が見つからなければ終了する
        if min_v == -1:
            break
        #min_vを始点とした各辺を緩和する
        for e in g[min_v]:
            print("flag2")
            e_to = e[0]; e_w = e[1]
            print("e_to = " + str(e_to))
            print("dist[e_to]1 = " + str(dist[e_to]))
            print("dist[min_v] = " + str(dist[min_v]))
            print("e_w = " + str(e_w))
            dist[e_to] = min(dist[e_to], dist[min_v] + e_w)
            print("dist[e_to]2 = " + str(dist[e_to]))

        used[min_v] = True #min_vを「使用済み」とする
        print("used = " + str(used))
        print("dist = " + str(dist))
        print("----------------------------")
    return dist

#結果出力
dist = dijkstra_simple(s, n)
print(dist)
