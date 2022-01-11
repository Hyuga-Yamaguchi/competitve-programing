"""二部グラフ(bipartite graph)とは
与えられた無向グラフについて、以下の条件を満たすように全頂点を白か黒に塗り分けられるグラフのこと
「白頂点同士がへんで結ばれることなく、黒頂点同士が辺d結ばれることもない」
考え方
始点を白に塗るとし、
・白頂点に隣接した頂点は黒でなければならない
・黒頂点に隣接した頂点は白でなければならない
"""

import sys
sys.setrecursionlimit(10 ** 7)

#２部グラフ判定
#color[v] = 1（黒確定）, 0（白確定）, −１（未訪問）
def dfs(g, v, cur = 0):
    color[v] = cur

    for next_v in g[v]:
        #隣接頂点がすでに色が確定していた場合
        if color[next_v] != -1:
            #同じ色が隣接していた場合は二部グラフでない
            if color[next_v] == cur:
                return False
            #色が確定した場合には探索しない
            continue

        #隣接頂点の色を変えて、再起的に探索(一回でもfalseが帰ってきたらfalse)
        if not dfs(g, next_v, 1 - cur):
            return False
    return True

N, M = map(int, input().split())

color = [-1] * N
g = [[] for _ in range(N)]

for i in range (M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

#探索
is_bipartite = True
for v in range(N):
    if color[v] != -1: #探索済だったらスルー
        continue
    if not dfs(g, v):
        is_bipartite = False

if is_bipartite:
    print("Yes")
else:
    print("No")
