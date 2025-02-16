"""
単純なダイクストラ法
疎グラフ(|E| = O(|V|))に使用(O(|E|log|V|))
"""
"""
全ての辺が非負のときに使用可能
"""
'''
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
'''


from heapq import heappush, heappop

INF = 1 << 60

n, m, s = map(int, input().split()) #頂点数、辺数、始点

g = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    g[a].append([b, w])

#ダイクストラ法
def dijkstra_heap(s, n):
    dist = [INF] * n
    dist[s] = 0

    #(d[v], v)のペアを要素としたヒープを作る
    hq = [(dist[s], s)]
    seen = [False] * n #ノードが確定済みかどうか

    while hq:
        #v:使用済みでない頂点のうち、d[v]が最小の頂点
        #d:vに対するキー値
        v = heappop(hq)[1] #heappopで現時点の最小値を取り出す
        print("v = " + str(v))
        seen[v] = True
        print("seen = " + str(seen))
        for to, cost in g[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                print("to = " + str(to))
                print("dist[to]1 = " + str(dist[to]))
                print("dist[v] = " + str(dist[v]))
                print("cost = " + str(cost))
                dist[to] = dist[v] + cost
                print("dist[to]2 = " + str(dist[to]))
                print("hq1 = " + str(hq))
                heappush(hq, (dist[to], to))
                print("hq2 = " + str(hq))
                print("dist = " + str(dist))
        print("------------------------------------------------")
    return dist

dist = dijkstra_heap(s, n)
print(dist)
