n = int(input())
a, b = [], []
for i in range(n):
    A, B = map(int, input().split())
    a.append(A); b.append(B)

INF = 10 ** 12
lis = a + b #print(len(lis))
ans = INF
for j in range(2 * n):
    for k in range(2 * n):
        cur = 0
        for i in range(n):
            cur += abs(lis[j] - a[i]) + abs(a[i] - b[i]) + abs(lis[k] - b[i])
        ans = min(ans, cur)
print(ans)
