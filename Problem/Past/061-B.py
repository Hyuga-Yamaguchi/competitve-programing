n, m = map(int, input().split())
ab = list(list(map(int, input().split())) for _ in range(m))

a, b = [], []
for i in range(m):
    a.append(ab[i][0])
    b.append(ab[i][1])

lis = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(m):
        if a[j] == i:
            lis[i] += 1
        if b[j] == i:
            lis[i] += 1
for i in range(1, n + 1):
    print(lis[i])
