w, h, n = map(int, input().split())
xya = list(list(map(int, input().split())) for _ in range(n))

x, y, a = [], [], []
for i in range(n):
    x.append(xya[i][0])
    y.append(xya[i][1])
    a.append(xya[i][2])

lis = [[0] * (h) for _ in range(w)]
for i in range(n):
    if a[i] == 1:
        for j in range(x[i]):
            for k in range(h):
                lis[j][k] += 1
    if a[i] == 2:
        for j in range(x[i], w):
            for k in range(h):
                lis[j][k] += 1
    if a[i] == 3:
        for j in range(w):
            for k in range(y[i]):
                lis[j][k] += 1
    if a[i] == 4:
        for j in range(w):
            for k in range(y[i], h):
                lis[j][k] += 1
#print(lis)
ans = 0
for i in range(w):
    for j in range(h):
        if lis[i][j] == 0:
            ans += 1
print(ans)
