import sys
sys.setrecursionlimit(10 ** 9)

#深さ優先探索
def dfs(G, v):
    seen[v] = True #vを訪問済みにする
    print("seen = " + str(seen))

    #vから行ける各頂点next_vについて
    for next_v in G[v]:
        print("next_v = " + str(next_v))
        if seen[next_v]:
            continue
        dfs(G, next_v)

#頂点数nと辺数m,探索を開始する頂点s
n, m = map(int, input().split())
s = int(input())

#グラフの入力
g = [[] for _ in range(m)]
#g[i]は各頂点iに対し、隣接している頂点をリスト化している
#有向グラフ
for i in range (m):
    a, b = map(int, input().split())
    g[a].append(b)

#探索
seen = [False] * n #初期状態では全頂点が未訪問
for v in range(n):
    if seen[v]:
        continue #すでに訪問済みなら探索しない
    dfs(g, v)
