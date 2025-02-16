import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)

from collections import deque

def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


# 0からの各頂点の距離
d = bfs(0)
print(d)


from collections import deque

INF = 10 ** 18

def bfs(sy, sx):
    queue = deque([[sx, sy]])
    dist[sx][sy] = 0
    while queue:
        y , x = queue.popleft()
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = y + dy, x + dx
            if maze[ny][nx] == '#':
                continue
            if dist[ny][nx] != INF:
                continue
            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))


R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1

maze = [input() for _ in range(R)]
dist = [[INF] * C for _ in range(R)]

bfs(sy, sx)
print(dist[gy][gx])
