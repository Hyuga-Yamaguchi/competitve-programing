n, m = map(int, input().split())
a = [None] * m; b = [None] * m
for i in range(m):
    A, B = map(int, input().split())
    a[i] = A - 1; b[i] = B - 1
k = int(input())
c = [None] * k; d = [None] * k
for i in range(k):
    C, D = map(int, input().split())
    c[i] = C - 1; d[i] = D - 1

ans = 0
for bit in range(1 << k):
    lis = [0] * k
    for i in range(k):
        if (bit >> i) & 1:
            lis[i] += 1
    print("lis = " + str(lis))
    u = [0] * n
    for i in range(k):
        if lis[i] == 0:
            u[c[i]] += 1
        else:
            u[d[i]] += 1
    print("u = " + str(u))
    tmp = 0
    for i in range(m):
        if u[a[i]] > 0 and u[b[i]] > 0:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
