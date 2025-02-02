#根無し木の走査

#v:現在探索中の頂点, p:vの親(vが根のときはp=-1)
def dfs(g, v, p = -1):
    print("on the way(v)", v)
    for c in g[v]:
        if c == p:
            continue #探索が親方向へ逆流するのを防ぐ
        #print("on the way(c)", c)

        #cはvの各子頂点を動く。この時,cの親はvとなる
        dfs(g, c, v)
        #print("on the way back(c)", c)
    print("on the way back(v)", v)

n = int(input()) #頂点数
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
print(g)

dfs(g, 0)

"""sample"""
"""
15
0 1
0 4
0 11
1 2
1 3
4 5
4 8
5 6
5 7
8 9
8 10
11 12
11 13
13 14
"""
