from collections import deque

n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    lis = list(map(int, input().split()))
    for j in range(2, len(lis)):
        g[lis[0] - 1].append(lis[j] - 1)

#print(g)

import sys
sys.setrecursionlimit(10 ** 9)

time = []
#深さ優先探索
def dfs(G, v):
    seen[v] = True #vを訪問済みにする
    time.append(v)

    #vから行ける各頂点next_vについて
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)
    time.append(v)


seen = [False] * n
for i in range(len(seen)):
    if seen[i]:
        continue
    dfs(g, i)

ans = []
for i in range(n):
    for j in range(len(time)):
        if i == time[j]:
            ans.append(j + 1)

for i in range(len(ans)):
    if i % 2 == 0:
        print(i // 2 + 1, ans[i], ans[i + 1])
