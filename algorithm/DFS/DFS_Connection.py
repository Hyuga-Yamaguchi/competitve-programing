def dfs(g, v):
    seen[v] = True

    for next_v in g[v]:
        if seen[next_v]:
            continue
        dfs(g, next_v)

N, M = map(int, input().split())

seen = [] * N
g = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(N):
    seen.append(False)

cnt = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(g, v)
    cnt += 1

print(cnt)
