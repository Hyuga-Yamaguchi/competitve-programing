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
