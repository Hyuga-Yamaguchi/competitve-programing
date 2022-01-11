import sys
import copy

a = list(list(input()) for _ in range(10))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#陸 = 1, 海 = 0
for i in range(10):
    for j in range(10):
        if a[i][j] == "o":
            a[i][j] = 1
        if a[i][j] == "x":
            a[i][j] = 0
b = copy.deepcopy(a)

def dfs(h, w):
    a[h][w] = 0

    #四方向を探索
    for dir in range(4):
        nh = h + dx[dir]
        nw = w + dy[dir]

    #場外アウトしたり、0のときはスルー
        if nh < 0 or nh >= 10 or nw < 0 or nw >= 10:
            continue
        if a[nh][nw] == 0:
            continue
        dfs(nh, nw)

cnt_lis = []
for i in range(10):
    for j in range(10):
        a = copy.deepcopy(b)
        a[i][j] = 1
        # if i == 0 and j == 1:
        #     print(b)
        #     print(a)

        cnt = 0
        for h in range(10):
            for w in range(10):
                if a[h][w] == 0:
                    continue #残島じゃなければスルー
                dfs(h, w)
                cnt += 1
        cnt_lis.append(cnt)

#print(cnt_lis, len(cnt_lis))
if 1 in cnt_lis:
    print("YES")
else:
    print("NO")
