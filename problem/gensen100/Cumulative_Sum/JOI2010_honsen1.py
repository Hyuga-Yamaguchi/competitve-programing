n, m = map(int, input().split())
s = [None] * n
for i in range(n - 1):
    s[i] = int(input())
a = [None] * m
for i in range(m):
    a[i] = int(input())

lis = [0] * n
for i in range(1, n):
    lis[i] = lis[i - 1] + s[i - 1]
#print(lis)

ans = 0; cur = 0
for i in range(m):
    ans += abs(lis[a[i] + cur] - lis[cur])
    cur += a[i]
print(ans % 100000)
