from collections import deque

def bfs(sy, sx):
    INF = 10 ** 9
    dist = [[INF] * w for _ in range(h)]
    queue = deque([[sy, sx]])
    dist[sy][sx] = 0
    while queue:
        [y, x] = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if not 0 <= ny < h or not 0 <= nx < w:
                continue
            if maze[ny][nx] == "X":
                continue
            if dist[ny][nx] != INF:
                continue
            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))
    return dist

h, w, n = map(int, input().split())
maze = [input() for _ in range(h)]
s0x, s0y = None, None
#print(maze)

lis = [None] * n
for i in range(h):
    for j in range(w):
        if maze[i][j] == "S":
            s0y = i; s0x = j
        #print(i, j)
        for k in range(1, 10):
            if maze[i][j] == str(k):
                lis[k - 1] = [i, j]
            #print(maze[i][j], str(k), i, j)
#print(lis)
#print(s0y, s0x)
ans = 0
for i in range(n):
    gy = lis[i][0]; gx = lis[i][1]
    if i == 0:
        ans += bfs(s0y, s0x)[gy][gx]
    if i >= 1:
        sy = lis[i - 1][0]; sx = lis[i - 1][1]
        ans += bfs(sy, sx)[gy][gx]
    #print(dist)
print(ans)
