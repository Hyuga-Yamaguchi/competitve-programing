"""有向グラフGの２頂点s, tが与えられた時、sから辺を辿ってtに到達できるかどうかを判定
sを始点としたDFSを実施　DFS実施後においてseen配列を見ることで,各頂点が探索されたかどうかを判定
"""
"""
再帰関数によるDFSで実施
"""

def dfs(g, v):
    seen[v] = True

    for next_v in g[v]:
        if seen[next_v]:
            continue
        dfs(g, next_v)

N, M, s ,t = map(int, input().split())

seen = [False] * N
g = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)

dfs(g, s)

if seen[t]:
    print("Yes")
else:
    print("No")
