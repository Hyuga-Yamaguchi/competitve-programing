r, c = map(int, input().split())
xy = list(list(map(int, input().split())) for _ in range(r))

ans = 0
for bit in range(1 << r):
    lis = [[-1] * c for _ in range(r)]
    for i in range(r):
        if (bit >> i) & 1:
            for j in range(c):
                if xy[i][j] == 1:
                    lis[i][j] = 0
                elif xy[i][j] == 0:
                    lis[i][j] = 1
        else:
            for j in range(c):
                if xy[i][j] == 1:
                    lis[i][j] = 1
                elif xy[i][j] == 0:
                    lis[i][j] = 0

    tmp = 0
    for i in range(c):
        column = 0
        for j in range(r):
            column += lis[j][i]
        tmp += max(column, r - column)
    ans = max(ans, tmp)
print(ans)
