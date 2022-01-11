R, C = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1; sx -= 1
gy, gx = map(int, input().split())
gy -= 1; gx -= 1
c = [[None] * C for _ in range(R)]
for i in range(R):
    ci = input()
    for j in range(C):
        c[i][j] = ci[j]
#print(c)

from collections import deque

INF = 10 ** 18

def bfs(sy, sx):
    queue = deque([[sx, sy]])
    dist[sy][sx] = 0
    while queue:
        [y, x] = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if c[ny][nx] == "#":
                continue
            if dist[ny][nx] != INF:
                continue
            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))

dist = [[INF] * C for _ in range(R)]
bfs(sy, sx)
print(dist[gy][gx])
