"""頂点と変数"""
n, m = map(int, input().split())

"""グラフ"""
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a) #無向グラフの場合は追加

print(g)
