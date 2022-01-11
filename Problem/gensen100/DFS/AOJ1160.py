import sys
sys.setrecursionlimit(10 ** 9)

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        exit()
    c = [None] * h
    for i in range(h):
        c[i] = list(map(int, input().split()))
    #print(c)

    def dfs(x, y):
        if not (0 <= x < h) or not (0 <= y < w) or c[x][y] == 0:
            return

        c[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 0:
                continue
            dfs(i, j)
            cnt += 1
    print(cnt)
