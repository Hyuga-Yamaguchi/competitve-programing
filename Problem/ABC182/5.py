h, w, n, m = map(int, input().split())

#横
s = [[0] * w for _ in range(h)]
#縦
v = [[0] * w for _ in range(h)]

for i in range(n):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    v[a - 1][b - 1] = 1

for i in range(m):
    c, d = map(int, input().split())
    s[c - 1][d - 1] = -1
    v[c - 1][d - 1] = -1

#print(s, v)

for i in range(w):
    x = 0
    flag = False
    for j in range(h):
        if s[j][i] == 1:
            flag = True
        if s[j][i] == -1:
            if flag:
                flag = False
                for k in range(x, j):
                    s[k][i] = 1
            x = j + 1
        if j == h - 1 and flag:
            for k in range(x, h):
                s[k][i] = 1

for i in range(h):
    y = 0
    flag_2 = False
    for j in range(w):
        if v[i][j] == 1:
            flag_2 = True
        if v[i][j] == -1:
            if flag_2:
                flag_2 = False
                for k in range(y, j):
                    v[i][k] = 1
            y = j + 1
        if j == w - 1 and flag_2:
            for k in range(y, w):
                v[i][k] = 1
#print(s, v)
for i in range(h):
    for j in range(w):
        s[i][j] += v[i][j]
#print(s)
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] > 0:
            ans += 1
print(ans)
