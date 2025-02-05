n, k = map(int, input().split())
a = list(map(int, input().split()))

max_a = max(a)
u = [0] * (max_a + 1)
for i in range(n):
    u[a[i]] += 1

ans = 0
for i in range(len(u)):
    ans += min(u[i], k)
    k = min(u[i], k)
print(ans)
