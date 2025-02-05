n, m = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

ans = 0
for j in range(m - 1):
    for k in range(j, m):
        cur = 0
        for i in range(n):
            cur += max(a[i][j], a[i][k])
        ans = max(ans, cur)
print(ans)
