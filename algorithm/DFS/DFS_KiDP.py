"""
根なし木を根付き木としたときの各頂点の深さを求める
"""
"""
各頂点vを根とする部分木のサイズsubtree_size[v]を考える.
subtree_size[v] = 1 + sigma(c:(vの子頂点), subtree_size[c])
*１を足すのは頂点v自身を足している

各頂点の深さ:行きがけ時に求めたタイミング
各頂点を根としたときの部分木のサイズ：帰りがけ時に求めたタイミング
"""
"""
Sample
15
0 1
0 2
0 3
1 4
1 5
2 6
2 7
3 8
3 9
6 10
6 11
7 12
7 13
9 14
"""
#木上の探索
#d:頂点の深さv(vが根の時はd = 0)
def dfs(g, v, p = -1, d = 0):
    depth[v] = d
    for c in g[v]:
        if c == p:
            continue #探索が親方向へ逆流するのを防ぐ
        dfs(g, c, v, d + 1) #dを1増やして子頂点へ

    #帰りがけ時に、部分木のサイズを求める
    subtree_size[v] = 1 #自分自身
    for c in g[v]:
        if c == p:
            continue
        #子頂点を根とする部分木のサイズを加算する
        subtree_size[v] += subtree_size[c]

n = int(input()) #頂点数(木なので辺数はn - 1で確定)
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

#探索
root = 0
depth = [0] * n
subtree_size = [0] * n
dfs(g, root)

#結果
for v in range(n):
    print(str(v) + ": depth = " + str(depth[v]))
    print("subtree_size = " + str(subtree_size[v]))
